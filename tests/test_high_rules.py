"""Proves a HIGH rule (1, 2, 6, 8) is released only by an exact-sha approval, never by a moderate
clearance or a ChatGPT SAFE. Uses a temporary content-review dir; the real approvals.jsonl is never touched."""
import os, sys, json, tempfile, importlib
tmp = tempfile.mkdtemp(prefix="lgtest-")
os.environ["LEGAL_GATE_CR"] = tmp
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import legal_gate as g; importlib.reload(g)
assert g.CR == tmp and not g.APPROVALS.startswith("/workspace/content-review")

SRC = '<a href="https://www.reuters.com/x">Reuters</a>'
TITLE = "TEST: Fictional Person"
BODY = f"<p>Former governor Testo Fakename was convicted of fraud in 2025, per {SRC}.</p>"
fs = g.scan(TITLE, "", BODY, None, None, "zz-test/", "page")
sha = g.content_sha(TITLE, "", BODY)
r1 = [x for x in fs if x["rule"] == 1]
assert r1 and all(x["severity"] == "HIGH" for x in r1), "rule 1 court finding must be HIGH"
print("1. sourced conviction sentence -> rule 1 HIGH:", [x["severity"] for x in r1])

def w(p, rec): open(p, "a").write(json.dumps(rec) + "\n")
# moderate clearance with exact sha + ChatGPT SAFE
w(g.CLEARANCES, {"site": g.SITE, "sha256": sha, "rule": [1], "chatgpt_verdict": "SAFE: test"})
w(g.CLEARANCES, {"site": g.SITE, "sha256": sha, "rule": [4], "chatgpt_verdict": "SAFE: mislabelled test"})
st, _ = g.decide(fs, sha); assert st == "hold_high", st
print("2. exact-sha ChatGPT SAFE clearance -> ", st)
# even a finding mislabelled MODERATE under a HIGH rule stays held
for rule in (1, 2, 6, 8):
    fake = [{"rule": rule, "severity": "MODERATE", "snippet": "x", "why": "t", "sent_hash": "h"}]
    st, _ = g.decide(fake, sha); assert st == "hold_high", (rule, st)
print("3. rules 1/2/6/8 mislabelled MODERATE + SAFE clearance -> hold_high for all")
gate = g.Gate(dry=True); assert not gate.check("zz-test/", TITLE, "", BODY)
print("4. Gate.check publishes it? False")
# approval of a different sha does nothing
w(g.APPROVALS, {"sha256": "0" * 64, "decision": "approved"})
st, _ = g.decide(fs, sha); assert st == "hold_high", st
print("5. approval for a different sha -> ", st)
w(g.APPROVALS, {"sha256": sha, "decision": "approved"})
st, _ = g.decide(fs, sha); assert st == "approved", st
gate = g.Gate(dry=True); assert gate.check("zz-test/", TITLE, "", BODY)
print("6. exact-sha approval in approvals.jsonl -> ", st)
# review() refuses HIGH-rule drafts
d = os.path.join(tmp, "d.json"); json.dump({"severity": "MODERATE", "findings": [{"rule": 1}]}, open(d, "w"))
assert g.review(d, "t") == 2
print("7. review command refuses a HIGH-rule draft labelled MODERATE")
# MODERATE rule still clears with SAFE
fs4 = [{"rule": 4, "severity": "MODERATE", "snippet": "x", "why": "t", "sent_hash": "h"}]
w(g.CLEARANCES, {"site": g.SITE, "sha256": "f" * 64, "rule": [4], "chatgpt_verdict": "SAFE"})
assert g.decide(fs4, "f" * 64)[0] == "cleared"
w(g.CLEARANCES, {"site": g.SITE, "revokes_sha256": "f" * 64, "status": "REVOKED"})
assert g.decide(fs4, "f" * 64)[0] == "hold_moderate"
print("8. MODERATE rule 4 clears with SAFE; a revocation line cancels it")
print("ALL HIGH-RULE TESTS PASSED")
