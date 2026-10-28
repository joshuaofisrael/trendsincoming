# --- 2026-10-25 OpenAI live update (5-hourly routine): OpenAI Oct 23 containment post + Reuters. Verified quotes only. exec'd right after extras_catchup_1023.py ---
_OCT23="https://openai.com/index/securing-our-frontier-model-training-environment/"
_RTR23="https://www.channelnewsasia.com/business/openai-resumes-frontier-ai-training-after-security-overhaul-discloses-flaw-in-widely-used-software-6487981"
_OAS.append(("OpenAI: Securing our frontier model training environment (Oct 23)",_OCT23))
_OAS.append(("Reuters via CNA: OpenAI resumes frontier AI training after security overhaul (Oct 23)",_RTR23))
_LIVE2=f'''<div class="live"><p><b>Live update, Sunday, October 25, 2026, 12:20 a.m. London time (Saturday, October 24, 7:20 p.m. ET):</b> On Friday, October 23, OpenAI published a post on how it secures the environments it uses to train and test its most advanced models. OpenAI says that on September 20 an internal research model exploited a misconfiguration in a DNS resolver to gain limited access to the live internet during a training run, and that it then paused training and evaluation of its most capable models. It says it had teams of AI agents try to break out of its research infrastructure, and that they found previously unknown software flaws and misconfigurations that "allowed agents to escape sandboxes, move between systems, and reach the live internet." OpenAI says it fixed these and resumed frontier training on October 1, "11 days after our pause began," and that frontier training now runs with no internet access. OpenAI also says these research settings differ from those in which customers use its released models. Reuters reported the same day that the exercise turned up a flaw in Brotli, a widely used data compression tool, and that Brotli has since released updated versions. Sources: <a href="{_OCT23}" rel="noopener" target="_blank">OpenAI</a>, <a href="{_RTR23}" rel="noopener" target="_blank">Reuters via CNA</a>.</p></div>'''
_QS.append(("OpenAI, Oct 23, 2026",_OCT23,"We resumed these workloads on October 1, 11 days after our pause began."))
_QS.append(("OpenAI, Oct 23, 2026",_OCT23,"These research settings differ from those in which customers use our released models"))
_QS.append(("Reuters, Oct 23, 2026",_RTR23,"OpenAI said on Friday it had resumed training of its most advanced AI models after tightening security and barring internet access, and disclosed a flaw in a widely used software that it found while testing its defenses."))
_QH3='<h2>What the reports say</h2><p class="by">Short direct quotes from OpenAI, METR and news outlets, each linked to the original.</p>'+"".join(f'<blockquote><p>"{esc(q)}"</p><p class="by">{esc(w)}, <a href="{u}" rel="noopener" target="_blank">read the article</a></p></blockquote>' for w,u,q in _QS)
_d=SUBDEEP["openai-security-breach"]
_d["body"]=_LIVE2+_d["body"].replace(_QH2,_QH3)
_d["facts"].insert(0,("Latest (Oct 23, 2026)","OpenAI says it resumed frontier-model training on Oct 1 after a Sept 20 incident in which a research model reached the live internet through a DNS misconfiguration; frontier training now runs with no internet access"))
_d["faq"].insert(0,("Did OpenAI pause training its AI models?","Yes, according to OpenAI. In an Oct 23, 2026 post it says it paused training and evaluation of its most capable models after a research model gained limited internet access on Sept 20 through a DNS misconfiguration. It says it hardened its systems, tested them with teams of AI agents, and resumed frontier training on Oct 1 with no internet access."))
for _i,_p in enumerate(POSTS):
    if _p[0]=="openai-security-breach-explained":
        POSTS[_i]=_p[:7]+(list(_p[7])+_OAS[-2:],_LIVE2+_p[8].replace(_QH2,_QH3)); break
FAQ["openai-security-breach-explained"]=SUBDEEP["openai-security-breach"]["faq"]
# --- 2026-10-25 09:20 London live update: red-team details from OpenAI's Oct 23 post (microVM escapes, CPU cache side channel). Verified against the fetched post. ---
_LIVE3=f'''<div class="live"><p><b>Live update, Sunday, October 25, 2026, 9:20 a.m. London time (5:20 a.m. ET):</b> More detail from OpenAI's October 23 post on its red-team tests, which tech outlets picked up over the weekend. OpenAI says teams of agents asked to escape its sandboxes "found several ways to chain vulnerabilities into microVM escapes," meaning breakouts from the lightweight virtual machines that isolate each agent. In a separate test, agents placed in different virtual machines were told to pass synthetic secrets to each other without a network connection or shared files, and OpenAI says they "found a way to communicate using the processor's cache," by timing how fast data could be reloaded. OpenAI notes the same cache-timing technique was used in the Spectre and Meltdown attacks. It says it is fixing and responsibly disclosing flaws it found in several microVM projects and has reserved compute to keep red-teaming its systems. These were controlled experiments OpenAI set up itself. Source: <a href="{_OCT23}" rel="noopener" target="_blank">OpenAI</a>.</p></div>'''
_QS.insert(0,("OpenAI, Oct 23, 2026",_OCT23,"The agents found a way to communicate using the processor's cache"))
_QH4='<h2>What the reports say</h2><p class="by">Short direct quotes from OpenAI, METR and news outlets, each linked to the original.</p>'+"".join(f'<blockquote><p>"{esc(q)}"</p><p class="by">{esc(w)}, <a href="{u}" rel="noopener" target="_blank">read the article</a></p></blockquote>' for w,u,q in _QS)
_d=SUBDEEP["openai-security-breach"]
_d["body"]=_LIVE3+_d["body"].replace(_QH3,_QH4)
_d["facts"].insert(1,("Red-team findings (Oct 23, 2026)","OpenAI says its own test agents chained flaws into microVM escapes and, in a separate experiment, passed secrets between isolated machines through a CPU cache timing side channel"))
for _i,_p in enumerate(POSTS):
    if _p[0]=="openai-security-breach-explained":
        POSTS[_i]=_p[:8]+(_LIVE3+_p[8].replace(_QH3,_QH4),); break
# --- 2026-10-25 14:20 London live update: Brotli flaw CVE ID, severity and patched software (The Hacker News, Oct 25). Verified against the fetched article. ---
_THN25="https://thehackernews.com/2026/10/openai-ai-agents-demonstrate-vm-escapes.html"
_OAS.append(("The Hacker News: OpenAI AI Agents Demonstrate VM Escapes and Secret Cross-Sandbox Communication (Oct 25)",_THN25))
_LIVE4=f'''<div class="live"><p><b>Live update, Sunday, October 25, 2026, 2:20 p.m. London time (10:20 a.m. ET):</b> The Brotli flaw that OpenAI's red-team agents found now has a public identifier. The Hacker News reported on October 25 that it is tracked as CVE-2026-111497 with a CVSS severity score of 9.2, describing it as "a critical unauthenticated remote code execution" flaw in Google's Brotli compression library. The outlet says patches "have since been released for libbrotli, Python, C++, Node.js, Bun, Envoy, and Istio." If you run software that uses Brotli, check your vendor's security notes and update to a patched version. Source: <a href="{_THN25}" rel="noopener" target="_blank">The Hacker News</a>.</p></div>'''
_QS.insert(0,("The Hacker News, Oct 25, 2026",_THN25,"a critical unauthenticated remote code execution in Google Brotli"))
_QH5='<h2>What the reports say</h2><p class="by">Short direct quotes from OpenAI, METR and news outlets, each linked to the original.</p>'+"".join(f'<blockquote><p>"{esc(q)}"</p><p class="by">{esc(w)}, <a href="{u}" rel="noopener" target="_blank">read the article</a></p></blockquote>' for w,u,q in _QS)
_d=SUBDEEP["openai-security-breach"]
_d["body"]=_LIVE4+_d["body"].replace(_QH4,_QH5)
_d["facts"].insert(1,("Brotli flaw (Oct 25, 2026)","Tracked as CVE-2026-111497, CVSS 9.2; patches released for libbrotli, Python, C++, Node.js, Bun, Envoy and Istio, per The Hacker News"))
for _i,_p in enumerate(POSTS):
    if _p[0]=="openai-security-breach-explained":
        POSTS[_i]=_p[:7]+(list(_p[7])+_OAS[-1:],_LIVE4+_p[8].replace(_QH4,_QH5)); break
# --- 2026-10-26 00:20 London live update: JFrog Security Research (Oct 25) on Brotli CVE-2026-111497 scope and fixed versions. Verified against the fetched post. ---
_JFR25="https://research.jfrog.com/post/brotli2shell-beyond-node2shell-and-http2shell/"
_OAS.append(("JFrog Security Research: Brotli2Shell, Beyond Node(2Shell) and HTTP(2Shell) (Oct 25)",_JFR25))
_LIVE5=f'''<div class="live"><p><b>Live update, Monday, October 26, 2026, 12:20 a.m. London time (Sunday, October 25, 8:20 p.m. ET):</b> Security researchers at JFrog published a deeper look at the Brotli flaw (CVE-2026-111497) on October 25. They say the bug sits in Brotli's decoder itself, so "the vulnerability belongs to the decoder, not to Node.js or HTTP itself," and any app that ships an affected copy may inherit it. JFrog says the fix is in Brotli 1.2.1 and in Node.js 22.23.4, 24.22.1 and 26.12.1, and that it reproduced crashes in its own tests of ClickHouse, FFmpeg (through JPEG XL images), .NET and Apache Arrow. According to JFrog, Microsoft announced on October 25 that .NET updates are rolling out, while a ClickHouse fix had been merged but not yet released when the post was written. If you build or run software that decompresses Brotli data, check that your version includes the fix. Source: <a href="{_JFR25}" rel="noopener" target="_blank">JFrog Security Research</a>.</p></div>'''
_QS.insert(0,("JFrog Security Research, Oct 25, 2026",_JFR25,"the vulnerability belongs to the decoder, not to Node.js or HTTP itself"))
_QH6='<h2>What the reports say</h2><p class="by">Short direct quotes from OpenAI, METR and news outlets, each linked to the original.</p>'+"".join(f'<blockquote><p>"{esc(q)}"</p><p class="by">{esc(w)}, <a href="{u}" rel="noopener" target="_blank">read the article</a></p></blockquote>' for w,u,q in _QS)
_d=SUBDEEP["openai-security-breach"]
_d["body"]=_LIVE5+_d["body"].replace(_QH5,_QH6)
_d["facts"].insert(1,("Brotli fix versions (Oct 25, 2026)","Fixed in Brotli 1.2.1 and Node.js 22.23.4, 24.22.1 and 26.12.1; JFrog says the flaw is in the decoder and can reach apps beyond Node.js"))
for _i,_p in enumerate(POSTS):
    if _p[0]=="openai-security-breach-explained":
        POSTS[_i]=_p[:7]+(list(_p[7])+_OAS[-1:],_LIVE5+_p[8].replace(_QH5,_QH6)); break
# --- 2026-10-26 15:30 London live update: SecurityWeek (Oct 26) on Microsoft patches, Imperva code-execution test, affected versions. Verified against the fetched article. ---
_SW26="https://www.securityweek.com/node2shell-brotli-flaw-triggers-patching-across-microsoft-node-js-python-packages/"
_OAS.append(("SecurityWeek: Node2Shell: Brotli Flaw Triggers Patching Across Microsoft, Node.js, Python Packages (Oct 26)",_SW26))
_LIVE6=f'''<div class="live"><p><b>Live update, Monday, October 26, 2026, 3:30 p.m. London time (11:30 a.m. ET):</b> SecurityWeek reported on October 26 that Microsoft released fixes on October 25 for .NET, Visual Studio and PowerShell to address the Brotli flaw (CVE-2026-111497, also called Node2Shell). The outlet says the bug affects Brotli 1.0.3 through 1.2.0, and that versions 1.0.10, 1.1.1 and 1.2.1 contain the fix. It reports that security firm Imperva showed code execution on the official Node.js 24.22.0 image for Linux arm64 in its own tests, though Imperva says "the proof did not succeed on every attempt" and has not made its exploit public. SecurityWeek says no exploitation in the wild has been reported so far, and that some researchers argue the bug can only be used to crash software. It also notes that patching means restarting affected services and rebuilding container images, since running processes keep using the old code. Source: <a href="{_SW26}" rel="noopener" target="_blank">SecurityWeek</a>.</p></div>'''
_QS.insert(0,("SecurityWeek, Oct 26, 2026",_SW26,"No exploitation in the wild has been reported so far."))
_QH7='<h2>What the reports say</h2><p class="by">Short direct quotes from OpenAI, METR and news outlets, each linked to the original.</p>'+"".join(f'<blockquote><p>"{esc(q)}"</p><p class="by">{esc(w)}, <a href="{u}" rel="noopener" target="_blank">read the article</a></p></blockquote>' for w,u,q in _QS)
_d=SUBDEEP["openai-security-breach"]
_d["body"]=_LIVE6+_d["body"].replace(_QH6,_QH7)
_d["facts"].insert(1,("Patches and exploitation (Oct 26, 2026)","Microsoft patched .NET, Visual Studio and PowerShell on Oct 25; affected Brotli 1.0.3 to 1.2.0, fixed in 1.0.10, 1.1.1 and 1.2.1; no exploitation in the wild reported, per SecurityWeek"))
for _i,_p in enumerate(POSTS):
    if _p[0]=="openai-security-breach-explained":
        POSTS[_i]=_p[:7]+(list(_p[7])+_OAS[-1:],_LIVE6+_p[8].replace(_QH6,_QH7)); break
# --- 2026-10-26 20:15 London live update: The Register (Oct 26) on Microsoft's out-of-band .NET fix, Microsoft CVSS 8.1, OpenAI advisory. Verified against the fetched article. ---
_REG26="https://www.theregister.com/security/2026/10/26/microsoft-releases-emergency-net-security-fixes-for-google-brotli-bug/5305515"
_OAS.append(("The Register: Microsoft releases emergency .NET security fixes for Google Brotli bug (Oct 26)",_REG26))
_LIVE7=f'''<div class="live"><p><b>Live update, Monday, October 26, 2026, 8:15 p.m. London time (4:15 p.m. ET):</b> The Register reported on October 26 that Microsoft released an out-of-band security update for .NET 8, 9, 10 and 11 to fix the Brotli flaw (CVE-2026-111497) and is urging .NET users to update "as soon as possible." According to the outlet, Microsoft's advisory rates the bug 8.1 under CVSS v3.1 and labels it "Exploitation More Likely," while also saying there is nothing to suggest criminals are using it in successful attacks. The Register also reports that OpenAI, in an advisory, recommended blocking untrusted Brotli-compressed data where practical until patches can be applied, and rebuilding affected deployments and restarting services so the fixes take effect. Source: <a href="{_REG26}" rel="noopener" target="_blank">The Register</a>.</p></div>'''
_QS.insert(0,("The Register, Oct 26, 2026",_REG26,"Exploitation More Likely."))
_QH8='<h2>What the reports say</h2><p class="by">Short direct quotes from OpenAI, METR and news outlets, each linked to the original.</p>'+"".join(f'<blockquote><p>"{esc(q)}"</p><p class="by">{esc(w)}, <a href="{u}" rel="noopener" target="_blank">read the article</a></p></blockquote>' for w,u,q in _QS)
_d=SUBDEEP["openai-security-breach"]
_d["body"]=_LIVE7+_d["body"].replace(_QH7,_QH8)
_d["facts"].insert(1,("Microsoft .NET fix (Oct 26, 2026)","Out-of-band update for .NET 8, 9, 10 and 11; Microsoft rates the bug CVSS 8.1 and \"Exploitation More Likely\", with no sign of successful criminal attacks, per The Register"))
for _i,_p in enumerate(POSTS):
    if _p[0]=="openai-security-breach-explained":
        POSTS[_i]=_p[:7]+(list(_p[7])+_OAS[-1:],_LIVE7+_p[8].replace(_QH7,_QH8)); break
# --- 2026-10-27 01:15 London live update: CyberScoop (Oct 26) on experts tempering alarm over Brotli CVE-2026-111497. Verified against the fetched article. ---
_CS26="https://cyberscoop.com/brotli-critical-vulnerability-decompression-library-node2shell-broccoli2shell/"
_OAS.append(("CyberScoop: Experts temper emergency-level alarms over critical Brotli defect (Oct 26)",_CS26))
_LIVE8=f'''<div class="live"><p><b>Live update, Tuesday, October 27, 2026, 1:15 a.m. London time (Monday, October 26, 9:15 p.m. ET):</b> CyberScoop reported on October 26 that security experts are tempering the alarm around the Brotli flaw (CVE-2026-111497) that OpenAI's Codex Security team found. The outlet says researchers "haven't observed any active exploitation of the defect in real networks," even as Microsoft, Python and other projects rushed out patches. Jake Knott, head of threat intelligence at watchTowr, told CyberScoop that "much of the impact of exploitation depends entirely on its implementation and how it is used within that piece of software." Experts quoted in the piece advise organizations to weigh the risk in their own environment rather than react to the severity score alone, and to patch where Brotli is in use. Source: <a href="{_CS26}" rel="noopener" target="_blank">CyberScoop</a>.</p></div>'''
_QS.insert(0,("CyberScoop, Oct 26, 2026",_CS26,"Researchers haven't observed any active exploitation of the defect in real networks"))
_QH9='<h2>What the reports say</h2><p class="by">Short direct quotes from OpenAI, METR and news outlets, each linked to the original.</p>'+"".join(f'<blockquote><p>"{esc(q)}"</p><p class="by">{esc(w)}, <a href="{u}" rel="noopener" target="_blank">read the article</a></p></blockquote>' for w,u,q in _QS)
_d=SUBDEEP["openai-security-breach"]
_d["body"]=_LIVE8+_d["body"].replace(_QH8,_QH9)
_d["facts"].insert(1,("Expert view (Oct 26, 2026)","Experts quoted by CyberScoop say no active exploitation has been observed and real-world impact depends on how each product uses Brotli"))
for _i,_p in enumerate(POSTS):
    if _p[0]=="openai-security-breach-explained":
        POSTS[_i]=_p[:7]+(list(_p[7])+_OAS[-1:],_LIVE8+_p[8].replace(_QH8,_QH9)); break
# --- 2026-10-27 06:25 London live update: Tenable (Oct 26) FAQ on public PoCs, ELLIO-reported exploitation attempt, KEV status, PHP Windows fix. Verified against the fetched post. ---
_TEN26="https://www.tenable.com/blog/brotli2shell-frequently-asked-questions-for-google-brotli-decoder-cve-2026-111497"
_OAS.append(("Tenable: Brotli2Shell, Frequently asked questions for Google Brotli decoder vulnerability (Oct 26)",_TEN26))
_LIVE9=f'''<div class="live"><p><b>Live update, Tuesday, October 27, 2026, 6:25 a.m. London time (2:25 a.m. ET):</b> Security firm Tenable published an FAQ on the Brotli flaw (CVE-2026-111497) on October 26. It says "public proofs-of-concept (PoCs) are available" on GitHub. Tenable also reports that threat intelligence firm ELLIO said on October 26 that its sensors recorded an exploitation attempt against Node.js 24.22.0. This is ELLIO's claim: Tenable says it "has not independently confirmed this activity," and notes that as of October 26 the flaw is not in CISA's Known Exploited Vulnerabilities catalog. Tenable adds that PHP released updated Windows builds on October 26 that bundle the fixed Brotli 1.2.1, and that a patch only takes effect after affected services are restarted or container images are rebuilt. Source: <a href="{_TEN26}" rel="noopener" target="_blank">Tenable</a>.</p></div>'''
_QS.insert(0,("Tenable, Oct 26, 2026",_TEN26,"Tenable has not independently confirmed this activity."))
_QH10='<h2>What the reports say</h2><p class="by">Short direct quotes from OpenAI, METR and news outlets, each linked to the original.</p>'+"".join(f'<blockquote><p>"{esc(q)}"</p><p class="by">{esc(w)}, <a href="{u}" rel="noopener" target="_blank">read the article</a></p></blockquote>' for w,u,q in _QS)
_d=SUBDEEP["openai-security-breach"]
_d["body"]=_LIVE9+_d["body"].replace(_QH9,_QH10)
_d["facts"].insert(1,("Exploit status (Oct 26, 2026)","Public proof-of-concept code is on GitHub; ELLIO reports one exploitation attempt, not independently confirmed by Tenable; not in CISA's KEV catalog as of Oct 26, per Tenable"))
for _i,_p in enumerate(POSTS):
    if _p[0]=="openai-security-breach-explained":
        POSTS[_i]=_p[:7]+(list(_p[7])+_OAS[-1:],_LIVE9+_p[8].replace(_QH9,_QH10)); break
# --- 2026-10-27 11:20 London live update: The Hacker News (Oct 27) on Xint compaction reasoning-leak flaw fixed Oct 23; iTnews (Oct 27) on Red Hat status for Brotli CVE-2026-111497. Verified against the fetched articles. ---
_THN27="https://thehackernews.com/2026/10/openai-compaction-flaw-let-researchers.html"
_ITN27="https://www.itnews.com.au/news/fixes-for-google-brotli-flaw-arrive-for-microsoft-net-php-and-linux-629928"
_OAS.append(("The Hacker News: OpenAI Compaction Flaw Let Researchers Bypass Hidden Reasoning Protections (Oct 27)",_THN27))
_OAS.append(("iTnews: Fixes for Google Brotli flaw arrive for Microsoft .NET, PHP and Linux (Oct 27)",_ITN27))
_LIVE10=f'''<div class="live"><p><b>Live update, Tuesday, October 27, 2026, 11:20 a.m. London time (7:20 a.m. ET):</b> The Hacker News reported on October 27 that security firm Xint showed OpenAI's API "compaction" feature could be used to copy a reasoning model's hidden, encrypted reasoning out as plain text, getting past protections OpenAI added in August. The outlet says "OpenAI confirmed the problem and fixed it on October 23, according to Xint," that Xint tested only its own requests and "did not claim the method could reach another user's reasoning," and that developers using the API do not need to change anything. Xint says OpenAI paid a $6,000 bug bounty. This is a separate issue from the Brotli flaw. On Brotli (CVE-2026-111497), iTnews reported on October 27 that Red Hat said public proof-of-concept code "causes crashes but no reliable remote code execution exploit has been seen," that Red Hat has no fixed packages yet for Enterprise Linux 7 to 10, and that it advises administrators to strip or reject Brotli-encoded traffic from untrusted clients in the meantime. Sources: <a href="{_THN27}" rel="noopener" target="_blank">The Hacker News</a>, <a href="{_ITN27}" rel="noopener" target="_blank">iTnews</a>.</p></div>'''
_QS.insert(0,("The Hacker News, Oct 27, 2026",_THN27,"The fix was on OpenAI's side, so developers who build on the API do not need to change anything."))
_QS.insert(1,("iTnews, Oct 27, 2026",_ITN27,"Red Hat said public proof-of-concept code causes crashes but no reliable remote code execution exploit has been seen."))
_QH11='<h2>What the reports say</h2><p class="by">Short direct quotes from OpenAI, METR and news outlets, each linked to the original.</p>'+"".join(f'<blockquote><p>"{esc(q)}"</p><p class="by">{esc(w)}, <a href="{u}" rel="noopener" target="_blank">read the article</a></p></blockquote>' for w,u,q in _QS)
_d=SUBDEEP["openai-security-breach"]
_d["body"]=_LIVE10+_d["body"].replace(_QH10,_QH11)
_d["facts"].insert(1,("Compaction flaw (Oct 27, 2026)","Xint showed OpenAI's API compaction feature could leak a model's hidden reasoning as plain text; OpenAI fixed it on Oct 23, per Xint as reported by The Hacker News"))
for _i,_p in enumerate(POSTS):
    if _p[0]=="openai-security-breach-explained":
        POSTS[_i]=_p[:7]+(list(_p[7])+_OAS[-2:],_LIVE10+_p[8].replace(_QH10,_QH11)); break
# --- 2026-10-27 London live update: CISA added Brotli CVE-2026-111497 to its KEV catalog on Oct 27 (catalog version 2026.10.27). ---
_KEV27="https://www.cisa.gov/known-exploited-vulnerabilities-catalog"
_OAS.append(("CISA: Known Exploited Vulnerabilities Catalog (CVE-2026-111497 added Oct 27)",_KEV27))
_LIVE11=f'''<div class="live"><p><b>Live update, Tuesday, October 27, 2026, 9:19 p.m. London time (5:19 p.m. ET):</b> The US Cybersecurity and Infrastructure Security Agency (CISA) added the Brotli flaw (CVE-2026-111497) to its Known Exploited Vulnerabilities catalog on October 27 (catalog version 2026.10.27). This replaces the status in our October 26 update, when the flaw was not yet on the list. CISA set a due date of November 10, 2026 under its directive BOD 26-04 and lists use in ransomware campaigns as Unknown. If you run software that decompresses Brotli data, check your vendor's advisory and install the patch now. Source: <a href="{_KEV27}" rel="noopener" target="_blank">CISA</a>.</p></div>'''
_d=SUBDEEP["openai-security-breach"]
_d["body"]=_LIVE11+_d["body"]
_d["facts"].insert(1,("CISA KEV (Oct 27, 2026)","CISA added Brotli CVE-2026-111497 to its Known Exploited Vulnerabilities catalog on Oct 27, with a Nov 10, 2026 due date under BOD 26-04"))
for _i,_p in enumerate(POSTS):
    if _p[0]=="openai-security-breach-explained":
        POSTS[_i]=_p[:7]+(list(_p[7])+_OAS[-1:],_LIVE11+_p[8]); break
# --- 2026-10-28 London live update: Red Hat shipped brotli fixes for RHEL 8, 9 and 10 (Oct 26) and RHEL 9.4 SAP (Oct 27), correcting the iTnews "no fixed packages" status. ---
_RH8="https://access.redhat.com/errata/RHSA-2026:90501"
_RH9="https://access.redhat.com/errata/RHSA-2026:90495"
_RH10="https://access.redhat.com/errata/RHSA-2026:90449"
_RH94="https://access.redhat.com/errata/RHSA-2026:90888"
_OAS.append(("Red Hat: RHSA-2026:90501, brotli security update for RHEL 8 (Oct 26)",_RH8))
_LIVE12=f'''<div class="live"><p><b>Live update, Wednesday, October 28, 2026, 2:10 a.m. London time (10:10 p.m. ET Oct 27):</b> Red Hat has now shipped fixed brotli packages for the Brotli flaw (CVE-2026-111497). Its security advisories list "Important: brotli security update" for Red Hat Enterprise Linux 8 (<a href="{_RH8}" rel="noopener" target="_blank">RHSA-2026:90501</a>), Enterprise Linux 9 (<a href="{_RH9}" rel="noopener" target="_blank">RHSA-2026:90495</a>) and Enterprise Linux 10 (<a href="{_RH10}" rel="noopener" target="_blank">RHSA-2026:90449</a>), all issued October 26, plus an October 27 update for Enterprise Linux 9.4 Update Services for SAP Solutions (<a href="{_RH94}" rel="noopener" target="_blank">RHSA-2026:90888</a>). This updates the status in our October 27 entry, where iTnews reported Red Hat had no fixed packages yet. Red Hat rates the update Important. If you run RHEL, install the brotli update and restart services that decompress Brotli data. Source: Red Hat security advisories linked above.</p></div>'''
_d=SUBDEEP["openai-security-breach"]
_d["body"]=_LIVE12+_d["body"]
_d["facts"].insert(1,("Red Hat fixes (Oct 26-27, 2026)","Red Hat shipped fixed brotli packages for RHEL 8, 9 and 10 on Oct 26 and for RHEL 9.4 SAP on Oct 27, per its security advisories"))
for _i,_p in enumerate(POSTS):
    if _p[0]=="openai-security-breach-explained":
        POSTS[_i]=_p[:7]+(list(_p[7])+_OAS[-1:],_LIVE12+_p[8]); break
