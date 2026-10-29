#!/usr/bin/env python3
"""Trends Incoming pre-publish legal-hold gate (Joshua's global HOLD_REVIEW rule, 27 Oct 2026).

Rules: /workspace/content-review/RULE.md (8 hold rules + 18:25 severity amendment).
Used three ways:
  1. build.py imports it: every trend card, blog post and page is scanned before it is written.
     HIGH findings are held for Joshua; MODERATE findings are held until a SAFE ChatGPT clearance
     with the exact sha256 exists. Held items are never written to the live path, sitemap, feed,
     search index or llms.txt; a HOLD_REVIEW draft is saved and the item is queued.
  2. `python3 legal_gate.py check` (pre-push hook + GitHub Actions): rescans the rendered site and
     fails if any published page carries an unreleased finding or if a held page is on disk.
  3. `python3 legal_gate.py review <draft.json>`: runs the ChatGPT reviewer for a MODERATE item
     after the bot has made a real fix; logs the clearance on SAFE, escalates to the queue otherwise.
  Also: `python3 legal_gate.py scan <file>` to test one HTML or text file.
Releases: only an approval of the exact sha256 in approvals.jsonl (written by Joshua, never by a bot),
or for MODERATE-only items a SAFE entry with the same sha256 in moderate-clearances.jsonl.
"""
import re, os, sys, json, html, hashlib, datetime

SITE = "trendsincoming.com"
BOT = "Trends Incoming site"
CR = os.environ.get("LEGAL_GATE_CR", "/workspace/content-review")
QUEUE = os.path.join(CR, "queue.jsonl")
APPROVALS = os.path.join(CR, "approvals.jsonl")
CLEARANCES = os.path.join(CR, "moderate-clearances.jsonl")
DRAFTS = os.path.join(CR, "drafts", "trendsincoming")
REPO = os.path.dirname(os.path.abspath(__file__))
MANIFEST = os.path.join(REPO, ".legal-gate", "manifest.json")
PROVENANCE = os.path.join(REPO, ".legal-gate", "image-provenance.json")
REVIEWER = os.path.join(CR, "bin", "chatgpt_review.py")

OWN_EMAILS = {"joshuaofisrael@gmail.com"}
OWN_ADDRESS = "5640 W Maple Rd"
# Our own policy pages: rule 8 words (DMCA, takedown) describe our process there, and they need no sources.
POLICY_PAGES = {"about/", "contact/", "contact/thanks/", "terms/", "privacy/", "disclaimer/", "copyright/",
                "corrections/", "advertising-disclosure/", "search/", "trend-data/", "404"}
# Structural pages (indexes) that only list already-gated cards: no page-level rule 4 check.
STRUCTURAL = {"", "blog/", "news/", "trending-hashtags/"}

HIGH, MOD = "HIGH", "MODERATE"
# Rules that are HIGH by definition. A finding under one of these can never be released by a moderate
# clearance or a ChatGPT SAFE, whatever severity label it carries; only an exact-sha approval does.
HIGH_RULES = {1, 2, 6, 8}
RULE_NAMES = {1: "damaging allegation", 2: "sensitive personal info", 3: "unclear content rights",
              4: "unsupported claim / no source", 5: "high-impact advice", 6: "election logistics without official source",
              7: "misleading presentation", 8: "legal complaint / restriction"}

# ---------------------------------------------------------------- text helpers
def strip_html(s):
    s = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", s or "")
    s = re.sub(r"(?i)<(/p|/h\d|/li|br|/div|/tr|/td|/th|/blockquote|/section|/article|h\d|p|li|div|tr|td|blockquote)\b[^>]*>", "\n", s)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    s = re.sub(r"[ \t\r\f\v]+", " ", s)
    return re.sub(r"\n\s*", "\n", s).strip()

def sentences(text):
    out = []
    for block in text.split("\n"):
        for s in re.split(r"(?<=[.!?])\s+(?=[\"\u201c'(A-Z0-9])", block):
            s = s.strip()
            if len(s) > 2: out.append(s)
    return out

def norm(s): return re.sub(r"\s+", " ", (s or "")).strip().lower()
def shash(s): return hashlib.sha256(norm(s).encode()).hexdigest()[:20]

def links_of(h):
    return [u for u in re.findall(r'href="(https?://[^"]+)"', h or "") if "trendsincoming.com" not in u]

def imgs_of(h, ld=None):
    out = re.findall(r'<img[^>]+src="([^"]+)"', h or "")
    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if k in ("image", "thumbnailUrl", "contentUrl", "logo"):
                    if isinstance(v, str): out.append(v)
                    elif isinstance(v, dict) and isinstance(v.get("url"), str): out.append(v["url"])
                    elif isinstance(v, list): out.extend(x for x in v if isinstance(x, str))
                walk(v)
        elif isinstance(o, list):
            for x in o: walk(x)
    walk(ld)
    IMG = re.compile(r"\.(?:png|jpe?g|webp|gif|avif|svg)(?:\?|$)|ytimg\.com/", re.I)
    return [u for u in out if IMG.search(u)]

# Pages awaiting a review decision. Paragraphs, list items and links pointing at them are left out of every
# page's hash, so a page's sha256 does not change when one of these is held or released. They are still
# rendered and scanned in full when the target is live; only the hash input is fixed.
REVIEW_LINK_KEYS = ("politics/alaska-senate-certification-lawsuit/", "world/france-protests-2026/",
                    "world/serbia-election-2026/", "world/israel-election-2026/", "blog/election-sunday-serbia-brazil-2026/")
def _hash_body(b):
    for k in REVIEW_LINK_KEYS:
        seg = re.escape(k.rstrip("/").split("/")[-1])
        hr = r'href="(?:[^"]*/)?' + seg + r'/(?:index\.html)?(?:#[^"]*)?"'
        if not re.search(hr, b): continue
        b = re.sub(r'(?s)<(p|li)\b[^>]*>(?:(?!</\1>).)*?' + hr + r'(?:(?!</\1>).)*?</\1>', "", b)
        b = re.sub(r'(?s)<a\b[^>]*' + hr + r'[^>]*>.*?</a>', "", b)
    return b

def content_sha(title, desc, body, ld=None):
    """sha256 of the exact visible version: title, description, body text, link targets, images, JSON-LD."""
    body = _hash_body(body)
    parts = [title or "", desc or "", strip_html(body), " ".join(links_of(body)), " ".join(imgs_of(body, ld)),
             json.dumps(ld, sort_keys=True) if ld else ""]
    return hashlib.sha256(norm("\n".join(parts)).encode()).hexdigest()

# ---------------------------------------------------------------- entity detection
STOP = set("""a an the in on at for and but or if it its this that these those we you our your he she they his her their
what when where why how who yes no not live update updated sources source read latest more new next first last our
monday tuesday wednesday thursday friday saturday sunday january february march april may june july august september
october november december jan feb mar apr jun jul aug sep sept oct nov dec et gmt bst pt ct est edt pst pdt am pm us u.s
uk usa eu also after before during per as by from with to of so then here there all any some each every one two three
watch tickets ticket game games season week day night today tonight tomorrow quick answers why's what's trend trends
trending explainer guide follow keep heads note fact check checked officials official police authorities experts researchers reports
report critics fans players people residents protesters analysts witnesses observers sheet sheets most many""".split())
TOKEN = re.compile(r"[A-Z][A-Za-z0-9&'\u2019.\-]*[A-Za-z0-9]|[A-Z]{2,}")

def entities(sent):
    ents = []
    for m in TOKEN.finditer(sent):
        w = m.group(0).strip(".'\u2019")
        if w.lower() in STOP or len(w) < 2: continue
        ents.append(w)
    return ents

ORGWORDS = set("""elementary school high university college hospital national department police red cross city county state states
united airport terminal oil senate house court supreme ministry party rally games records news times post journal inc corp
company group bank center centre street park stadium arena festival day eve series league cup awards church market exchange
commission committee agency office service administration board council reserve federal security social international
world tv network studios studio entertainment media press club team fc
jazeera reuters afp bbc cnn nbc abc cbs fox npr pbs guardian independent euronews anadolu ynet politico axios bloomberg""".split())
NAME = re.compile(r"\b([A-Z][a-z\u00e0-\u00ff'\u2019-]+(?:\s+[A-Z][a-z\u00e0-\u00ff'\u2019-]+){1,2})\b")
def person_names(sent):
    out = []
    for m in NAME.finditer(sent):
        ws = [w.strip("'\u2019").removesuffix("'s").removesuffix("\u2019s") for w in m.group(1).split()]
        if any(w.lower() in ORGWORDS or w.lower() in STOP for w in ws): continue
        out.append(" ".join(ws))
    return out

def has_entity(sent, kw_span=None):
    ents = entities(sent)
    if kw_span:
        kw = sent[kw_span[0]:kw_span[1]].lower()
        ents = [e for e in ents if e.lower() not in kw and kw not in e.lower()]
    return ents

# ---------------------------------------------------------------- rule patterns
R1 = re.compile(r"\b(fraud\w*|scam(?:s|med|mer|mers)?\b|embezzl\w*|brib(?:e|es|ed|ery)\b|corrupt(?:ion|ly)?\b|money launder\w*|launder(?:ed|ing)\b|"
                r"indict\w*|charged with|faces? charges|criminal charges?|arrested|under arrest|convicted|conviction|pleaded guilty|found guilty|"
                r"sentenced to|alleg(?:e|es|ed|edly|ation|ations)\b|accus\w*|lawsuits?\b|sued\b|sues\b|suing\b|class action|misconduct|harass\w*|"
                r"sexual(?:ly)? assault\w*|assault(?:ed|ing)?\b|abus(?:e|ed|es|ive|er|ers|ing)\b|rape[ds]?\b|molest\w*|cover[- ]?ups?\b|covered up|"
                r"\blied\b|\blying\b|liars?\b|misled\b|mislead(?:ing)? (?:investors|customers|regulators|the public)|deceiv\w*|deceptive|deception|"
                r"falsely (?:claimed|said|stated|told|denied)|cheat(?:ed|ing|s)?\b|theft|\bstole\b|stolen(?! bases?)|insider trading|price[- ]fixing|"
                r"illegal(?:ly)?\b|unlawful(?:ly)?\b|wrongdoing|negligen\w*|racketeer\w*|extort\w*|plagiari\w*|ponzi|pyramid scheme|kickbacks?|"
                r"market manipulation|under investigation|investigated for|criminal probe|war crimes?|genocide|massacre|doping|performance-enhancing|"
                r"fined\b|misappropriat\w*|defraud\w*)", re.I)
NONPERSON_SUBJ = re.compile(r"\b(agents?|models?|AI|bots?|chatbots?|malware|software|feature|system)\b[^.]{0,90}$", re.I)
DISHONESTY = re.compile(r"lied|lying|liar|misled|deceiv|deceptive|deception|falsely|cheat", re.I)
GENERIC_ARRESTS = re.compile(r"how many (?:people |protesters )?(?:were |have been )?arrested|(?:people|protesters|demonstrators|rioters|fans) (?:were |have been )?arrested|(?:\d[\d,]*|thousands|hundreds|dozens|scores)\s+(?:\w+\s+){0,3}?(?:were\s+|are\s+|have been\s+|had been\s+)?arrest(?:ed|s)\b", re.I)
# keyword uses that are not allegations (titles, idioms, statements of law)
R1_BENIGN = re.compile(r"grand theft auto|cheat sheets?|cheat codes?|low-lying|\b(?:is|are) illegal (?:in|to|for|under)\b|illegal to (?:drink|park|fly|carry|bring)", re.I)
# court findings of record (not allegations): MODERATE, need a source + independent review
R1_RECORD = re.compile(r"^(?:convicted|conviction|pleaded guilty|found guilty|sentenced to)$", re.I)
CASUALTY = re.compile(r"(?:\d[\d,]*|dozens|hundreds|thousands|several|one|two|three|four|five|six)\s+(?:\w+\s+){0,3}?(?:were\s+|are\s+)?(?:killed|injured|wounded|hurt)|injur(?:ed|ing)\s+(?:more than|at least|about|nearly|over|some)?\s*\d|\d+\s+(?:killed|dead)[,;]?\s+\d+\s+injured", re.I)

PHONE = re.compile(r"(?<![\d.$])(?:\+?1[-. ]?)?\(?\b(\d{3})\)?[-. ](\d{3})[-. ](\d{4})\b|\+44\s?\d{2,4}\s?\d{3,4}\s?\d{3,4}")
TOLLFREE = {"800", "833", "844", "855", "866", "877", "888"}
EMAIL = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
ADDRESS = re.compile(r"(?<![/\d])\b\d{1,5}\s+(?:[NSEW]\.?\s+)?(?:[A-Z][a-z]+\s+){1,3}(?:Street|St|Avenue|Ave|Road|Rd|Boulevard|Blvd|Lane|Ln|Drive|Dr|Court|Ct|Terrace|Place|Pl|Circle|Cir)\b\.?")
HEALTH = re.compile(r"\b(diagnos\w*|cancer|tumou?r|hospitali[sz]ed|in hospital|rehab\b|rehabilitation|overdos\w*|pregnan\w*|miscarriage|"
                    r"mental health|depression|anxiety|surgery|illness|terminally ill|chemotherapy|HIV|dementia|alzheimer\w*|autism|ADHD|"
                    r"eating disorder|suicid\w*|self-harm|medically cleared|not cleared|injur(?:y|ies|ed)|concussion|torn (?:ACL|MCL|labrum)|"
                    r"cause of death|died of|stroke|heart attack|sexual orientation|came out as|coming out as|\bgay\b|lesbian|bisexual|transgender|"
                    r"social security number|\bSSN\b|bank account number|routing number|credit card number|home address|private messages?|"
                    r"leaked (?:texts|messages|emails|dms|photos))\b", re.I)
MINOR = re.compile(r"\b(?:(?:[1-9]|1[0-7])-year-old|minors?\b|juvenile|child victim|teen(?:age)? victim|victims?\b|survivors? of)", re.I)

ELECTION = re.compile(r"\b(polling (?:place|location|station)s?(?!\s+(?:counted|reported|processed|tallied))|where to vote|registration deadlines?|register to vote by|voter registration (?:deadline|closes|ends)|"
                      r"eligib\w* to vote|eligible voters|who can vote|polls (?:open|close|opened|closed|are open)|"
                      r"early voting (?:starts|started|begins|began|ends|ended|runs|opens|opened|closes|period|dates?|hours|deadline|through|until|from|is underway)|"
                      r"absentee ballots? (?:deadline|requests?|must|due|postmarked)|mail[- ]in ballots? (?:deadline|requests?|must|due|postmarked)|"
                      r"voter id (?:law|requirement|rules)|same[- ]day registration|certif(?:y|ied|ies|ication)\b[^.]{0,40}\b(?:results?|winner|vote)|"
                      r"(?:final|official|certified) (?:results?|count|tally)|election day (?:is|falls|will be)|ballots? (?:must|are due)|"
                      r"provisional ballots?|cure (?:your|a) ballot)\b", re.I)
OFFICIAL_ELECTION = re.compile(r"https?://(?:[\w-]+\.)*(?:gov|gov\.[a-z]{2}|gouv\.fr|mil|eac\.gov|usa\.gov|vote\.gov|bechirot\.gov\.il|"
                               r"elections\.ca|electoralcommission\.org\.uk|aec\.gov\.au|tse\.jus\.br|rik\.parlament\.gov\.rs|"
                               r"[a-z]+\.state\.[a-z]{2}\.us|sos\.[a-z]{2}\.gov|sos\.state\.[a-z]{2}\.us)(?:/|$)", re.I)

LEGAL = re.compile(r"\b(cease[- ]and[- ]desist|dmca (?:notice|takedown|complaint|request)|takedown (?:notice|request|demand)|legal notice|"
                   r"letter before action|embargo(?:ed)?|broke the embargo|reporting restrictions?|gag order|super-?injunction|injunction|"
                   r"correction request|asked (?:us )?to remove|copyright (?:claim|complaint|strike|infringement notice)|notice of infringement|"
                   r"defamation (?:claim|complaint|notice)|right to be forgotten)\b", re.I)

ADVICE = re.compile(r"\b(you should (?:buy|sell|invest|short|stop taking|take)\b|(?:buy|sell) (?:it |the stock |shares )?(?:now|today) before|"
                    r"guaranteed (?:returns?|profits?|income|gains?|win)|risk[- ]free (?:returns?|investment|profit)|can't lose|cannot lose|"
                    r"double your money|get rich|strong buy|we recommend (?:buying|selling|investing)|(?:stop|start) taking your (?:medication|meds)|"
                    r"(?:increase|double|reduce) your (?:dose|dosage)|without (?:a|your) doctor)\b", re.I)
HYPE_ALWAYS = re.compile(r"\b(guaranteed|proof|proven|100%|shocking|you won't believe|exposed|destroys|leaked)\b", re.I)
HYPE_NEEDS_SOURCE = re.compile(r"\b(confirmed|official|officially)\b", re.I)
AFFIL = re.compile(r"\b(official partner of|endorsed by|in partnership with|sponsored by|our partners? at)\b", re.I)

# ---------------------------------------------------------------- provenance
_PROV_CACHE = {}
def load_provenance():
    p = os.environ.get("LEGAL_GATE_PROVENANCE", PROVENANCE)
    if p not in _PROV_CACHE:
        try: _PROV_CACHE[p] = json.load(open(p))
        except Exception: _PROV_CACHE[p] = None
    return _PROV_CACHE[p]

def seed_held():
    """Page keys held by the previous build, so early pages can drop links to them (build re-runs once if this changes)."""
    try: man = json.load(open(MANIFEST))
    except Exception: return []
    return sorted(k for k in man.get("held", {}) if k.endswith("/") and not k.startswith("trend-card/"))

def image_ok(src, prov):
    if prov is None: return False
    p = re.sub(r"^https?://(?:www\.)?trendsincoming\.com/", "", src).lstrip("./").lstrip("/")
    while p.startswith("../"): p = p[3:]
    for k, v in prov.get("files", {}).items():
        if k == p and v.get("status") == "documented": return True
    for pre, v in prov.get("prefixes", {}).items():
        if p.startswith(pre) and v.get("status") == "documented": return True
    return False

# ---------------------------------------------------------------- scanning
def finding(rule, sev, snippet, why):
    return {"rule": rule, "severity": sev, "snippet": snippet[:300], "why": why, "sent_hash": shash(snippet)}

def scan(title, desc, body, ld=None, sources=None, key="", kind="page"):
    """Return list of findings for one item. sources: extra list of source URLs (cards, posts)."""
    f = []
    is_policy = key in POLICY_PAGES or key.startswith("contact/")
    text = strip_html(body)
    full = "\n".join(x for x in [title or "", desc or "", text] if x)
    srcs = list(sources or []) + links_of(body)
    sents = sentences(full)
    for s in sents:
        # rule 1: wrongdoing keyword + identifiable entity in the same sentence
        if not is_policy:
          for m in R1.finditer(s):
            pre = s[:m.start()]
            kw = m.group(0)
            if R1_BENIGN.search(s[max(0, m.start()-12):m.end()+12]): continue
            if DISHONESTY.match(kw) and NONPERSON_SUBJ.search(pre): continue
            if kw.lower() in ("arrested", "arrests") and GENERIC_ARRESTS.search(s): continue
            if has_entity(s, m.span()):
                # rule 1 is always HIGH (court findings of record included): only Joshua's exact-sha approval releases it
                f.append(finding(1, HIGH, s, f"'{kw}' near named entity {has_entity(s, m.span())[:3]}")); break
        # rule 2: personal data
        if not is_policy:
            for m in PHONE.finditer(s):
                if m.group(1) and m.group(1) in TOLLFREE: continue
                f.append(finding(2, HIGH, s, f"phone number {m.group(0)}")); break
            for m in EMAIL.finditer(s):
                if m.group(0).lower() not in OWN_EMAILS:
                    f.append(finding(2, HIGH, s, f"email address {m.group(0)}")); break
            for m in ADDRESS.finditer(s):
                if OWN_ADDRESS.lower() not in s.lower():
                    f.append(finding(2, HIGH, s, f"street address '{m.group(0)}'")); break
            m = HEALTH.search(s)
            if m and m.group(0).lower().startswith(("injur", "hurt")) and CASUALTY.search(s): m = None
            w = s[max(0, m.start()-70):m.end()+70] if m else ""
            if m and person_names(w): f.append(finding(2, HIGH, s, f"health/sensitive term '{m.group(0)}' about named person {person_names(w)[:3]}"))
            m = MINOR.search(s)
            if m and person_names(s[max(0, m.start()-70):m.end()+70]): f.append(finding(2, HIGH, s, f"minor/victim term '{m.group(0)}' near named subject"))
        # rule 8
        if not is_policy:
            m = LEGAL.search(s)
            if m and re.search(r"(?:review|press) embargo|embargo (?:lifts|lifted|ends|is up)|once the embargo", s, re.I): m = None
            if m: f.append(finding(8, HIGH, s, f"legal notice/restriction marker '{m.group(0)}'"))
        # rule 5
        m = ADVICE.search(s)
        if m: f.append(finding(5, MOD, s, f"personal advice / promised return '{m.group(0)}'"))
        m = AFFIL.search(s)
        if m and not is_policy: f.append(finding(7, MOD, s, f"implied affiliation '{m.group(0)}'"))
    # rule 6: election logistics need an official election-authority link on the same item/page
    el = [s for s in sents if ELECTION.search(s)]
    if el and not any(OFFICIAL_ELECTION.match(u) for u in srcs):
        for s in el[:6]: f.append(finding(6, HIGH, s, f"election logistics '{ELECTION.search(s).group(0)}' with no official (.gov / election authority) source on this item"))
    # rule 7: headline strength
    if title:
        m = HYPE_ALWAYS.search(title)
        if m: f.append(finding(7, MOD, title, f"absolute/hype headline word '{m.group(0)}'"))
        m = HYPE_NEEDS_SOURCE.search(title)
        if m and not srcs: f.append(finding(7, MOD, title, f"headline says '{m.group(0)}' but item has no source"))
    # rule 4: material content with no source URL
    if not is_policy and key not in STRUCTURAL and not key.startswith("hubs/") and len(text) > 80 and not srcs:
        f.append(finding(4, MOD, (title or text[:120]), "no source URL on this item"))
    # rule 3: images need a documented licence/provenance record; long verbatim quotes
    prov = load_provenance()
    for src in imgs_of(body, ld):
        if not image_ok(src, prov): f.append(finding(3, MOD, src, f"image {src}: no documented licence/provenance record"))
    for q in [q for line in text.split("\n") for q in re.findall(r"\u201c([^\u201d\n]{40,})\u201d|\"([^\"\n]{40,})\"", line)]:
        q = q[0] or q[1]
        if len(q.split()) > 60: f.append(finding(3, MOD, q[:200], "verbatim quote over 60 words (copyright, not fair use by default)"))
    # de-duplicate
    seen, out = set(), []
    for x in f:
        k = (x["rule"], x["sent_hash"])
        if k not in seen: seen.add(k); out.append(x)
    return out

# ---------------------------------------------------------------- releases
def _jsonl(p):
    out = []
    if os.path.exists(p):
        for line in open(p):
            line = line.strip()
            if line:
                try: out.append(json.loads(line))
                except Exception: pass
    return out

def approved(sha):
    """Joshua's approvals of an exact version (written by him, never by a bot)."""
    for a in _jsonl(APPROVALS):
        if a.get("sha256") == sha and str(a.get("decision", a.get("status", "approved"))).lower() in ("approved", "approve", "publish", "release"):
            return a
    return None

def _revoked():
    return {c.get("revokes_sha256") for c in _jsonl(CLEARANCES) if c.get("revokes_sha256")}

def _rules_of(c):
    r = c.get("rule", [])
    return set(r if isinstance(r, list) else [r])

def cleared(sha):
    rv = _revoked()
    for c in _jsonl(CLEARANCES):
        if c.get("revokes_sha256") or sha in rv: continue
        if _rules_of(c) & HIGH_RULES: continue  # a clearance logged under a HIGH rule is never valid
        if c.get("sha256") == sha and c.get("site") == SITE and str(c.get("chatgpt_verdict", "")).upper().startswith("SAFE"):
            return c
    return None

def decide(findings, sha):
    """-> (status, release_record). status: pass | approved | cleared | hold_high | hold_moderate"""
    if not findings: return "pass", None
    a = approved(sha)
    if a: return "approved", a
    if any(x["severity"] == HIGH or x["rule"] in HIGH_RULES for x in findings): return "hold_high", None
    c = cleared(sha)
    if c: return "cleared", c
    return "hold_moderate", None

# ---------------------------------------------------------------- holding
def _slug(key): return re.sub(r"[^a-z0-9]+", "-", key.lower()).strip("-")[:80] or "home"

def save_draft(key, title, desc, body, ld, sha, findings, sources, status):
    os.makedirs(DRAFTS, exist_ok=True)
    base = os.path.join(DRAFTS, f"{_slug(key)}.{sha[:10]}.HOLD_REVIEW")
    meta = {"status": "HOLD_REVIEW", "site": SITE, "bot": BOT, "key": key, "title": title, "description": desc,
            "sha256": sha, "severity": "HIGH" if status == "hold_high" else "MODERATE", "findings": findings,
            "sources": sources[:20], "saved": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
            "note": "Unpublished. Release only by Joshua's approval of this exact sha256 in approvals.jsonl, or (MODERATE only) a SAFE ChatGPT clearance with this sha256."}
    with open(base + ".html", "w") as fh:
        fh.write("<!-- STATUS: HOLD_REVIEW (unpublished draft, do not deploy)\n" + json.dumps(meta, indent=1).replace("--", "- -") + "\n-->\n")
        fh.write(f"<h1>{html.escape(title or '')}</h1>\n<p><i>{html.escape(desc or '')}</i></p>\n{body}\n")
        if ld: fh.write('<script type="application/ld+json">' + json.dumps(ld) + "</script>\n")
    json.dump(meta, open(base + ".json", "w"), indent=1)
    return base + ".html"

def queue(key, title, sha, findings, sources, draft, suggestion=None, severity=None):
    """One HOLD_REVIEW line per held item: never duplicates key+sha, and a newer version of a still-pending item replaces its old line."""
    old = None
    for q in _jsonl(QUEUE):
        if q.get("site") == SITE and q.get("key") == key and q.get("sha256") == sha: return False
        if q.get("site") == SITE and q.get("key") == key and q.get("status") == "HOLD_REVIEW": old = q
    rules = sorted({x["rule"] for x in findings})
    sev = severity or ("HIGH" if any(x["severity"] == HIGH for x in findings) else "MODERATE")
    if not suggestion:
        sg = []
        if 1 in rules: sg.append("Joshua to approve this exact version or tell the bot to drop the allegation (do not soften it to bypass review)")
        if 2 in rules: sg.append("remove the personal/sensitive detail or Joshua approves this exact version")
        if 6 in rules: sg.append("add a current official election-authority (.gov) source confirming the logistics, or Joshua approves")
        if 8 in rules: sg.append("LEGAL NOTICE/RESTRICTION: Joshua to review before any republication")
        if sev == "MODERATE": sg.append("ChatGPT review did not return SAFE; Joshua to decide")
        suggestion = "; ".join(sg) or "Joshua to review"
    line = {"ts": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"), "site": SITE, "bot": BOT,
            "title": title, "flagged": " | ".join(f"[r{x['rule']}] {x['snippet'][:160]}" for x in findings[:6]),
            "rule": rules, "severity": sev, "sources": sources[:10], "suggestion": suggestion,
            "draft_path": draft, "status": "HOLD_REVIEW", "key": key, "sha256": sha}
    if old:
        raw = open(QUEUE).read().splitlines(True)
        out = []
        for l in raw:
            try: q = json.loads(l)
            except Exception: out.append(l); continue
            if q.get("site") == SITE and q.get("key") == key and q.get("status") == "HOLD_REVIEW": continue
            out.append(l)
        out.append(json.dumps(line) + "\n")
        tmp = QUEUE + ".tmp-legal-gate"
        open(tmp, "w").write("".join(out)); os.replace(tmp, QUEUE)
        od = old.get("draft_path") or ""
        for ext in (".html", ".json"):
            if od and od != draft and od.endswith(".html") and os.path.exists(od[:-5] + ext): os.remove(od[:-5] + ext)
        return True
    with open(QUEUE, "a") as fh: fh.write(json.dumps(line) + "\n")
    return True

PENDING = os.path.join(DRAFTS, "pending-moderate.jsonl")
def pending_moderate(key, title, sha, findings, draft):
    for q in _jsonl(PENDING):
        if q.get("key") == key and q.get("sha256") == sha: return
    os.makedirs(DRAFTS, exist_ok=True)
    with open(PENDING, "a") as fh:
        fh.write(json.dumps({"ts": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"), "key": key, "title": title,
                             "sha256": sha, "rule": sorted({x["rule"] for x in findings}), "draft_path": draft,
                             "next": "fix properly, rebuild, then run: python3 legal_gate.py review <draft.json>"}) + "\n")

class Gate:
    """Stateful gate used by build.py."""
    def __init__(self, dry=False):
        self.dry = dry or os.environ.get("LEGAL_GATE_DRY") == "1"
        self.results = {}      # key -> dict
        self.allow = set()     # sentence hashes released by approval/clearance of an item
        self.approved_allow = set()  # HIGH-rule sentence hashes released only by an exact-sha approval
        self.held_keys = set()
        self._pending = {}
    def flush(self):
        """Save drafts and queue lines for the holds of the final, converged pass."""
        for key, (k, title, desc, body, ld, sha, fs, srcs, st) in self._pending.items():
            d = save_draft(k, title, desc, body, ld, sha, fs, srcs, st)
            self.results[key]["draft_path"] = d
            if st == "hold_high": queue(k, title, sha, fs, srcs, d)
            else: pending_moderate(k, title, sha, fs, d)
        self._pending = {}
    def check(self, key, title, desc, body, ld=None, sources=None, kind="page"):
        fs = scan(title, desc, body, ld, sources, key, kind)
        fs0 = fs
        fs = [x for x in fs if x["sent_hash"] not in self.allow]
        sha = content_sha(title, desc, body + " ".join(sources or []), ld)
        st, rec = decide(fs, sha)
        prev = self.results.get(key)
        if fs0 and not fs and prev and prev["status"] in ("approved", "cleared"):
            return True  # same item, already released by its approval/clearance in an earlier stage of this build
        if st in ("approved", "cleared"):
            for x in fs:
                if x["rule"] in HIGH_RULES and st != "approved": continue  # never: a clearance cannot release a HIGH rule
                self.allow.add(x["sent_hash"])
                if st == "approved": self.approved_allow.add(x["sent_hash"])
        r = {"key": key, "kind": kind, "title": title, "sha256": sha, "status": st, "findings": fs,
             "released_by": (rec or {}).get("ts") if rec else None}
        if st.startswith("hold"):
            self.held_keys.add(key)
            srcs = list(sources or []) + links_of(body)
            if not self.dry:
                # writes are deferred to flush() so intermediate build passes never queue false holds
                self._pending[key] = (key, title, desc, body, ld, sha, fs, srcs, st)
        self.results[key] = r
        return st in ("pass", "approved", "cleared")
    def summary(self):
        from collections import Counter
        c = Counter(r["status"] for r in self.results.values())
        return dict(c)
    def write_manifest(self, published_keys):
        os.makedirs(os.path.dirname(MANIFEST), exist_ok=True)
        rel = sorted(self.allow)
        # public file (served from the site root): keys, rules and hashes only; titles and drafts stay in /workspace/content-review
        held = {k: {"status": r["status"], "rules": sorted({x["rule"] for x in r["findings"]}), "sha256": r["sha256"]}
                for k, r in self.results.items() if r["status"].startswith("hold")}
        released = {k: {"status": r["status"], "sha256": r["sha256"]} for k, r in self.results.items() if r["status"] in ("approved", "cleared")}
        json.dump({"site": SITE, "released_sentence_hashes": rel, "approved_sentence_hashes": sorted(self.approved_allow), "released_items": released, "held": held,
                   "published_pages": sorted(published_keys)}, open(MANIFEST, "w"), indent=1, sort_keys=True)

# ---------------------------------------------------------------- CI / pre-push check over the rendered site
def rendered_main(h):
    m = re.search(r"(?s)<main>(.*)</main>", h)
    if not m: return None
    b = m.group(1)
    b = re.sub(r'(?s)<p class="pnote.*?</p>|<p class="stamp">.*?</p>', " ", b)
    b = re.sub(r'(?s)<div class="share.*', " ", b)  # share bar + related links are template, scanned at their own pages
    return b

def man_high_ok(man, x):
    """A HIGH-rule sentence on a rendered page is allowed only if some released item carrying it is an exact-sha approval."""
    return x["sent_hash"] in set(man.get("approved_sentence_hashes", []))

def check_site(root=REPO):
    mp = os.path.join(root, ".legal-gate", "manifest.json")
    os.environ["LEGAL_GATE_PROVENANCE"] = os.path.join(root, ".legal-gate", "image-provenance.json")
    man = json.load(open(mp)) if os.path.exists(mp) else None
    if man is None: print("LEGAL GATE CI FAIL: .legal-gate/manifest.json missing (build.py must run the gate)"); return 1
    allow = set(man.get("released_sentence_hashes", []))
    bad = []
    if os.path.isdir(CR):  # local pre-push: every release must match a real approval or SAFE clearance with the same sha256
        for k, r in man.get("released_items", {}).items():
            ok = approved(r.get("sha256")) if r.get("status") == "approved" else cleared(r.get("sha256"))
            if not ok: bad.append(f"released item has no matching {r.get('status')} record for sha256 {str(r.get('sha256'))[:12]}: {k}")
    for k in man.get("held", {}):
        p = os.path.join(root, k, "index.html") if k.endswith("/") or k == "" else None
        if p and not k.startswith("trend-card/") and os.path.exists(p): bad.append(f"held page is on disk: {k}")
    sm = open(os.path.join(root, "sitemap.xml")).read() if os.path.exists(os.path.join(root, "sitemap.xml")) else ""
    for k in man.get("held", {}):
        if k.endswith("/") and f"trendsincoming.com/{k}<" in sm: bad.append(f"held page in sitemap: {k}")
    n = 0
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if not d.startswith(".") and d not in ("tools", "node_modules")]
        for f in fn:
            if not f.endswith(".html"): continue
            p = os.path.join(dp, f); key = os.path.relpath(dp, root).replace("\\", "/")
            key = "" if key == "." else key + "/"
            h = open(p, errors="ignore").read()
            if "STATUS: HOLD_REVIEW" in h: bad.append(f"HOLD_REVIEW draft inside the site: {key}{f}"); continue
            body = rendered_main(h)
            if body is None: continue
            n += 1
            t = re.search(r"<title>(.*?)</title>", h)
            ld = []
            for j in re.findall(r'(?s)<script type="application/ld\+json">(.*?)</script>', h):
                try: ld.append(json.loads(j))
                except Exception: pass
            fs = scan(html.unescape(t.group(1)) if t else "", "", body, ld, links_of(h), key, "rendered")
            # page-level rule 4/7 are decided at build time on the source item; CI enforces HIGH + rule 3 on output
            fs = [x for x in fs if (x["sent_hash"] not in allow or x["rule"] in HIGH_RULES and not man_high_ok(man, x)) and (x["severity"] == HIGH or x["rule"] in HIGH_RULES or x["rule"] == 3)]
            if fs: bad.append(f"{key or '/'}: " + "; ".join(f"r{x['rule']} {x['why']} :: {x['snippet'][:100]}" for x in fs[:3]))
    if bad:
        print("LEGAL GATE CI FAIL (%d problems):" % len(bad)); [print("  -", b) for b in bad[:60]]; return 1
    print(f"LEGAL GATE CI OK: {n} rendered pages scanned, {len(man.get('held', {}))} items held, none published")
    return 0

def review(draft_json, fix):
    """Run the independent ChatGPT review for a MODERATE item and log the result."""
    import subprocess
    meta = json.load(open(draft_json))
    if meta.get("severity") != "MODERATE" or any(x.get("rule") in HIGH_RULES for x in meta.get("findings", [])):
        print("Refusing: HIGH items are only released by Joshua's approval."); return 2
    htmlp = draft_json[:-5] + ".html"
    rules = sorted({x["rule"] for x in meta["findings"]})
    ctx = f"Rule(s) {rules} ({', '.join(RULE_NAMES[r] for r in rules)}). Fix made: {fix}"
    p = subprocess.run([sys.executable, REVIEWER, htmlp, ctx], capture_output=True, text=True, timeout=200)
    print(p.stdout.strip())
    try: v = json.loads(p.stdout.strip().splitlines()[-1])
    except Exception: v = {"verdict": "UNSURE", "reasons": [p.stderr[-300:]]}
    if p.returncode == 0 and v.get("verdict") == "SAFE":
        with open(CLEARANCES, "a") as fh:
            fh.write(json.dumps({"ts": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"), "site": SITE, "bot": BOT,
                                 "title": meta["title"], "key": meta["key"], "rule": rules, "fix": fix,
                                 "chatgpt_verdict": "SAFE: " + "; ".join(v.get("reasons", []))[:400], "sha256": meta["sha256"]}) + "\n")
        print("CLEARED (logged to moderate-clearances.jsonl)"); return 0
    queue(meta["key"], meta["title"], meta["sha256"], meta["findings"], meta.get("sources", []), htmlp,
          suggestion=f"MODERATE escalated: ChatGPT verdict {v.get('verdict')} ({'; '.join(v.get('reasons', []))[:300]}). Fix tried: {fix}", severity="MODERATE")
    print("ESCALATED to queue.jsonl for Joshua"); return 1

if __name__ == "__main__":
    a = sys.argv[1:] or ["check"]
    if a[0] == "check": sys.exit(check_site(a[a.index("--root") + 1] if "--root" in a else REPO))
    if a[0] == "review": sys.exit(review(a[1], a[2] if len(a) > 2 else "fix not described"))
    if a[0] == "scan":
        h = open(a[1]).read(); t = re.search(r"<h1>(.*?)</h1>", h) or re.search(r"<title>(.*?)</title>", h)
        title = strip_html(t.group(1)) if t else ""
        fs = scan(title, "", h, None, None, a[2] if len(a) > 2 else "zz-scan/", "file")
        sha = content_sha(title, "", h)
        st, _ = decide(fs, sha)
        print(json.dumps({"status": st, "sha256": sha, "findings": fs}, indent=1))
        sys.exit(0 if st in ("pass", "approved", "cleared") else 3)
    print(__doc__); sys.exit(2)
