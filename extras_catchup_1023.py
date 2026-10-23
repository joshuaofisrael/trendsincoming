# --- 2026-10-23 catch-up (Joshua "wake now"): OpenAI live update, Macy's 100th parade hub, holiday store hours hub. exec'd last from build.py ---
# 1) OpenAI: timestamped live update (METR primary source, verified quotes only)
_MET="https://metr.org/blog/2026-10-22-red-teaming-openai-agent-monitoring/"
_OAS.append(("METR: Red-Teaming OpenAI's Internal Agent Monitoring Systems (Oct 22)",_MET))
_LIVE=f'''<div class="live"><p><b>Live update, Friday, October 23, 2026, 1:15 a.m. London time (Thursday, October 22, 8:15 p.m. ET):</b> On Thursday, October 22, the AI safety group METR published a write-up of a three-week exercise, July 21 to August 11, in which a METR employee and a Redwood Research employee stress-tested OpenAI's internal misalignment monitoring system. METR says they found "a number of novel vulnerabilities" in the system as it existed on and before July 21. METR says OpenAI has stated that all of the vulnerabilities it identified that affect OpenAI's production safeguards "have been patched", and adds: "We have not evaluated these claims." METR also notes its findings describe the historical system, not the expanded system's current coverage. Source: <a href="{_MET}" rel="noopener" target="_blank">METR</a>. Reuters and NBC News also covered the METR findings on October 22. This is separate from OpenAI's October 20 report on agents weakening monitoring. Next check: within a few hours.</p></div>'''
_QS.append(("METR, Oct 22, 2026",_MET,"The METR and Redwood employees discovered a number of novel vulnerabilities in the asynchronous internal misalignment monitoring system as it existed on and before July 21st."))
_QS.append(("METR, Oct 22, 2026",_MET,"Since completing the exercise, OpenAI has stated that all of the vulnerabilities we identified that impact their production safeguards stack have been patched."))
_QS.append(("METR, Oct 22, 2026",_MET,"We have not evaluated these claims."))
_QH2='<h2>What the reports say</h2><p class="by">Short direct quotes from OpenAI, METR and news outlets, each linked to the original.</p>'+"".join(f'<blockquote><p>"{esc(q)}"</p><p class="by">{esc(w)}, <a href="{u}" rel="noopener" target="_blank">read the article</a></p></blockquote>' for w,u,q in _QS)
_d=SUBDEEP["openai-security-breach"]
_d["body"]=_LIVE+_d["body"].replace(_QH,_QH2)
_d["facts"].insert(0,("Latest (Oct 22, 2026)","METR publishes findings from a July 21 to Aug 11 stress test of OpenAI's internal monitoring system; says OpenAI states production-safeguard issues are patched, which METR has not evaluated"))
_d["faq"].insert(0,("What did METR find about OpenAI's monitoring system?","On Oct 22, 2026, METR published a high-level write-up of a July 21 to Aug 11 exercise. It says it found \"a number of novel vulnerabilities\" in the system as it existed on and before July 21. It says OpenAI states the vulnerabilities affecting production safeguards have been patched, and that METR has not evaluated that claim."))
_p=POSTS[0]; _pb=_p[8].replace(_QH,_QH2)
POSTS[0]=_p[:7]+(list(_p[7])+[_OAS[-1]],_LIVE+_pb)
FAQ["openai-security-breach-explained"]=SUBDEEP["openai-security-breach"]["faq"]
PHCSS_LIVE='.live{border:3px solid var(--ink);border-radius:16px;background:#fff8d6;padding:4px 16px;margin:14px 0;box-shadow:4px 4px 0 var(--ink)}\n'

# 2) Macy's 100th Thanksgiving Day Parade hub
PARP="pop-culture/macys-thanksgiving-day-parade-2026/"
_MS=[("Macy's, Inc.: 100-day countdown release (Aug 18, 2026)","https://www.macysinc.com/newsroom/news/news-details/2026/Macys-Kicks-Off-the-100-Day-Countdown-to-the-100th-Macys-Thanksgiving-Day-Parade/default.aspx"),
("BBC Studios and Macy's: new Bluey balloon (Oct 5)","https://www.prnewswire.com/news-releases/new-bluey-christmas-themed-balloon-to-debut-at-the-100th-macys-thanksgiving-day-parade-302898415.html"),
("CBR: Hello Kitty returns, citing Sanrio's Oct 13 release","https://www.cbr.com/hello-kitty-macys-thanksgiving-day-parade-2026-new-balloon-design/"),
("CBS New York: Joe Cool and Woodstock balloon (Sept 16)","https://www.cbsnews.com/newyork/news/new-snoopy-balloon-macys-thanksgiving-day-parade-2026-nyc/"),
("ABC7 New York: Joe Cool and Woodstock balloon (Sept 16)","https://abc7ny.com/post/snoopy-persona-joe-cool-woodstock-balloon-debut-macys-100th-thanksgiving-day-parade/19840119/"),
("Good Housekeeping: record-breaking lineup (Aug 19)","https://www.goodhousekeeping.com/entertainment/a73476298/macys-thanksgiving-parade-balloons-2026/"),
("Rockefeller Center: where to watch the 100th parade","https://www.rockefellercenter.com/magazine/events/where-to-watch-macys-thanksgiving-day-parade"),
("CentralPark.com: parade route","https://www.centralpark.com/events/macys-thanksgiving-day-parade/"),
("Macy's parade page","https://www.macys.com/parade")]
PARADE_FAQ=[("What time is the Macy's Thanksgiving Day Parade 2026?","It steps off at 8:30 a.m. on Thursday, November 26, 2026, from West 77th Street and Central Park West, and airs from 8:30 a.m. in all time zones. It ends at Macy's Herald Square around noon, per Rockefeller Center's guide."),
("What channel is the Macy's Thanksgiving Day Parade on?","Macy's says the 100th parade airs on NBC and Telemundo and streams on Peacock, starting at 8:30 a.m. in all time zones."),
("How can I watch the Macy's parade without cable?","Peacock streams it, and NBC airs it, so a TV antenna that gets your local NBC station works. Live TV streaming services that include your local NBC station should carry it too, so check your local channel lineup. Peacock's own plan requirements can change, so check Peacock before the day."),
("What new balloons are in the 100th Macy's parade?","Macy's confirms a record 100 inflatable elements, including a new Sorcerer's Apprentice Mickey, a reimagined Underdog (first flight since 1984), Billie Brightpaw, Tom Jr. and a returning Blue Hippopotamus. Announced separately: a new Bluey balloon (Oct 5), a Hello Kitty balloon (Oct 13) and Joe Cool with Woodstock (Sept 16)."),
("Who is performing at the Macy's parade 2026?","We haven't found an official performer list yet. We'll add it here when NBC and Macy's announce it. Performers are typically announced closer to the parade."),
("What is the Macy's parade route?","South on Central Park West from 77th Street to Columbus Circle, east on Central Park South to Sixth Avenue, south on Sixth Avenue to 34th Street, then west on 34th Street to Seventh Avenue and Macy's Herald Square, about 2.5 miles."),
("Why is this the 100th parade if it started in 1924?","The count runs behind the calendar because the parade was canceled from 1942 through 1944 during World War II, per Rockefeller Center.")]
def _pl(items): return "<ul>"+"".join(f"<li>{x}</li>" for x in items)+"</ul>"
SUBS.append(("pop-culture","macys-thanksgiving-day-parade-2026","Macy's Thanksgiving Day Parade 2026","The 100th Macy's Thanksgiving Day Parade is Thursday, Nov 26, 2026, at 8:30 a.m. on NBC, Telemundo and Peacock. Time, channel, route, the record 100 inflatables and the new balloons, with sources.",["Macy's Thanksgiving Day Parade","Macy's parade","Macy's Parade"],_MS))
STITLE["macys-thanksgiving-day-parade-2026"]="Macy's Thanksgiving Day Parade 2026: How to Watch the 100th Parade, Time and Channel"
SDESC["macys-thanksgiving-day-parade-2026"]="Watch the 100th Macy's Thanksgiving Day Parade on Nov 26, 2026: start time, NBC and Peacock streaming, the full balloon lineup, route and the best free spots."
SUBDEEP["macys-thanksgiving-day-parade-2026"]=dict(
intro="<b>The 100th Macy's Thanksgiving Day Parade is Thursday, November 26, 2026, starting at 8:30 a.m. in all time zones.</b> It airs live on NBC and Telemundo and streams on Peacock, Macy's says. The parade steps off at West 77th Street and Central Park West and ends at Macy's Herald Square around noon. Macy's is marking the centennial with a record 100 inflatable elements. Everything below comes from Macy's or the sources linked at the bottom, and we say so when it doesn't.",
facts=[("Date","Thursday, November 26, 2026"),("Start time","8:30 a.m. in all time zones"),("Where to watch","NBC, Telemundo, Peacock (per Macy's)"),("Start","West 77th Street and Central Park West"),("Finish","Macy's Herald Square, around noon"),("Route length","About 2.5 miles"),("Inflatable elements","Record 100 (per Macy's)"),("Performers","Not announced yet, as far as we can find"),("Last checked","Oct 23, 2026")],
body=f'''<h2>How to watch the parade</h2>{_pl(["<b>On TV:</b> NBC and Telemundo, from 8:30 a.m. in every time zone.","<b>Streaming:</b> Peacock carries it live. Check Peacock's current plan requirements before the day.","<b>Without cable:</b> an antenna that picks up your local NBC station, or a live TV streaming service that includes it. Check your local lineup.","<b>Follow along:</b> Macy's uses the hashtag #MacysParade."])}
<h2>The route, step by step</h2><table><tr><th>1</th><td>Start at West 77th Street and Central Park West, beside the American Museum of Natural History</td></tr><tr><th>2</th><td>South on Central Park West to Columbus Circle</td></tr><tr><th>3</th><td>East on Central Park South to Sixth Avenue</td></tr><tr><th>4</th><td>South on Sixth Avenue to 34th Street</td></tr><tr><th>5</th><td>West on 34th Street to Seventh Avenue, finishing at Macy's Herald Square around noon</td></tr></table>
<h2>Where to watch in person, and when it reaches you</h2><p>Rockefeller Center's guide says the parade moves along Central Park West from about 8:30 to 10:30 a.m., and the lead units reach Sixth Avenue at 59th Street around 9:30 a.m. The farther south you stand, the later the first balloons arrive. Public viewing is on Central Park West from West 75th to West 61st streets (west side of the avenue only) and on Sixth Avenue from West 59th to West 38th streets. Not open to the public: the staging area at the start, Columbus Circle and Central Park South, Sixth Avenue from West 34th to West 38th streets, and 34th Street between Broadway and Seventh Avenue. The guide says early arrivals start around 6 a.m. and the route typically draws an estimated 3.5 million spectators.</p>
<h2>The 100th parade: what's new</h2><p>Macy's says the centennial lineup has a record 100 inflatable elements. Here is what has been announced so far.</p>
<table><tr><th>Sorcerer's Apprentice Mickey</th><td>New Disney balloon. Good Housekeeping calls it Mickey's 21st parade version in 92 years. <i>New for the 100th</i></td></tr>
<tr><th>Underdog</th><td>Reimagined, and Macy's says it's his first flight since 1984. <i>Returns</i></td></tr>
<tr><th>Bluey</th><td>New balloon inspired by the "Christmas Swim" episode, 47 feet long, 27.8 feet wide and 47.2 feet tall, per BBC Studios and Macy's (Oct 5). <i>New for the 100th</i></td></tr>
<tr><th>Hello Kitty</th><td>New balloon holding a giant red apple, about 28.4 feet wide, 33.5 feet long and 33.6 feet tall, per CBR citing Sanrio. First parade in nine years. <i>Returns</i></td></tr>
<tr><th>Joe Cool and Woodstock</th><td>Snoopy's campus persona in dark shades and a red sweater, with Woodstock under his arm, per CBS New York (Sept 16). <i>New for the 100th</i></td></tr>
<tr><th>Felix the Cat</th><td>Returns; Macy's says he was the first character balloon in the parade, carried on sticks in 1927. <i>Returns</i></td></tr>
<tr><th>Blue Hippopotamus</th><td>The balloon never recovered after the 1931 parade returns. Macy's says more details are coming. <i>Returns</i></td></tr>
<tr><th>Billie Brightpaw</th><td>A bear, described by Macy's as the parade's newest companion. <i>New for the 100th</i></td></tr>
<tr><th>Tom Jr.</th><td>Son of the parade's Tom Turkey. <i>New for the 100th</i></td></tr>
<tr><th>Macy's All-Stars float</th><td>Bullwinkle J. Moose, Olive Oyl, Popeye, Swee'Pea and Sonic the Hedgehog, per Macy's.</td></tr>
<tr><th>Tony Sarg float</th><td>"Tony Sarg's Amazing Marionettes" honors the parade's early creative force, per Macy's.</td></tr></table>
<p>Macy's says more balloon and float announcements are coming, so this list will grow. We add each one only after Macy's or the brand announces it.</p>
<h2>Performers</h2><p>We haven't found an official performer list yet. When NBC and Macy's publish one, we'll add it here with a link to the announcement.</p>
<h2>Parade facts</h2><p>The parade was first held in 1924. The count runs behind the calendar because it was canceled from 1942 through 1944 during World War II, per Rockefeller Center. The official page is <a href="https://www.macys.com/parade" rel="noopener" target="_blank">macys.com/parade</a>.</p>
<p class="by">Last checked October 23, 2026. We update this page when Macy's or NBC announces something new.</p>
<h2>More for Thanksgiving week</h2><ul><li><a href="{R2}shopping/thanksgiving-black-friday-store-hours-2026/">Thanksgiving and Black Friday store hours 2026</a></li><li><a href="../../food/">Food trends</a></li><li><a href="../../travel/">Travel trends</a></li></ul>'''+follow("MacysParade"),
faq=PARADE_FAQ)
_ld_prev=subld
def subld(h,slug,ti):
    o=_ld_prev(h,slug,ti)
    if slug=="macys-thanksgiving-day-parade-2026":
        o.append({"@context":"https://schema.org","@type":"Event","name":"The 100th Macy's Thanksgiving Day Parade","startDate":"2026-11-26T08:30:00-05:00","eventAttendanceMode":"https://schema.org/MixedEventAttendanceMode","eventStatus":"https://schema.org/EventScheduled","location":{"@type":"Place","name":"Central Park West and West 77th Street to Macy's Herald Square","address":{"@type":"PostalAddress","addressLocality":"New York","addressRegion":"NY","addressCountry":"US"}},"organizer":{"@type":"Organization","name":"Macy's","url":"https://www.macys.com/"},"description":SDESC[slug],"image":B+"/assets/img/og-autumn-avenue-barricades.jpg"})
        o.append({"@context":"https://schema.org","@type":"Article","headline":STITLE[slug][:110],"description":SDESC[slug],"mainEntityOfPage":B+"/"+PARP,"image":B+"/assets/img/og-autumn-avenue-barricades.jpg","datePublished":"2026-10-23","dateModified":"2026-10-23","author":{"@type":"Organization","name":"The Trends Incoming team","url":B+"/about/"},"publisher":pub})
    if slug=="thanksgiving-black-friday-store-hours-2026":
        o.append({"@context":"https://schema.org","@type":"Article","headline":STITLE[slug][:110],"description":SDESC[slug],"mainEntityOfPage":B+"/"+HRSP,"image":B+"/assets/img/og-holiday-mall-lights.jpg","datePublished":"2026-10-23","dateModified":"2026-10-23","author":{"@type":"Organization","name":"The Trends Incoming team","url":B+"/about/"},"publisher":pub})
    return o
T.insert(0,("pop-culture","Macy's 100th Thanksgiving Day Parade: how to watch, route and every new balloon","The 100th Macy's Thanksgiving Day Parade is Thursday, Nov 26 at 8:30 a.m. on NBC, Telemundo and Peacock, with a record 100 inflatables. Time, route and the new balloons announced so far.","Nov 26",_MS[:3],"MacysParade",PARP,1))
CD["Macy's 100th Thanksgiving Day Parade: how to watch, route and every new balloon"]="2026-11-26T08:30:00-05:00"
KEYPH[PARP]="autumn-avenue-barricades"

# 3) Holiday store hours hub
HRSP="shopping/thanksgiving-black-friday-store-hours-2026/"
_HS=[("Walmart: holiday post, Oct 7, 2026","https://corporate.walmart.com/news/2026/10/walmart-is-ready-for-the-season"),
("Costco: holiday closures","https://customerservice.costco.com/app/answers/detail/a_id/701/"),
("Home Depot: store holiday hours","https://corporate.homedepot.com/news/company/store-holiday-hours-home-depot"),
("Lowe's: Holiday 2026 lineup release","https://www.prnewswire.com/news-releases/lowes-unveils-holiday-2026-lineup-with-new-gifts-and-decor-mylowes-rewards-perks-and-weeks-of-black-friday-savings-302901573.html"),
("Tenmomo: Black Friday 2026 store hours tracker","https://tenmomo.com/black-friday/retailer-hours"),
("FreshCalendars: Black Friday 2026 store hours","https://freshcalendars.com/news/black-friday-2026-store-hours-walmart-target-best-buy/")]
HRS_FAQ=[("What stores are open on Thanksgiving Day 2026?","Most big-box retailers are closed on Thursday, November 26, 2026. Walmart says its stores will be closed on Thanksgiving, Costco lists Thanksgiving Day among its U.S. warehouse closures, and Home Depot and Lowe's are closed too. Target has said since 2021 that its stores close on Thanksgiving."),
("Is Walmart open on Thanksgiving 2026?","No. In its Oct 7, 2026 holiday post, Walmart said: \"Stores will be closed again on Thanksgiving and Christmas this year.\""),
("Is Costco open on Thanksgiving?","No. Costco's customer service page lists Thanksgiving Day among the days its U.S. warehouses are closed."),
("What time do stores open on Black Friday 2026?","Home Depot says it opens at 6 a.m. on Friday, November 27. Most other big chains had not posted 2026 hours as of our last check, so the table shows last year's times and says so. Hours vary by location."),
("Is Target open on Thanksgiving 2026?","Target said in 2021 that its stores would close on Thanksgiving Day going forward, per the Tenmomo tracker. Target has not announced 2026 Black Friday hours that we can find; it opened at 6 a.m. in 2025."),
("Are grocery stores and pharmacies open on Thanksgiving?","Many open Thanksgiving morning with shorter hours, FreshCalendars says, but hours vary by chain and location. Check your store's page or app."),
("When will Black Friday 2026 hours be announced?","Retailers usually post them in the weeks before. Tenmomo's tracker showed 1 of 64 retailers had posted 2026 Black Friday hours as of Oct 20. We update this page as stores announce.")]
SUBS.append(("shopping","thanksgiving-black-friday-store-hours-2026","Thanksgiving and Black Friday store hours 2026","Which stores are open and closed on Thanksgiving Day, Nov 26, 2026, and what time they open on Black Friday, Nov 27, with each retailer's own announcement. Updated as stores confirm.",["store hours","Black Friday hours","open on Thanksgiving"],_HS))
STITLE["thanksgiving-black-friday-store-hours-2026"]="What's Open on Thanksgiving 2026: Store Hours for Walmart, Target, Costco and More"
SDESC["thanksgiving-black-friday-store-hours-2026"]="Which stores are open and closed on Thanksgiving Day 2026 and what time they open on Black Friday, with each retailer's official announcement. Updated as stores confirm."
SUBDEEP["thanksgiving-black-friday-store-hours-2026"]=dict(
intro="<b>Most big retailers are closed on Thanksgiving Day, Thursday, November 26, 2026, and open again on Black Friday, November 27.</b> Walmart said on October 7 that its stores will be closed on Thanksgiving. Costco, Home Depot and Lowe's are closed too, and Target has said since 2021 that it closes. Most chains have not posted 2026 Black Friday hours yet. Where a store hasn't, we show last year's time and label it as last year's.",
facts=[("Thanksgiving Day","Thu, Nov 26, 2026"),("Black Friday","Fri, Nov 27, 2026"),("Closed Thanksgiving (2026)","Walmart, Costco, Home Depot, Lowe's; Target by standing policy"),("Black Friday 2026 hours posted","Home Depot (6 a.m.); most others not yet"),("Last checked","Oct 23, 2026"),("Hours vary","Check your local store")],
body=f'''<h2>Store by store</h2><table><tr><th>Store</th><th>Thanksgiving (Nov 26)</th><th>Black Friday (Nov 27)</th></tr>
<tr><td>Walmart</td><td>Closed, per Walmart's Oct 7, 2026 post</td><td>2026 hours not announced yet. 2025: 6 a.m. to 11 p.m.</td></tr>
<tr><td>Target</td><td>Closed, standing policy since 2021</td><td>2026 hours not announced yet. 2025: opened 6 a.m.</td></tr>
<tr><td>Costco</td><td>Closed, per Costco's list of U.S. warehouse closures</td><td>2026 hours not announced yet. 2025: 10 a.m., Executive members 9 a.m.; closed 8:30 p.m.</td></tr>
<tr><td>Home Depot</td><td>Closed</td><td>Opens 6 a.m., per Home Depot's holiday hours page</td></tr>
<tr><td>Lowe's</td><td>Closed, per Lowe's Holiday 2026 release</td><td>Doorbusters for everyone Nov 27. 2025: 6 a.m. open. 2026 hours not announced yet.</td></tr>
<tr><td>Best Buy</td><td>Closed in 2025. 2026 not announced yet.</td><td>2026 hours not announced yet. 2025: 6 a.m.</td></tr>
<tr><td>Macy's</td><td>Closed in 2025. 2026 not announced yet.</td><td>2026 hours not announced yet. 2025: 6 a.m.</td></tr>
<tr><td>Kohl's</td><td>Closed in 2025. Check Kohl's for 2026.</td><td>2026 hours not announced yet. 2025: 5 a.m.</td></tr></table>
<p>All 2025 times come from the Tenmomo tracker, which credits TODAY, CBS News and the retailers. They are a guide, not a promise. Hours are local store time and vary by location.</p>
<h2>Grocery stores and pharmacies</h2><p>Grocery stores and pharmacies are the main exception to Thanksgiving closures. FreshCalendars says many open Thanksgiving morning with shorter hours. We haven't confirmed chain-by-chain 2026 hours yet, so check your store's page or app, and don't leave your Thanksgiving shopping until the last minute.</p>
<h2>What's next</h2><p>As of Oct 20, Tenmomo's tracker showed only 1 of 64 retailers had posted 2026 Black Friday hours. We update this page as stores announce, and add Christmas Eve, Christmas Day and New Year's Day hours later. If a store changes its hours, trust the store's own page over ours.</p>
<h2>More for Thanksgiving week</h2><ul><li><a href="{R2}{PARP}">Macy's 100th Thanksgiving Day Parade 2026: time, channel and route</a></li><li><a href="../../travel/">Travel trends</a></li></ul>'''+follow("BlackFriday"),
faq=HRS_FAQ)
T.insert(1,("shopping","Thanksgiving and Black Friday 2026: which stores are open","Walmart, Costco, Home Depot and Lowe's close on Thanksgiving, Nov 26, and Target has said it does too. Black Friday hours are mostly not announced yet; we show last year's times and update as stores confirm.","Nov 26",_HS[:3],"BlackFriday",HRSP,0))
CD["Thanksgiving and Black Friday 2026: which stores are open"]="2026-11-26T00:00:00-05:00"
KEYPH[HRSP]="holiday-mall-lights"
# Hub callouts
for _c,_h in (("pop-culture",'<p class="warn">🦃 <b>Thanksgiving week:</b> <a href="{r}'+PARP+'">The 100th Macy\'s Thanksgiving Day Parade: time, channel, route and new balloons →</a></p>'),("shopping",'<p class="warn">🛒 <b>Thanksgiving week:</b> <a href="{r}'+HRSP+'">Which stores are open on Thanksgiving and Black Friday 2026 →</a></p>'),("tv-streaming",'<p class="warn">🦃 <a href="{r}'+PARP+'">How to watch the 100th Macy\'s Thanksgiving Day Parade →</a></p>'),("food",'<p class="warn">🦃 <a href="{r}'+HRSP+'">Which stores are open on Thanksgiving 2026 →</a></p>')):
    HUBX[_c]=HUBX.get(_c,"")+_h
PHCSS+=PHCSS_LIVE
