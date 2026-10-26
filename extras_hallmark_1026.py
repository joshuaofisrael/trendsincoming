# --- 2026-10-26 Hallmark Countdown to Christmas 2026 schedule desk (Trend Bot brief). Every title, date, time and cast checked on hallmarkchannel.com 26 Oct 2026. ---
import json as _j, datetime as _d2
HMP="tv-streaming/hallmark-christmas-movies-2026-schedule/"
HMV="Oct 26, 2026"
HMSRC="https://www.hallmarkchannel.com/christmas/countdown-to-christmas-2026-preview"
HMGUIDE="https://www.hallmarkchannel.com/christmas/movie-guide-countdown-to-christmas-2026"
_MO={"OCTOBER":10,"NOVEMBER":11,"DECEMBER":12}
HMALL=[]
for n,t,dl,st in _j.load(open("hm_ctc_2026.json")):
    p=dl.replace(",","").split(); mo=_MO[p[1].upper()]; dy=int(p[2]); tm=p[3].lower()
    kind="series" if "Mistletoe Murders" in t else ("special" if "Christmas Experience" in t else "movie")
    t=t.replace(" - Season 3 Premiere",": Season 3 premiere")
    cast=st.split(":",1)[1].strip() if st.startswith("Co-Hosts") else st.replace("Starring ","")
    HMALL.append(dict(t=t,d=_d2.date(2026,mo,dy),tm=tm,cast=cast,kind=kind,hosts=st.startswith("Co-Hosts")))
HMOV=[x for x in HMALL if x["kind"]=="movie"]
assert len(HMOV)==34, len(HMOV)
_T=_d2.date.fromisoformat(TODAY)
def _fd2(d): return d.strftime("%a %b ")+str(d.day)
def _et(x):
    h=int(x["tm"].split("/")[0])+12; off="-04:00" if x["d"]<_d2.date(2026,11,1) else "-05:00"
    return f'{x["d"].isoformat()}T{h:02d}:00:00{off}'
def _status(x):
    if x["d"]<_T: return "Aired"
    if x["d"]==_T: return "Tonight"
    return "Upcoming"
# this weekend: from today, the next Fri-Sun block (or the current one)
_wk=[x for x in HMALL if x["d"]>=_T][:0]
_up=[x for x in HMALL if x["d"]>=_T]
if _up:
    _first=_up[0]["d"]; _end=_first+_d2.timedelta(days=(6-_first.weekday())%7)
    _wk=[x for x in _up if x["d"]<=_end]
def _row(x): 
    lab={"movie":"New movie","series":"Series premiere","special":"Special"}[x["kind"]]
    who=("Hosts: " if x["hosts"] else "")+x["cast"]
    return f'<tr><td>{_fd2(x["d"])}</td><td>{x["tm"]}</td><td><b>{esc(x["t"])}</b><br><span class="h1l">{lab}</span></td><td>{esc(who)}</td><td>{_status(x)}</td></tr>'
_wkhtml=("".join(f'<li><b>{_fd2(x["d"])} at {x["tm"]}:</b> {esc(x["t"])} <span class="h1l">({esc(x["cast"])})</span></li>' for x in _wk)) or "<li>Countdown to Christmas premieres have wrapped for 2026.</li>"
_tn=[x for x in HMALL if x["d"]==_T]
_tnhtml=("Tonight on Hallmark Channel: "+", ".join(f'<b>{esc(x["t"])}</b> at {x["tm"]}' for x in _tn)+".") if _tn else (f'No new Countdown to Christmas premiere tonight. The next one is <b>{esc(_up[0]["t"])}</b> on {_fd2(_up[0]["d"])} at {_up[0]["tm"]}.' if _up else "")
_aired=sum(1 for x in HMOV if x["d"]<_T)
_tg=[x for x in HMALL if _d2.date(2026,11,26)<=x["d"]<=_d2.date(2026,11,29)]
HM_FAQ=[
("How many new Hallmark Christmas movies are there in 2026?","Hallmark Channel's official Countdown to Christmas 2026 preview lists 34 new original movies, plus the Season 3 premiere of the series Mistletoe Murders and the special The Hallmark Christmas Experience: A Hometown Holiday."),
("When does Countdown to Christmas 2026 start and end?","The first premiere, 'Tis the Season for Setups, aired Friday, October 16, 2026. The last new movie, Save the Date for Christmas, premieres Sunday, December 20, 2026 at 8/7c."),
("What time do new Hallmark Christmas movies air?","Hallmark lists premieres every Friday, Saturday and Sunday at 8/7c. Thanksgiving weekend adds a second premiere at 6/5c on Friday Nov 27, Saturday Nov 28 and Sunday Nov 29, and Christmas Delivered premieres on Thanksgiving Day, Thursday Nov 26, at 8/7c."),
("What Hallmark movie is on tonight?",_tnhtml.replace("<b>","").replace("</b>","") or "Countdown to Christmas premieres have wrapped for 2026."),
("When is the Mistletoe Murders season 3 premiere?","Thursday, November 5, 2026 at 8/7c on Hallmark Channel, starring Sarah Drew and Peter Mooney, with guest stars Catherine Bell and Holly Robinson Peete."),
("When is The Hallmark Christmas Experience special?","The Hallmark Christmas Experience: A Hometown Holiday airs Saturday, December 5, 2026 at 10/9c, hosted by Jonathan Bennett and Melissa Peterman, right after the A Grand Biltmore Christmas premiere."),
("Where can I stream Hallmark Christmas movies?","Hallmark's own streaming service is Hallmark+. Hallmark's preview page does not list next-day streaming dates for each movie, so check the Hallmark+ app for a title before you plan around it. Live airings are on Hallmark Channel."),
("Is there a Hanukkah movie in Countdown to Christmas 2026?","Yes. Eight Nights for Love, starring Hunter King and Dan Jeannotte, premieres Sunday, November 29, 2026 at 6/5c.")]
_rows="".join(_row(x) for x in HMALL)
HM_BODY=f'''<article><span class="pill">Fri, Sat, Sun 8/7c</span><h1>Hallmark Christmas Movies 2026 Schedule: Every Countdown to Christmas Premiere</h1><p class="by">{BY} · Verified on {HMV} against Hallmark Channel's official preview</p>
<p><b>Grab the cocoa!</b> Hallmark Channel's Countdown to Christmas 2026 has <b>34 brand new movies</b>, premiering every Friday, Saturday and Sunday at 8/7c from October 16 through December 20. {_aired} have aired so far. Below you'll find what's on tonight and this weekend, the full printable schedule with cast, and quick answers. We update it every weekend.</p>
<h2 id="tonight">Tonight and this weekend</h2><p>{_tnhtml}</p><ul>{_wkhtml}</ul>
<h2 id="thanksgiving">Thanksgiving weekend: two premieres a night</h2><p>Hallmark is going big for Thanksgiving. Here's the lineup:</p><ul>{"".join(f'<li><b>{_fd2(x["d"])} at {x["tm"]}:</b> {esc(x["t"])}</li>' for x in _tg)}</ul>
<h2 id="schedule">Full Countdown to Christmas 2026 schedule</h2><p class="h1l">All times Eastern/Central as listed by Hallmark. Tip: use your browser's Print button for a clean copy to stick on the fridge.</p>
<div class="tw"><table class="hmsched"><thead><tr><th>Date</th><th>Time</th><th>Title</th><th>Starring</th><th>Status</th></tr></thead><tbody>{_rows}</tbody></table></div>
<h2>Big moments to circle</h2><ul><li><b>Thu Nov 5, 8/7c:</b> Mistletoe Murders season 3 premiere.</li><li><b>Sat Nov 28, 8/7c:</b> Holiday Ever After: A Disney World Wish Come True with Lacey Chabert.</li><li><b>Sat Dec 5, 8/7c:</b> A Grand Biltmore Christmas with Andie MacDowell, then The Hallmark Christmas Experience special at 10/9c.</li><li><b>Sun Dec 20, 8/7c:</b> the finale, Save the Date for Christmas with Jonathan Bennett and Italia Ricci.</li></ul>
<h2>Lifetime, Netflix and Great American Family</h2><p>We only add other networks' holiday lineups once they're posted in an official announcement we've opened ourselves. Check back on our Thursday refresh.</p>
<h2>Quick answers</h2>{"".join(f"<h3>{esc(q)}</h3><p>{esc(a)}</p>" for q,a in HM_FAQ)}
<h2>More holiday guides</h2><ul><li><a href="../../pop-culture/macys-thanksgiving-day-parade-2026/">Macy's Thanksgiving Day Parade 2026</a></li><li><a href="../../shopping/thanksgiving-black-friday-store-hours-2026/">Thanksgiving and Black Friday store hours</a></li><li><a href="../../hubs/coming-up/">Coming Up This Month</a></li></ul>
{srclist([("Hallmark Channel: Countdown to Christmas 2026 Preview",HMSRC),("Hallmark Channel: Countdown to Christmas 2026 programming guide",HMGUIDE)])}</article>
<style>@media print{{header,footer,nav,.hubbar,.adsbygoogle,.hubrel,.crumbs{{display:none!important}}.hmsched{{font-size:10pt}}}}.hmsched{{border-collapse:collapse;width:100%}}.hmsched td,.hmsched th{{border:1px solid #999;padding:5px;vertical-align:top}}</style>'''
_SVC={"@type":"BroadcastService","name":"Hallmark Channel","url":"https://www.hallmarkchannel.com/"}
HM_LD=[{"@context":"https://schema.org","@type":"ItemList","name":"Hallmark Countdown to Christmas 2026 new movies","numberOfItems":len(HMOV),"itemListOrder":"https://schema.org/ItemListOrderAscending",
 "itemListElement":[{"@type":"ListItem","position":i+1,"item":{"@type":"Movie","name":x["t"],"actor":[{"@type":"Person","name":a.strip()} for a in x["cast"].split(",")],"productionCompany":{"@type":"Organization","name":"Hallmark Media"},
   "subjectOf":{"@type":"BroadcastEvent","name":x["t"]+" premiere","startDate":_et(x),"isLiveBroadcast":False,"publishedOn":_SVC,"location":{"@type":"VirtualLocation","url":"https://www.hallmarkchannel.com/"}}}} for i,x in enumerate(HMOV)]},
 {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in HM_FAQ]}]
KEYPH[HMP]=KEYPH.get("pop-culture/macys-thanksgiving-day-parade-2026/","holiday-mall-lights")
page(HMP+"index.html","Hallmark Christmas Movies 2026 Schedule: Every Countdown to Christmas Premiere","All new Hallmark Countdown to Christmas 2026 movies with dates, times, cast and where to stream, updated every weekend.",HM_BODY,ld=HM_LD,cat="tv-streaming")
_hmlink=f'<h2>Hallmark Christmas movies on Thanksgiving weekend</h2><p>Settling in after the parade? Hallmark has two new Countdown to Christmas premieres a night on Nov 27, 28 and 29. See the <a href="../../{HMP}">full Hallmark Christmas movies 2026 schedule</a>.</p>'
for _s in ("macys-thanksgiving-day-parade-2026","thanksgiving-black-friday-store-hours-2026"):
    if _s in SUBDEEP: SUBDEEP[_s]["body"]=_hmlink+SUBDEEP[_s]["body"]
    else: print("WARN no SUBDEEP",_s)
