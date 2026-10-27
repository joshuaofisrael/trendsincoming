# Topic hubs. Every new guide MUST be filed in HUBMAP (path -> hub). Build fails otherwise.
import datetime as _dt
HUBS=[
 ("thanksgiving-black-friday","🦃","Thanksgiving and Black Friday","Store hours, dinner deals and the Macy's parade for Thanksgiving week 2026."),
 ("holidays-observances","📅","Holidays and Observances","Veterans Day, Halloween, Election Day and other dated days, with what is open and what is free."),
 ("money-benefits","💵","Money and Benefits","COLA 2027, 2027 tax numbers, minimum wage raises and open enrollment deadlines."),
 ("games-movies-music","🎮","Games, Movies and Music","Release dates, award shows and tour tickets: GTA VI, Zelda, The Game Awards, Grammys and more."),
 ("sports","🏀","Sports","Where to watch the NBA and NHL, the NBA Cup, the World Series and the WNBA Finals."),
]
HUBN={s:(e,n,d) for s,e,n,d in HUBS}
# path: (hub, ISO date or None, short title, one line)
HUBMAP={
 "shopping/thanksgiving-black-friday-store-hours-2026/":("thanksgiving-black-friday","2026-11-26","Thanksgiving and Black Friday store hours","Which stores are closed on Thanksgiving and when Black Friday doors open."),
 "shopping/thanksgiving-dinner-deals-2026/":("thanksgiving-black-friday","2026-11-26","Thanksgiving dinner deals compared","Aldi, Lidl, Target and Sam's Club holiday meal prices side by side."),
 "pop-culture/macys-thanksgiving-day-parade-2026/":("thanksgiving-black-friday","2026-11-26","Macy's Thanksgiving Day Parade 2026","Start time, route and how to watch the parade."),
 "shopping/veterans-day-free-meals-deals-2026/":("holidays-observances","2026-11-11","Veterans Day free meals and deals","Verified Veterans Day 2026 offers from restaurants and stores."),
 "tv-streaming/hallmark-christmas-movies-2026-schedule/":("holidays-observances","2026-10-30","Hallmark Christmas movies 2026 schedule","All 34 new Countdown to Christmas premieres, Fri, Sat and Sun at 8/7c through Dec 20."),
 "pop-culture/when-is-hanukkah-2026/":("holidays-observances","2026-12-04","When is Hanukkah 2026","Starts at sundown Fri Dec 4, ends Sat Dec 12, with a night-by-night candle chart."),
 "tv-streaming/new-years-rockin-eve-2027/":("holidays-observances","2026-12-31","New Year's Rockin' Eve 2027: how to watch","ABC and, for the first time, Disney+ from 8 p.m. ET Thu Dec 31, with hosts and ball drop times."),
 "tv-streaming/new-years-rockin-eve-2027/performers/":("holidays-observances","2026-12-31","Rockin' Eve 2027 performers","Lineup tracker, updated as performers are announced."),
 "pop-culture/times-square-new-years-eve-2027/":("holidays-observances","2026-12-31","Times Square New Year's Eve in person","Free entry, arrival time, banned items and no bathrooms."),
 "pop-culture/ball-drop-time-zones-2027/":("holidays-observances","2026-12-31","Ball drop time in every US time zone","Midnight ET is 11 p.m. CT, 10 p.m. MT and 9 p.m. PT."),
 "pop-culture/halloween-costumes-2026/":("holidays-observances","2026-10-31","Halloween costumes 2026","The costumes everyone is searching for this year."),
 "politics/early-voting-2026/":("holidays-observances","2026-11-03","Election Day and early voting 2026","How early voting works before Election Day on Nov 3."),
 "money/social-security-2027/":("money-benefits","2027-01-01","Social Security COLA 2027","The 3.6% COLA, new benefit amounts and January payment dates."),
 "money/2027-tax-numbers/":("money-benefits",None,"2027 tax numbers","Brackets, 401(k), HSA and mileage numbers for 2027, tracked from IRS releases."),
 "money/minimum-wage-2027/":("money-benefits","2027-01-01","Minimum wage by state 2027","Every state minimum wage raise that starts January 1, 2027."),
 "money/open-enrollment-2027/":("money-benefits","2026-11-01","Open enrollment 2027","ACA marketplace open enrollment dates and deadlines."),
 "money/medicare-open-enrollment-2027/":("money-benefits","2026-12-07","Medicare open enrollment 2027","Medicare open enrollment runs Oct 15 to Dec 7."),
 "games/zelda-switch-2-40th-anniversary-edition/":("games-movies-music","2026-10-29","Zelda Switch 2 40th Anniversary Edition","Release day details for the Zelda Switch 2 bundle."),
 "games/ocarina-of-time-remake/":("games-movies-music","2026-11-05","Ocarina of Time remake","Release date and what is new in the remake."),
 "gaming/pokemon-delta-reign-30th-celebration/":("games-movies-music","2026-11-06","Pokemon Delta Reign","Pokemon Delta Reign and the 30th celebration."),
 "games/gta-6-release-date/":("games-movies-music","2026-11-19","GTA VI release date","GTA VI is coming November 19, 2026."),
 "movies/sunrise-on-the-reaping-guide/":("games-movies-music","2026-11-20","Sunrise on the Reaping","Release date, tickets, runtime and watch order."),
 "music/grammy-nominations-2027/":("games-movies-music","2026-11-16","Grammy nominations 2027","When the 2027 Grammy nominations are announced and how to watch."),
 "games/the-game-awards-2026/":("games-movies-music","2026-12-10","The Game Awards 2026","Date, time, tickets, nominees and how to vote."),
 "movies/narnia-magicians-nephew-release-date/":("games-movies-music","2027-02-12","Narnia: The Magician's Nephew","Theater date, IMAX previews and Netflix date."),
 "music/spotify-wrapped-2026/":("games-movies-music",None,"Spotify Wrapped 2026","When Wrapped drops and how to see yours."),
 "music/zach-bryan-2027-tour-tickets/":("games-movies-music",None,"Zach Bryan 2027 tour","Tour dates, presale steps and ticket times."),
 "sports/nba-where-to-watch-2026-27/":("sports",None,"NBA 2026-27: where to watch","Every national TV and streaming option this season."),
 "sports/nba-cup-2026/":("sports","2026-10-30","NBA Cup 2026","Schedule, standings and how to watch every round."),
 "sports/nhl-where-to-watch-2026-27/":("sports",None,"NHL 2026-27: where to watch","National TV and streaming for the NHL season."),
 "sports/world-series-2026/":("sports",None,"World Series 2026","Game schedule and how to watch."),
 "sports/wnba-finals-2026/":("sports",None,"WNBA Finals 2026","Finals schedule and how to watch."),
}
# Older pages created before the hub rule; exempt from enforcement.
HUB_CUTOFF="2026-10-26"
_MON=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
def _fd(iso):
    if not iso: return "Ongoing"
    d=_dt.date.fromisoformat(iso); return f"{d.strftime('%a')} {_MON[d.month-1]} {d.day}, {d.year}"
# Cross-listed guides: path -> extra hubs
HUBALSO={"tv-streaming/hallmark-christmas-movies-2026-schedule/":["games-movies-music","thanksgiving-black-friday"],"tv-streaming/new-years-rockin-eve-2027/":["games-movies-music"],"tv-streaming/new-years-rockin-eve-2027/performers/":["games-movies-music"]}
def hub_items(s): 
    it=[(p,v) for p,v in HUBMAP.items() if v[0]==s or s in HUBALSO.get(p,[])]
    return sorted(it,key=lambda x:(x[1][1] is None,x[1][1] or ""))
def hub_list(items,r):
    return '<ul class="hubl">'+"".join(f'<li><span class="hd">{_fd(v[1])}</span> <a href="{r}{p}">{esc(v[2])}</a><br><span class="h1l">{esc(v[3])}</span></li>' for p,v in items)+'</ul>'
def coming_up(days=30):
    t=_dt.date.fromisoformat(TODAY); end=t+_dt.timedelta(days=days)
    it=[(p,v) for p,v in HUBMAP.items() if v[1] and t<=_dt.date.fromisoformat(v[1])<=end]
    return sorted(it,key=lambda x:x[1][1])
def hubbar(r):
    return '<nav class="hubbar" aria-label="Topic hubs">'+"".join(f'<a href="{r}hubs/{s}/">{e} {n}</a>' for s,e,n,d in HUBS)+f'<a href="{r}hubs/coming-up/">🗓️ Coming Up</a></nav>'
def hub_wrap(k,r,lds,body):
    v=HUBMAP.get(k)
    if not v: return lds,body
    s=v[0]; e,n,d=HUBN[s]
    lds=[x for x in lds if x.get("@type")!="BreadcrumbList"]
    lds.append({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":B+"/"},{"@type":"ListItem","position":2,"name":n,"item":B+f"/hubs/{s}/"},{"@type":"ListItem","position":3,"name":v[2],"item":B+"/"+k}]})
    bc=f'<nav class="crumbs" aria-label="Breadcrumb"><a href="{r}">Home</a> &gt; <a href="{r}hubs/{s}/">{n}</a> &gt; <span>{esc(v[2])}</span></nav>'
    rel=[x for x in hub_items(s) if x[0]!=k]
    blk=f'<section class="hubrel"><h2>Related in {n}</h2>'+hub_list(rel,r)+f'<p><a href="{r}hubs/{s}/">See the full {n} hub</a></p></section>'
    return lds,bc+body+blk
def home_hubs(r=""):
    cu=coming_up()
    return ('<section class="hubhome"><h2>🧭 Browse by hub</h2><div class="hubgrid">'+"".join(f'<a class="hubc" href="{r}hubs/{s}/"><b>{e} {n}</b><span>{d}</span><i>{len(hub_items(s))} guides</i></a>' for s,e,n,d in HUBS)+
      f'</div><h2>🗓️ Next 30 days</h2>'+hub_list(cu,r)+f'<p><a href="{r}hubs/coming-up/">Full Coming Up calendar</a></p></section>')
def render_hubs():
    allp=set(DATES)
    for p in HUBMAP:
        if not os.path.exists(p+"index.html"): raise SystemExit(f"HUB ERROR: {p} filed in HUBMAP but not built")
    def ild(name,url,items):
        return [{"@context":"https://schema.org","@type":"CollectionPage","name":name,"url":url,"isPartOf":{"@type":"WebSite","name":"Trends Incoming","url":B+"/"},"publisher":{"@type":"Organization","name":"Trends Incoming","url":B+"/"},
          "mainEntity":{"@type":"ItemList","numberOfItems":len(items),"itemListElement":[{"@type":"ListItem","position":i+1,"url":B+"/"+p,"name":v[2]} for i,(p,v) in enumerate(items)]}},
          {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":B+"/"},{"@type":"ListItem","position":2,"name":name,"item":url}]}]
    for s,e,n,d in HUBS:
        it=hub_items(s); r="../../"
        body=f'<nav class="crumbs" aria-label="Breadcrumb"><a href="{r}">Home</a> &gt; <span>{n}</span></nav><h1>{e} {n}</h1><p>{d}</p><p><b>{len(it)} guides</b>, sorted by date. Dated items first, ongoing guides last.</p>'+hub_list(it,r)+'<h2>Other hubs</h2><ul>'+"".join(f'<li><a href="{r}hubs/{s2}/">{e2} {n2}</a></li>' for s2,e2,n2,d2 in HUBS if s2!=s)+f'<li><a href="{r}hubs/coming-up/">🗓️ Coming Up This Month</a></li></ul>'
        page(f"hubs/{s}/index.html",f"{n} guides 2026 | Trends Incoming",d,body,ild(n,B+f"/hubs/{s}/",it),article=False,rel=False)
    cu=coming_up(); r="../../"
    body=f'<nav class="crumbs" aria-label="Breadcrumb"><a href="{r}">Home</a> &gt; <span>Coming Up This Month</span></nav><h1>🗓️ Coming Up This Month</h1><p>Every dated guide across our hubs for the next 30 days, sorted automatically by date. Rebuilt every time the site updates.</p>'
    cur=None
    for p,v in cu:
        e,n,_=HUBN[v[0]]
        body+=f'<h3>{_fd(v[1])}</h3>' if v[1]!=cur else ""; cur=v[1]
        body+=f'<p><a href="{r}{p}">{esc(v[2])}</a> <span class="h1l">({e} {n})</span><br>{esc(v[3])}</p>'
    body+=f'<h2>Further out</h2><p><a href="{r}tv-streaming/new-years-rockin-eve-2027/">New Year\'s Rockin\' Eve 2027: how to watch</a> (Thu Dec 31, 8 p.m. ET on ABC and Disney+) and <a href="{r}pop-culture/ball-drop-time-zones-2027/">ball drop times in every US time zone</a>.</p>'
    body+='<h2>All hubs</h2><ul>'+"".join(f'<li><a href="{r}hubs/{s}/">{e} {n}</a></li>' for s,e,n,d in HUBS)+'</ul>'
    page("hubs/coming-up/index.html","Coming Up This Month: dates to know | Trends Incoming","An auto-sorted calendar of every dated guide on Trends Incoming for the next 30 days: holidays, releases, deadlines and games.",body,ild("Coming Up This Month",B+"/hubs/coming-up/",cu),article=False,rel=False)
    body=f'<h1>🧭 All hubs</h1><ul>'+"".join(f'<li><a href="{s}/">{e} {n}</a>: {d} ({len(hub_items(s))} guides)</li>' for s,e,n,d in HUBS)+'<li><a href="coming-up/">🗓️ Coming Up This Month</a></li></ul>'
    page("hubs/index.html","Topic hubs | Trends Incoming","Browse Trends Incoming guides by hub: Thanksgiving, holidays, money, games and entertainment, and sports.",body,article=False,rel=False)
    # enforcement: new guides must be filed under a hub
    skip=("blog/","hubs/","contact/","search/")
    miss=[k for k,e in DATES.items() if e.get("pub","")>=HUB_CUTOFF and k.count("/")>=2 and not k.startswith(skip) and k not in HUBMAP and not any(k.startswith(h) and k!=h for h in HUBMAP)]
    if miss: raise SystemExit("HUB ERROR: guides with no hub (add to HUBMAP in hubs.py): "+", ".join(miss))

HUBCSS='.hubbar{max-width:1100px;margin:auto;display:flex;gap:8px;padding:0 14px 8px;overflow-x:auto;white-space:nowrap;-webkit-overflow-scrolling:touch}.hubbar a{font-weight:800;font-size:.8rem;color:var(--ink);text-decoration:none;background:var(--lime);border:2px solid var(--ink);border-radius:8px;padding:2px 9px;flex:0 0 auto}\n.crumbs{font-size:.85rem;margin:0 0 10px}.hubl{list-style:none;padding:0}.hubl li{border-bottom:1px dashed #999;padding:8px 0}.hd{display:inline-block;min-width:150px;font-weight:800}.h1l{font-size:.88rem;color:#444}.hubrel{border-top:3px solid var(--ink);margin-top:28px;padding-top:6px}\n.hubgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px}.hubc{display:flex;flex-direction:column;gap:4px;border:3px solid var(--ink);border-radius:12px;padding:12px;background:#fff;color:var(--ink);text-decoration:none}.hubc span{font-size:.85rem}.hubc i{font-size:.8rem;font-weight:700}\n'
