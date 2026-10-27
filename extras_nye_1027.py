# --- 2026-10-27 New Year's Eve 2027 watch desk (Trend Bot brief). Facts opened 27 Oct 2026: Dick Clark Productions release (Oct 7, 2026), Deadline (Oct 7, 2026), Times Square Alliance NYE FAQ. ---
NYP="tv-streaming/new-years-rockin-eve-2027/"; NYL=NYP+"performers/"
NYT="pop-culture/times-square-new-years-eve-2027/"; NYZ="pop-culture/ball-drop-time-zones-2027/"
NY_DCP=("Dick Clark Productions: NYRE to simulcast live on ABC and Disney+ for the first time ever (Oct 7, 2026)","https://www.dickclark.com/news/nyre-to-simulcast-live-on-abc-and-disney-for-the-first-time-ever/")
NY_DL=("Deadline: Rockin' Eve 2027 to simulcast on ABC and Disney+ (Oct 7, 2026)","https://deadline.com/2026/10/dick-clarks-new-years-rockin-eve-ryan-seacrest-2027-simulcast-abc-disney-1237149016/")
NY_TSA=("Times Square Alliance: New Year's Eve FAQ","https://www.timessquarenyc.org/nye/nye-faq")
NYV="Oct 27, 2026"
_TZ=[("Eastern (New York, Miami, Detroit)","12:00 a.m. Fri Jan 1"),("Central (Chicago, Dallas, Houston)","11:00 p.m. Thu Dec 31"),("Mountain (Denver, Salt Lake City)","10:00 p.m. Thu Dec 31"),("Arizona (most of the state)","10:00 p.m. Thu Dec 31"),("Pacific (Los Angeles, Seattle, Las Vegas)","9:00 p.m. Thu Dec 31"),("Alaska (Anchorage)","8:00 p.m. Thu Dec 31"),("Hawaii (Honolulu)","7:00 p.m. Thu Dec 31")]
_TZ2=[("Eastern","12:00 a.m. Jan 1","Midnight, live with the ball drop"),("Central","1:00 a.m. Jan 1","11:00 p.m. Dec 31"),("Mountain","2:00 a.m. Jan 1","10:00 p.m. Dec 31"),("Pacific","3:00 a.m. Jan 1","9:00 p.m. Dec 31"),("Alaska","4:00 a.m. Jan 1","8:00 p.m. Dec 31"),("Hawaii","5:00 a.m. Jan 1","7:00 p.m. Dec 31")]
def nytz(): return '<div class="tw"><table><tr><th>US time zone</th><th>Times Square ball drop happens at your local time</th></tr>'+"".join(f"<tr><td>{a}</td><td><b>{b}</b></td></tr>" for a,b in _TZ)+'</table></div>'
def nyfaq(F): return {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in F]}
def nyfh(F): return "<h2>Quick answers</h2>"+"".join(f"<h3>{esc(q)}</h3><p>{esc(a)}</p>" for q,a in F)
_ORG={"@type":"Organization","name":"Dick Clark Productions","url":"https://www.dickclark.com/"}
NY_BE={"@context":"https://schema.org","@type":"BroadcastEvent","name":"Dick Clark's New Year's Rockin' Eve with Ryan Seacrest 2027","startDate":"2026-12-31T20:00:00-05:00","isLiveBroadcast":True,
 "description":"Live New Year's Eve telecast hosted by Ryan Seacrest, simulcast on ABC and Disney+ for the first time, from 8 p.m. ET on Thursday, December 31, 2026.",
 "publishedOn":[{"@type":"BroadcastService","name":"ABC","url":"https://abc.com/"},{"@type":"BroadcastService","name":"Disney+","url":"https://www.disneyplus.com/"}],
 "location":{"@type":"VirtualLocation","url":"https://www.newyearsrockineve.com/"},"organizer":_ORG,
 "performer":[{"@type":"Person","name":n} for n in ("Ryan Seacrest","Rita Ora","Druski","Julianne Hough","Rob Gronkowski")]}
NY_EV={"@context":"https://schema.org","@type":"Event","name":"Times Square New Year's Eve Ball Drop 2027","startDate":"2026-12-31T23:59:00-05:00","endDate":"2027-01-01T00:00:00-05:00",
 "description":"The Times Square Ball makes its 60 second descent from One Times Square at 11:59 p.m. ET to ring in 2027. Free outdoor viewing, no tickets.",
 "eventStatus":"https://schema.org/EventScheduled","eventAttendanceMode":"https://schema.org/MixedEventAttendanceMode",
 "location":[{"@type":"Place","name":"Times Square, One Times Square","address":{"@type":"PostalAddress","streetAddress":"1 Times Square","addressLocality":"New York","addressRegion":"NY","postalCode":"10036","addressCountry":"US"}},{"@type":"VirtualLocation","url":"https://www.timessquarenyc.org/"}],
 "isAccessibleForFree":True,"offers":{"@type":"Offer","price":"0","priceCurrency":"USD","availability":"https://schema.org/InStock","url":"https://www.timessquarenyc.org/nye/nye-faq","validFrom":"2026-10-01T00:00:00-04:00"},
 "organizer":{"@type":"Organization","name":"Times Square Alliance","url":"https://www.timessquarenyc.org/"}}
_more=lambda r:f'<h2>More New Year\'s Eve guides</h2><ul><li><a href="{r}{NYP}">New Year\'s Rockin\' Eve 2027: how to watch</a></li><li><a href="{r}{NYL}">Rockin\' Eve 2027 performers (lineup tracker)</a></li><li><a href="{r}{NYT}">Times Square New Year\'s Eve 2027 in person: rules</a></li><li><a href="{r}{NYZ}">Ball drop time in every US time zone</a></li><li><a href="{r}hubs/holidays-observances/">All holidays and observances</a></li></ul>'
# main guide
NYF=[("When does New Year's Rockin' Eve 2027 start?","Dick Clark's New Year's Rockin' Eve with Ryan Seacrest 2027 airs live on Thursday, December 31, 2026, beginning at 8 p.m. ET (listed as 8/7c) on ABC and Disney+, according to Dick Clark Productions."),
("Is New Year's Rockin' Eve on Disney+?","Yes. For the first time in the show's history, the 2027 edition will simulcast on Disney+ alongside the live ABC broadcast."),
("Who is hosting New Year's Eve 2027 on ABC?","Ryan Seacrest hosts. Rita Ora co hosts from Times Square, comedian Druski joins as the Chicago co host, and Julianne Hough and Rob Gronkowski co host from Las Vegas."),
("Who is performing on New Year's Rockin' Eve 2027?","The performer lineup has not been announced yet. Dick Clark Productions says more details will come in the coming months. Our lineup tracker adds names as they are officially announced."),
("What time does the ball drop in Central time?","The ball drops at midnight Eastern, which is 11 p.m. Central on Thursday, December 31. It starts its 60 second descent at 11:59 p.m. Eastern."),
("How many people watched Rockin' Eve last year?","Dick Clark Productions, citing Nielsen, says the 2026 edition reached 46 million total viewers, and more than 30 million watched the Times Square Ball Drop at midnight.")]
NY_BODY=f'''<article><span class="pill">Thu Dec 31, 8 p.m. ET</span><h1>New Year's Rockin' Eve 2027: Hosts, Performers and How to Watch</h1><p class="by">{BY} · Checked {NYV} against the Dick Clark Productions announcement</p>
<p><b>Short answer:</b> Dick Clark's New Year's Rockin' Eve with Ryan Seacrest 2027 airs live on <b>Thursday, December 31, 2026, from 8 p.m. ET</b> on <b>ABC</b>, and for the first time ever it also streams on <b>Disney+</b>. The ball drops at midnight Eastern, which is 11 p.m. Central and 9 p.m. Pacific.</p>
<h2 id="watch">How to watch the ball drop 2027</h2><div class="tw"><table><tr><th>Option</th><th>What we know</th></tr>
<tr><td><b>ABC</b></td><td>Live from 8 p.m. ET (8/7c) on Thu Dec 31. Check your local ABC station for start times outside Eastern and Central.</td></tr>
<tr><td><b>Disney+</b></td><td>Simulcast alongside ABC, a first in the show's history. You need a Disney+ subscription.</td></tr>
<tr><td><b>Times Square Alliance livestream</b></td><td>Last year the Alliance ran a free, commercial free webcast on TimesSquareNYC.org from 6 p.m., plus an accessible stream with open captions and ASL. We'll confirm the 2027 stream when the Alliance posts it.</td></tr>
<tr><td><b>Other networks</b></td><td>CNN, NBC and Fox have not posted 2027 New Year's Eve plans that we could verify. We'll add them once they are officially announced.</td></tr></table></div>
<h2 id="hosts">Who is hosting</h2><ul><li><b>Ryan Seacrest</b>, host</li><li><b>Rita Ora</b>, returning co host, Times Square</li><li><b>Druski</b>, new co host, Chicago</li><li><b>Julianne Hough and Rob Gronkowski</b>, returning co hosts, Las Vegas</li></ul>
<h2 id="performers">Performers</h2><p>The 2027 lineup isn't out yet. Dick Clark Productions says more details are coming in the months ahead. Follow our <a href="performers/">Rockin' Eve 2027 performers tracker</a>, which we update as names are officially announced.</p>
<h2 id="timezones">Ball drop time in every US time zone</h2>{nytz()}<p>Full breakdown: <a href="../../{NYZ}">midnight in every US time zone</a>.</p>
<h2>Last year's numbers</h2><p>The 2026 edition reached <b>46 million total viewers</b>, the No. 1 program of the night, and <b>more than 30 million</b> watched the ball drop at midnight, according to Dick Clark Productions citing Nielsen. It ran eight hours with 42 performers.</p>
<h2>Going in person?</h2><p>It's free, but there are strict rules: no bags, no bathrooms, and once you leave you can't get back in. Read our <a href="../../{NYT}">Times Square New Year's Eve in person guide</a>.</p>
{nyfh(NYF)}{_more("../../")}
{srclist([NY_DCP,NY_DL,NY_TSA])}</article>'''
page(NYP+"index.html","New Year's Rockin' Eve 2027: Hosts, Performers and How to Watch","Rockin' Eve airs 31 Dec from 8 p.m. ET on ABC and, for the first time, Disney+. Hosts, lineup as announced, and ball drop times in every US time zone.",NY_BODY,ld=[NY_BE,NY_EV,nyfaq(NYF)],cat="tv-streaming")
# lineup placeholder
NLF=[("Who is performing on New Year's Rockin' Eve 2027?","No performers have been announced yet as of "+NYV+". Dick Clark Productions says more details will be announced in the coming months."),
("Who performed on Rockin' Eve last year?","Dick Clark Productions lists Diana Ross ushering in the new year from Times Square, plus Mariah Carey, Post Malone, Chappell Roan, Pitbull, OneRepublic, Demi Lovato, Ciara and many others among 42 performers.")]
NL_BODY=f'''<article><span class="pill">Lineup not announced yet</span><h1>New Year's Rockin' Eve 2027 Performers: Lineup Tracker</h1><p class="by">{BY} · Last checked {NYV}</p>
<p><b>Status:</b> no performers have been announced for Dick Clark's New Year's Rockin' Eve with Ryan Seacrest 2027 yet. Dick Clark Productions says more details are coming in the months ahead. We add every name here as soon as it's officially announced, with the source.</p>
<h2>Confirmed so far</h2><div class="tw"><table><tr><th>Who</th><th>Role</th><th>Where</th></tr><tr><td>Ryan Seacrest</td><td>Host</td><td>Times Square</td></tr><tr><td>Rita Ora</td><td>Co host</td><td>Times Square</td></tr><tr><td>Druski</td><td>Co host</td><td>Chicago</td></tr><tr><td>Julianne Hough</td><td>Co host</td><td>Las Vegas</td></tr><tr><td>Rob Gronkowski</td><td>Co host</td><td>Las Vegas</td></tr></table></div>
<h2>Performers</h2><p>To be announced. Check back. We refresh this page on every official lineup announcement.</p>
<h2>How to watch</h2><p>Thu Dec 31 from 8 p.m. ET on ABC and Disney+. Details in our <a href="../">how to watch guide</a>.</p>
{nyfh(NLF)}{_more("../../../")}{srclist([NY_DCP])}</article>'''
page(NYL+"index.html","New Year's Rockin' Eve 2027 Performers: Lineup Tracker","Who is performing on New Year's Rockin' Eve 2027? Confirmed hosts now, and every performer added as soon as ABC and Dick Clark Productions announce them.",NL_BODY,ld=[nyfaq(NLF)],cat="tv-streaming")
# Times Square in person
NTF=[("Do you need tickets for Times Square on New Year's Eve?","No. The Times Square Alliance says the outdoor celebration is free and first come, first served. No public viewing spaces are sold. Only private parties inside restaurants and hotels need tickets."),
("What time should I get to Times Square for New Year's Eve?","Last year the Alliance said viewing areas officially opened at 3 p.m., and people start arriving in the afternoon. Areas fill up north from 43rd Street, so earlier is better."),
("Are there bathrooms in Times Square on New Year's Eve?","No. The Alliance says there are no portable restrooms during the celebration, and if you leave your viewing area you can't return to your spot."),
("What can't you bring to Times Square on New Year's Eve?","Backpacks, large bags, umbrellas, folding chairs, picnic blankets, large coolers, alcohol, drones, weapons and other large items. All bags are searched.")]
NT_BODY=f'''<article><span class="pill">Free, no tickets</span><h1>Times Square New Year's Eve 2027 in Person: Rules, Arrival Time and What to Bring</h1><p class="by">{BY} · Checked {NYV}</p>
<p class="warn">These rules come from the Times Square Alliance's New Year's Eve FAQ as posted for last year's celebration. The Alliance updates them in December, and we'll refresh this page when it does.</p>
<h2>The basics</h2><ul><li><b>Free:</b> no tickets needed and no public viewing spots are for sale. Beware of "all access" passes; the Alliance warns they don't get you past police lines.</li><li><b>Arrival:</b> viewing areas opened at 3 p.m. last year, first come, first served.</li><li><b>Ball raise:</b> around 6 p.m. ET. <b>Ball drop:</b> 60 second descent starting at 11:59 p.m. ET.</li><li><b>Best view:</b> along Broadway from 43rd to 50th Street and along Seventh Avenue up to 59th Street.</li></ul>
<h2>How to get in</h2><p>Enter from 6th Avenue or 8th Avenue only. Viewing area access points were at <b>45th, 49th, 52nd and 56th Streets</b>, from 6th and 8th Avenues. You can't cross Broadway or Seventh Avenue once streets close. Take the subway, but skip the Times Square 42nd Street station on the night.</p>
<h2>What you can't bring</h2><p>Backpacks, large bags, umbrellas, lawn or folding chairs, picnic blankets, large coolers, alcohol, drones, weapons and other large items. All bags are searched. Public drinking is illegal in New York City.</p>
<h2>The hard parts</h2><ul><li><b>No bathrooms:</b> there are no portable restrooms.</li><li><b>No food vendors:</b> no licensed food or drink vendors in the area.</li><li><b>No coming back:</b> leave your spot, even to eat, and you can't return to it.</li><li><b>Cold:</b> dress in layers for hours outside, possibly below freezing.</li></ul>
<h2>Alerts</h2><p>NYC Emergency Management runs an opt in text service: text <b>NEWYEARSEVE</b> to <b>692692</b> for weather, closures and traffic (NOCHEVIEJA for Spanish).</p>
<h2>Rather stay warm?</h2><p>Watch on ABC or Disney+ from 8 p.m. ET. See <a href="../../{NYP}">how to watch Rockin' Eve 2027</a>.</p>
{nyfh(NTF)}{_more("../../")}{srclist([NY_TSA])}</article>'''
page(NYT+"index.html","Times Square New Year's Eve 2027 in Person: Rules, Arrival Time and What to Bring","Free, no tickets, no bathrooms and no bags: the Times Square ball drop rules, entry points and arrival time, from the Times Square Alliance.",NT_BODY,ld=[NY_EV,nyfaq(NTF)],cat="pop-culture")
# time zones
NZF=[("What time does the ball drop in Central time?","11:00 p.m. Central on Thursday, December 31. The ball drops at midnight Eastern."),
("What time does the ball drop in Pacific time?","9:00 p.m. Pacific on Thursday, December 31."),
("What time does the ball drop in Mountain time?","10:00 p.m. Mountain on Thursday, December 31. Most of Arizona, which skips daylight saving time, is also on 10:00 p.m."),
("What time is midnight Eastern in Hawaii?","7:00 p.m. Hawaii time on December 31.")]
NZ_BODY=f'''<article><span class="pill">Midnight ET = 11 p.m. CT</span><h1>Ball Drop 2027 Time in Every US Time Zone</h1><p class="by">{BY} · Checked {NYV}</p>
<p>The Times Square Ball starts its 60 second descent at <b>11:59 p.m. ET</b> and hits midnight Eastern as 2027 begins. Here's when that is where you live, and when your own local midnight lands.</p>
<h2>When the Times Square ball drops, in your time zone</h2>{nytz()}
<h2>Your own local midnight, in Eastern time</h2><div class="tw"><table><tr><th>Zone</th><th>Local midnight is this time in New York</th><th>Ball drop is your local time</th></tr>'''+"".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for a,b,c in _TZ2)+f'''</table></div>
<p>ABC and Disney+ start Rockin' Eve at 8 p.m. ET (8/7c). For anywhere else, check your local ABC station for its airing time. More in our <a href="../../{NYP}">how to watch guide</a>.</p>
{nyfh(NZF)}{_more("../../")}{srclist([NY_TSA,NY_DCP])}</article>'''
page(NYZ+"index.html","Ball Drop 2027 Time in Every US Time Zone","What time the Times Square ball drops in Central, Mountain, Pacific, Alaska and Hawaii time, and when your local midnight hits.",NZ_BODY,ld=[NY_EV,nyfaq(NZF)],cat="pop-culture")
# cross links
NYLINK=lambda r:f'<p class="warn">🎆 <b>Next up, New Year\'s Eve:</b> <a href="{r}{NYP}">New Year\'s Rockin\' Eve 2027</a> airs Thu Dec 31 from 8 p.m. ET on ABC and, for the first time, Disney+. Plus <a href="{r}{NYZ}">ball drop times in every US time zone</a>.</p>'
for _s in ("macys-thanksgiving-day-parade-2026",):
    if _s in SUBDEEP: SUBDEEP[_s]["body"]=SUBDEEP[_s]["body"]+NYLINK("../../")
    else: print("WARN no SUBDEEP",_s)
page(HMP+"index.html","Hallmark Christmas Movies 2026 Schedule: Every Countdown to Christmas Premiere","All new Hallmark Countdown to Christmas 2026 movies with dates, times, cast and where to stream, updated every weekend.",HM_BODY.replace("<h2>Quick answers</h2>",NYLINK("../../")+"<h2>Quick answers</h2>",1),ld=HM_LD,cat="tv-streaming")
page(WR+"index.html",WTITLE,WDESC,wbody+NYLINK("../../"),ld=[art19(WTITLE,WDESC,WR,WSRC,"Spotify Wrapped 2026"),wev,whowld,faqld(WQ),crumbs(WRCR)],article=False,cat="music")
page(MW+"index.html",MTITLE2,MDESC2,mbody+NYLINK("../../"),ld=[art19(MTITLE2,MDESC2,MW,MWSRC,"US minimum wage 2027"),mwds,mwil,faqld(MQ2),crumbs(MWCR)],article=False,cat="money")
