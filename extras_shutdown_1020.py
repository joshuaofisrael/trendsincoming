# --- Lean-in 2026-10-20 (GSC top page): government funding deadline Dec 11. New subtopic, expanded blog, homepage pick, hub links. exec'd from build.py after extras_daily_1020.py ---
SHUTP="politics/government-shutdown-deadline-2026/"
SHUTB="blog/government-funding-deadline-oct-31/"
SHUT_SRC=[("Congress.gov: H.R. 6500 (Public Law 119-103)","https://www.congress.gov/bill/119th-congress/house-bill/6500"),
("CBS News: Congress passes funding bill to avoid October shutdown","https://www.cbsnews.com/news/house-vote-government-shutdown-funding-bill/"),
("NPR: Congress averts a shutdown ahead of midterms (Sept 1)","https://www.npr.org/2026/09/01/nx-s1-5951536/house-government-funding-vote-midterms"),
("WilmerHale: Congress's postelection agenda (Oct 14)","https://www.wilmerhale.com/en/insights/client-alerts/20261013-lame-duck-high-stakes-congresss-postelection-agenda"),
("Holland & Knight: year-end deadlines (Oct 9)","https://www.hklaw.com/en/insights/publications/2026/10/beyond-the-midterms-congress-faces-converging-year-end-deadlines"),
("SSA: what a shutdown means for you","https://www.ssa.gov/blog/en/posts/2025-10-01.html"),
("USPS: how the Postal Service is funded","https://about.usps.com/who/profile/"),
("Interior Department: shutdown contingency plans (incl. NPS)","https://www.doi.gov/shutdown"),
("OPM: furlough guidance","https://www.opm.gov/policy-data-oversight/pay-leave/furlough-guidance/")]
SHUT_FAQ=[("Is there a government shutdown in October 2026?","No. The Continuing Appropriations and Extensions Act, 2027 (H.R. 6500, Public Law 119-103), signed September 2, 2026, funds federal agencies through December 11, 2026. There is no October deadline."),
("Is there a government shutdown on October 31, 2026?","No. Some posts pointed to an October 31 deadline, but the law on Congress.gov funds the government through December 11, 2026."),
("When is the next government funding deadline?","Friday, December 11, 2026. If no new funding law is enacted by the end of that day, agencies without appropriations would start shutting down on Saturday, December 12."),
("Could there be a government shutdown in December 2026?","It is possible, not certain. By December 11, Congress could pass full-year funding, another short-term extension into 2027, or a mix of the two. A shutdown happens only if no funding law is enacted in time."),
("Will Social Security payments stop in a government shutdown?","No. The Social Security Administration says Social Security and SSI payments continue on their normal dates during a shutdown. Local offices stay open with reduced services, and some requests, like proof of benefits letters, wait until it ends."),
("Does the mail still come during a government shutdown?","Yes. The Postal Service generally receives no tax dollars for operating expenses and pays its way through postage and services, so mail delivery continues."),
("Are national parks open during a government shutdown?","It depends on the National Park Service contingency plan in effect. In past shutdowns, some parks stayed accessible with limited or no visitor services, while staffed facilities such as visitor centers closed. Check nps.gov and the Interior Department's shutdown page before you go."),
("What happens to federal workers in a shutdown?","Employees whose work is not excepted are furloughed. Excepted employees, such as those protecting life and property, keep working. OPM's furlough guidance has the details.")]
SHUT_DATES=[("Sep 2, 2026","H.R. 6500 signed into law (Public Law 119-103)"),("Oct 1, 2026","Fiscal year 2027 began, funded by the stopgap"),("Tue Nov 3, 2026","Midterm elections"),("November to December","Lame-duck session: funding, defense bill, extensions"),("Fri Dec 11, 2026","Stopgap funding expires at the end of the day"),("Sat Dec 12, 2026","First day a lapse could start if nothing passes"),("Dec 31, 2026","Export-Import Bank, TANF and Community Health Center Fund deadlines"),("Jan 3, 2027","New Congress convenes")]
def _dtable(r): return "<table><tr><th>Date</th><th>What happens</th></tr>"+"".join(f"<tr><td>{esc(a)}</td><td>{esc(b)}</td></tr>" for a,b in SHUT_DATES)+"</table>"
SUBS.append(("politics","government-shutdown-deadline-2026","Government shutdown deadline 2026","There is no government shutdown in October 2026. Federal funding runs through Friday, Dec 11, 2026 under H.R. 6500, so the next possible shutdown date is Dec 12, in the lame-duck session after the Nov 3 midterms. Key dates, Congress's options and what a shutdown would mean for you. Strictly nonpartisan.",["Shutdown","shutdown","funding deadline"],SHUT_SRC[:5]))
STITLE["government-shutdown-deadline-2026"]="Government shutdown deadline 2026: Dec 11 funding date, key dates and FAQ"
SDESC["government-shutdown-deadline-2026"]="No shutdown in October 2026. Federal funding runs through Fri, Dec 11, 2026 (H.R. 6500). Key dates, what Congress could do and what a shutdown means for Social Security, mail and parks."
SUBDEEP["government-shutdown-deadline-2026"]=dict(intro="<b>The current government funding deadline is Friday, December 11, 2026.</b> There is no shutdown in October. The stopgap law Congress passed, H.R. 6500 (Public Law 119-103), signed September 2, funds federal agencies through December 11, per Congress.gov. If no new funding law is enacted by then, a lapse could begin Saturday, December 12.",
facts=[("Current deadline","Fri Dec 11, 2026"),("Funding law","Continuing Appropriations and Extensions Act, 2027 (H.R. 6500)"),("Public law","119-103, signed Sep 2, 2026"),("Shutdown in October 2026?","No"),("Earliest possible lapse","Sat Dec 12, 2026"),("Midterms","Tue Nov 3, 2026"),("Last checked","Oct 20, 2026, against Congress.gov")],
body=f'''<h2>Key dates</h2>{_dtable(0)}<h2>What could happen by December 11</h2><ul><li><b>Full-year funding:</b> Congress passes some or all of the 12 fiscal 2027 appropriations bills, as one big omnibus or several smaller packages.</li><li><b>Another stopgap:</b> a new continuing resolution pushes the deadline into 2027, when the new Congress is seated.</li><li><b>A mix:</b> some full-year bills plus a stopgap for the rest.</li><li><b>A lapse:</b> if nothing is enacted in time, agencies without approved funding pause work that is not excepted.</li></ul><p>WilmerHale's October 14 analysis says the election results will shape the choice: Republicans may want to lock in a deal before January, while Democrats may prefer to wait if they win control of a chamber. Holland &amp; Knight noted on October 9 that the House had passed 3 of the 12 bills and the Senate none before the recess. We link analysis from across the spectrum and don't take a side.</p>
<h2>What a shutdown would mean for you</h2><table><tr><th>Social Security and SSI</th><td>Payments continue on normal dates, per SSA</td></tr><tr><th>Mail</th><td>Delivery continues; USPS funds itself through postage</td></tr><tr><th>National parks</th><td>Depends on the NPS contingency plan; in past shutdowns some stayed open with few or no services</td></tr><tr><th>Federal workers</th><td>Non-excepted staff are furloughed; excepted staff keep working (OPM guidance)</td></tr></table>
<p>The full story, including our October 17 correction of an earlier Oct 31 date, is in our explainer: <a href="{R2}{SHUTB}">Is there a government shutdown in October 2026?</a> For the rest of the lame-duck to-do list, see our <a href="../congress/">Congress page</a>, and for the election that comes first, <a href="../elections-2026/">Elections 2026</a> and <a href="../early-voting-2026/">early voting dates</a>.</p>''',
faq=SHUT_FAQ)
# Congress subtopic links to the new page
SUBDEEP["congress"]["body"]=SUBDEEP["congress"]["body"].replace("<p>Full story:",f'<p>Key dates and a shutdown FAQ: <a href="../government-shutdown-deadline-2026/">government shutdown deadline 2026</a>.</p><p>Full story:')
# Trend card: answer-first, guide link, homepage pick, countdown
for _i,_t in enumerate(T):
    if _t[1]=="Shutdown watch: the real deadline is Dec 11":
        T[_i]=(_t[0],_t[1],"No shutdown in October. The stopgap law signed Sept 2 (H.R. 6500) funds the government through Friday, Dec 11, 2026, so the next deadline lands in the lame-duck session after the Nov 3 election. Key dates and what a shutdown would mean for Social Security, mail and parks.","Dec 11",_t[4],_t[5],SHUTP,1)
CD["Shutdown watch: the real deadline is Dec 11"]="2026-12-11T23:59:00-05:00"
# Hub callouts (news + politics)
HUBX={c:'<p class="warn">🏛️ <b>Shutdown watch:</b> no shutdown in October. Federal funding runs through <b>Fri, Dec 11, 2026</b>. <a href="{r}'+SHUTP+'">Key dates and FAQ →</a> · <a href="{r}'+SHUTB+'">The explainer →</a></p>' for c in ("news","politics")}
# Blog: answer-first, key dates, what happens next, FAQ, sources. Same URL.
for _i,_p in enumerate(POSTS):
    if _p[0]=="government-funding-deadline-oct-31":
        _b=_p[8]
        _ans='<p><b>Short answer: there is no government shutdown in October 2026. The current government funding deadline is Friday, December 11, 2026.</b> The stopgap law H.R. 6500 (Public Law 119-103), signed September 2, funds federal agencies through that date, per Congress.gov (checked October 20, 2026). If Congress enacts no new funding by the end of December 11, a shutdown could start Saturday, December 12.</p>\n'
        _b=_ans+_b
        _b=re.sub(r"<p>Short version: .*?</p>\n",'<p>The next real fight over government funding happens after the November 3 election, in the lame-duck session. Here is a calm, nonpartisan rundown of where things stand, the dates to know and what a shutdown would mean for you. Want just the dates? See our <a href="/'+SHUTP+'">government shutdown deadline 2026</a> page.</p>\n',_b,flags=re.S)
        _new=f'''<h2>What happens next: key dates</h2>{_dtable(0)}
<ul><li><b>Before Nov 3:</b> Congress is out campaigning, so no funding votes are expected before the election.</li>
<li><b>Lame duck:</b> lawmakers return with a short calendar. Besides funding, WilmerHale and Holland &amp; Knight list the annual defense bill, surface transportation and other extensions that also expire Dec 11, the Farm Bill and a water resources bill.</li>
<li><b>By Dec 11:</b> Congress passes full-year funding, another stopgap into 2027, or a mix. If none is enacted, a lapse begins Dec 12 for agencies without funding.</li>
<li><b>How the election matters:</b> WilmerHale's Oct 14 analysis says Republicans may want to lock in a deal before the new Congress, while Democrats may prefer to wait if they win control of a chamber. See our neutral <a href="/politics/elections-2026/">Elections 2026 hub</a> and <a href="/blog/midterms-2026-explained/">midterms explainer</a>.</li></ul>
<h2>What a shutdown would mean for you</h2>
<ul><li><b>Social Security and SSI:</b> payments continue on their normal dates, the Social Security Administration says. Local offices stay open with reduced services.</li>
<li><b>Mail:</b> keeps coming. The Postal Service generally receives no tax dollars for operating expenses and funds itself through postage and services.</li>
<li><b>National parks:</b> depends on the National Park Service contingency plan. In past shutdowns, some parks stayed accessible with limited or no services while visitor centers closed. Check nps.gov before a trip.</li>
<li><b>Federal workers:</b> employees whose work is not excepted are furloughed; excepted employees keep working, per OPM guidance.</li></ul>
<p>We keep the <a href="/{SHUTP}">shutdown deadline page</a> and the <a href="/politics/congress/">Congress hub</a> updated as this moves.</p>
'''
        _b=re.sub(r"<h2>What's next</h2>.*?(?=<h2>Where to follow it</h2>)",lambda m:_new,_b,flags=re.S)
        assert "What happens next: key dates" in _b and "Short answer" in _b
        _src=list(_p[7])+[s for s in SHUT_SRC if s[1] not in [x[1] for x in _p[7]]]
        POSTS[_i]=(_p[0],"Is there a government shutdown in October 2026? No. The deadline is Dec 11","No shutdown in October 2026. Federal funding runs through Fri, Dec 11, 2026 under H.R. 6500. Key dates, what could happen in December, and what a shutdown means for Social Security, mail and parks.",_p[3],_p[4],_p[5],_p[6],_src,_b)
FAQ["government-funding-deadline-oct-31"]=SHUT_FAQ
