# --- Wrapped Week hub (added 2026-10-19). exec'd from build.py after extras_daily_1018 ---
PUB19="2026-10-19"
FC19="Oct 19, 2026"
def srcl(s): return '<h2>Sources</h2><ul class="src">'+"".join(f'<li><a href="{u}" rel="noopener" target="_blank">{esc(t)}</a></li>' for t,u in s)+f'</ul><p class="by">{BY} · Fact-checked {FC19}. Dates and rates change, so double-check with the official source.</p>'
def art19(title,desc,path,cites,about):
    return {"@context":"https://schema.org","@type":"Article","headline":title,"description":desc,"datePublished":PUB19,"dateModified":PUB19,"mainEntityOfPage":B+"/"+path,"image":B+"/og/"+("music" if path.startswith("music") else "money")+".png","author":{"@type":"Organization","name":"The Trends Incoming team","url":B+"/about/"},"publisher":pub,"citation":[u for _,u in cites],"about":{"@type":"Thing","name":about}}
EXPP='<span class="pill" style="background:#ff4fa3;color:#fff">EXPECTED, NOT CONFIRMED</span>'
OFFP='<span class="pill" style="background:#1a7f37;color:#fff">OFFICIAL</span>'
LAWP='<span class="pill" style="background:#1a7f37;color:#fff">SET BY LAW</span>'
PENDP='<span class="pill" style="background:#ff4fa3;color:#fff">PENDING</span>'
WR="music/spotify-wrapped-2026/"
WRT=WR+"wrapped-not-showing/"; WRA=WR+"apple-music-replay-2026/"; WRY=WR+"youtube-music-recap-2026/"
W_EXP="2026-12-02"
S_SPMETH=("Spotify Newsroom: how 2025 Wrapped data works (Jan 1 to mid November cutoff), Dec 5, 2025","https://newsroom.spotify.com/2025-12-05/wrapped-methodology-explained/")
S_SPUX=("Spotify Newsroom: 2025 Wrapped is here (eligibility and where to find it), Dec 3, 2025","https://newsroom.spotify.com/2025-12-03/2025-wrapped-user-experience/")
S_SPMADE=("Spotify Newsroom: how your Wrapped is made (Dec 3, 2025 launch, mid November cutoff)","https://newsroom.spotify.com/2025-12-03/how-your-wrapped-is-made/")
S_SPART=("Spotify for Artists: Get ready for 2026 Wrapped (video messages due Nov 6)","https://artists.spotify.com/get-ready-for-wrapped")
S_SPSUP=("Spotify Support: Spotify Wrapped","https://support.spotify.com/us/article/spotify-wrapped/")
S_SPCOM=("Spotify Community: Wrapped 2025 thread (campaign ended Jan 16, 2026)","https://community.spotify.com/forum/en/discussion/7219494/wrapped-2025")
S_OC=("Official Charts: Spotify Wrapped release dates 2018 to 2025 and the 2026 outlook (Aug 19, 2026)","https://www.officialcharts.com/chart-news/spotify-wrapped-2026-release-date/")
S_APSUP=("Apple Support: How to get your Apple Music Replay","https://support.apple.com/en-us/109356")
S_APUSA=("USA Today: Apple Music Replay 2025 dropped Dec 2 (with 2022 to 2024 dates)","https://www.usatoday.com/story/entertainment/music/2025/12/01/apple-music-replay-2025/87549858007/")
S_APAP=("AP News: how to find Spotify Wrapped, YouTube Recap, Apple Replay and more (2025)","https://apnews.com/article/spotify-youtube-twitch-amazon-recap-2025-3d057a82a1c75c13b1ddabb6da84f1f3")
S_YTHELP=("YouTube Music Help: View your YouTube Music Recap (eligibility, Jan 1 to Nov 15 window)","https://support.google.com/youtubemusic/answer/11418178?hl=en")
S_YTBLOG=("YouTube Official Blog: Introducing YouTube Recap (Dec 2, 2025)","https://blog.youtube/news-and-events/youtube-recap-2025/")
S_9TO5=("9to5Google: YouTube Music rolling out 2025 Recap (Nov 24, 2025)","https://9to5google.com/2025/11/24/youtube-music-2025-recap/")
WHIST=[("2025","2025-12-03"),("2024","2024-12-04"),("2023","2023-11-29"),("2022","2022-11-30"),("2021","2021-12-01"),("2020","2020-12-01"),("2019","2019-12-05"),("2018","2018-12-06")]
def _wd(iso):
    d=datetime.date.fromisoformat(iso); return d.strftime("%A, %B ")+str(d.day)
WHIST_ROWS="".join(f"<tr><td><b>{y}</b></td><td>{_wd(d)}</td></tr>" for y,d in WHIST)
def wrnav(r,cur):
    L=[(WR,"🎁 Hub: Spotify Wrapped 2026 tracker"),(WRT,"🛠️ Wrapped not showing? Fixes"),(WRA,"🍎 Apple Music Replay 2026"),(WRY,"▶️ YouTube Music Recap 2026")]
    return '<div class="cats" style="margin:14px 0">'+"".join(f'<a href="{r}{p}">{esc(t)}</a>' for p,t in L if p!=cur)+'</div>'
def wrrel(r):
    return f'<h2>More music on Trends Incoming</h2><ul><li><a href="{r}music/grammy-nominations-2027/">2027 Grammy nominations: Monday, Nov 16</a></li><li><a href="{r}music/zach-bryan-2027-tour-tickets/">Zach Bryan 2027 stadium tour tickets</a></li><li><a href="{r}music/charts/">What\'s topping the charts</a></li><li><a href="{r}music/">All music trends</a></li></ul>'
WRCR=[("Home",""),("Music","music/"),("Spotify Wrapped 2026",WR)]
COUNTJS='''<p id="wcd" class="by" aria-live="polite"></p><script>(function(){var t=new Date("2026-12-02T00:00:00-05:00"),n=new Date(),d=Math.ceil((t-n)/864e5),e=document.getElementById("wcd");if(!e)return;e.textContent=d>1?d+" days until our expected date (Wednesday, December 2). Spotify has not confirmed it.":(d==1?"Our expected date is tomorrow. Spotify has not confirmed it.":"We're in the expected window. Check the status box above for the latest.")})();</script>'''
WQ=[("When does Spotify Wrapped 2026 come out?","Spotify hasn't announced the date yet (checked October 19, 2026). Our best guess is Wednesday, December 2, 2026, because every Wrapped since 2021 has dropped on a Wednesday, and the last five landed between November 29 and December 4. Treat it as expected, not confirmed."),
("When does Spotify stop tracking for Wrapped 2026?","Spotify hasn't said for 2026. For 2025, Spotify said Wrapped captured listening from January 1 until mid November, a few weeks before the December 3 launch. So your November streams probably count, but the exact 2026 cutoff isn't confirmed."),
("Does Spotify Wrapped stop counting on October 31?","No, not in 2025. Spotify said the 2025 window ran to mid November. The October 31 cutoff is an old myth."),
("Why can't I see my Spotify Wrapped?","The most common reasons: it hasn't launched yet, your app needs an update, or you didn't meet the eligibility bar. In 2025 you needed at least 30 songs streamed for more than 30 seconds each and at least five different artists. See our Wrapped not showing fixes page for the full checklist."),
("Do Private Mode streams count toward Wrapped?","For 2025, Private Mode listening counted toward your total minutes, but not toward your taste-based stories or the eligibility minimum, per Spotify."),
("When is Apple Music Replay 2026 coming out?","Apple hasn't announced it. Apple Music Replay 2025 dropped December 2, 2025, and earlier editions landed between November 28 and December 3. Monthly Replay stats are already in the Music app all year.")]
WSRC=[S_OC,S_SPMADE,S_SPMETH,S_SPUX,S_SPART,S_SPSUP,S_SPCOM,S_APSUP,S_YTHELP]
WHOW=[("Update the Spotify app","Make sure your Spotify mobile app (iOS or Android) is on the latest version."),("Open Home","Open the app and look for the Wrapped feed at the top of your Home screen."),("Or search for it","Search \u201c2026 Wrapped\u201d in the app if the banner doesn't show up."),("Tap through your stories","Tap through your personalized stories, then save or share the cards you love.")]
wbody=f'''<article><p class="by"><a href="../">🎧 Music</a> › Spotify Wrapped 2026</p><span class="pill">Wrapped Week tracker · checked {FC19}</span>
<h1>Spotify Wrapped 2026 Release Date: When It Drops and How to See Yours</h1><p class="by">{BY} · Published Oct 19, 2026 · Last updated Oct 19, 2026</p>
<p><b>Short answer:</b> Spotify hasn't announced the Wrapped 2026 date yet. Our best guess is <b>Wednesday, December 2, 2026</b> {EXPP}. Every Wrapped since 2021 has dropped on a Wednesday, and the last five all landed between November 29 and December 4. The moment Spotify confirms it, this page flips to the official date. Bookmark it and get your group chat ready. 🎁</p>
<div class="card" style="background:#effcff;margin:14px 0"><h2 style="margin-top:0">📡 Release date tracker</h2><table>
<tr><th>Is Wrapped 2026 out?</th><td>Not yet</td></tr>
<tr><th>Date confirmed by Spotify?</th><td><b>No.</b> Spotify hasn't announced a date (checked {FC19}).</td></tr>
<tr><th>Our expected date</th><td><b>Wednesday, December 2, 2026</b> {EXPP}</td></tr>
<tr><th>Listening cutoff</th><td>Not confirmed for 2026. In 2025 it was <b>January 1 to mid November</b>.</td></tr>
<tr><th>Artist video message deadline</th><td><b>November 6, 2026</b> (Spotify for Artists, official)</td></tr>
<tr><th>Same week</th><td>Apple Music Replay and YouTube's recaps usually land in the same late November to early December stretch</td></tr></table>{COUNTJS}</div>
{wrnav("../../",WR)}
<h2>📅 Why we expect Wednesday, December 2</h2><p>Spotify keeps the date secret until launch morning, so nobody outside Spotify knows for sure. But the pattern is strong. Here's every launch since 2018:</p>
<table><tr><th>Year</th><th>Wrapped launch day</th></tr>{WHIST_ROWS}</table>
<p class="src">Dates from Official Charts; the 2025 date is confirmed by Spotify's own newsroom.</p>
<p>Five Wednesdays in a row, and no launch later than December 4 in the past five years. Wednesday, December 2 fits both. One heads up if you've seen "December 3" floating around: that's a Thursday this year, which would break the Wednesday streak. Could Spotify surprise us? Totally. That's why the date above wears its EXPECTED badge until Spotify says otherwise.</p>
<h2>⏱️ When does Spotify stop tracking for Wrapped?</h2><p>Spotify hasn't confirmed the 2026 cutoff. For 2025, Spotify said Wrapped captured your listening <b>from January 1 until mid November</b>, so it had time to check the data before the December 3 launch. If 2026 works the same way, you've still got a few weeks to push that one artist into your Top 5. Sorry, the October 31 cutoff is a myth.</p>
<p>A couple of 2025 rules worth knowing: a song counts once you've played it for more than 30 seconds, offline listening counts, and white noise and nature sounds get filtered out. Private Mode sessions add to your total minutes but don't shape your taste-based stories.</p>
<h2>📱 How to see your Spotify Wrapped</h2><p>When it goes live, here's how it worked in 2025 (we'll update the steps if Spotify changes anything):</p>
<ol>{"".join(f"<li><b>{esc(a)}.</b> {esc(b)}</li>" for a,b in WHOW)}</ol>
<p>Wrapped was free for both Free and Premium users in nearly every market where Spotify is live. It's a mobile app experience, so open it on your phone.</p>
<div class="card picks" style="margin:14px 0"><span class="pill">Troubleshooting</span><h3>🛠️ Wrapped not showing up?</h3><p>Check the eligibility rules, the update trick, and the other usual suspects.</p><div class="links"><a class="in" href="../../{WRT}">See every fix →</a></div></div>
<h2>🎶 It's Wrapped Week everywhere</h2><div class="grid">
<div class="card"><span class="pill">Expected late Nov to early Dec</span><h3>🍎 Apple Music Replay 2026</h3><p>Monthly stats are already in the Music app. The year-end Replay and highlight reel land around Wrapped time.</p><div class="links"><a class="in" href="../../{WRA}">Find your Replay →</a></div></div>
<div class="card"><span class="pill">Counts Jan 1 to Nov 15</span><h3>▶️ YouTube Music Recap 2026</h3><p>YouTube Music officially counts listening from January 1 to November 15 for the year-end Recap.</p><div class="links"><a class="in" href="../../{WRY}">Find your Recap →</a></div></div></div>
<h2>✅ Confirmed vs ❓ not confirmed</h2><ul><li>✅ Artists can submit Wrapped video messages until <b>November 6, 2026</b>.</li><li>✅ 2025 Wrapped launched December 3, 2025 and counted listening from January 1 to mid November.</li><li>❓ The 2026 launch date.</li><li>❓ The 2026 listening cutoff.</li><li>❓ The 2026 eligibility rules and new features.</li></ul>
{fhtml(WQ)}{wrrel("../../")}{srcl(WSRC)}</article>'''
WTITLE="Spotify Wrapped 2026 Release Date: When It Drops and How to See Yours"
WDESC="The expected Spotify Wrapped 2026 release date, when listening stops counting, and how to find your Wrapped, Apple Music Replay and YouTube Music Recap. Updated the minute it goes live."
wev={"@context":"https://schema.org","@type":"Event","name":"Spotify Wrapped 2026 release (expected date, not confirmed by Spotify)","description":"Expected launch of Spotify Wrapped 2026. Spotify has not announced the date; December 2, 2026 is the Trends Incoming estimate based on past Wednesday launches. This will be updated when Spotify confirms.","startDate":W_EXP,"eventAttendanceMode":"https://schema.org/OnlineEventAttendanceMode","location":{"@type":"VirtualLocation","url":"https://open.spotify.com/"},"organizer":{"@type":"Organization","name":"Spotify","url":"https://www.spotify.com/"},"url":B+"/"+WR,"isAccessibleForFree":True}
whowld={"@context":"https://schema.org","@type":"HowTo","name":"How to see your Spotify Wrapped","step":[{"@type":"HowToStep","position":i+1,"name":a,"text":b} for i,(a,b) in enumerate(WHOW)]}
page(WR+"index.html",WTITLE,WDESC,wbody,ld=[art19(WTITLE,WDESC,WR,WSRC,"Spotify Wrapped 2026"),wev,whowld,faqld(WQ),crumbs(WRCR)],article=False,cat="music")
# ---- troubleshooting ----
TQ=[("Why is my Spotify Wrapped not showing?","Check four things: Wrapped has actually launched, your app is updated, you're on the mobile app, and you met the eligibility bar. In 2025 that meant at least 30 songs streamed for more than 30 seconds each and at least five different artists."),
("Do Private Mode streams count toward Wrapped eligibility?","Not in 2025. Spotify said streams from Private Mode, or from songs and playlists you've excluded from your Taste Profile, didn't count toward the eligibility minimum."),
("Can I see Spotify Wrapped on desktop?","In 2025, Spotify pointed people to the mobile app on iOS and Android. If you're on a computer, grab your phone."),
("How long does Spotify Wrapped stay available?","It's a limited-time campaign. The 2025 Wrapped campaign ended on January 16, 2026, per Spotify's community team. Save or share your favorite cards early.")]
TSRC=[S_SPUX,S_SPMETH,S_SPSUP,S_SPCOM,S_OC]
TFIX=[("Is it actually out yet?","Wrapped 2026 hasn't launched (checked October 19, 2026). If it isn't launch day yet, there's nothing to find. Our hub tracks the date."),
("Update the app","Spotify's own advice for 2025 was to make sure your app is up to date. Update Spotify from the App Store or Google Play, then reopen it."),
("Use your phone","Wrapped lives in the Spotify mobile app on iOS and Android. Look for the Wrapped feed at the top of Home."),
("Search for it","Type \u201c2026 Wrapped\u201d into Spotify search. In 2025, searching \u201c2025 Wrapped\u201d opened the experience."),
("Check you're eligible","For 2025 you needed at least 30 songs streamed for more than 30 seconds each, and at least five different artists. Private Mode streams and anything excluded from your Taste Profile didn't count toward that minimum."),
("Make sure it's your account","Family or shared phone? Check you're logged in to the account you actually listen on, since Wrapped is per account."),
("Restart, then log out and back in","Fully close the app, reopen it, and if that doesn't work, log out and back in. It's the classic fix for a missing banner on launch day."),
("Check for known issues","On launch day, Spotify's community team posts known problems in its Ongoing Issues board. If lots of people are stuck, it's on Spotify's end and usually clears up."),
("Don't wait too long","Wrapped is a limited-time campaign. The 2025 stories stopped being available on January 16, 2026.")]
tbody=f'''<article><p class="by"><a href="../../">🎧 Music</a> › <a href="../">Spotify Wrapped 2026</a> › Wrapped not showing</p><span class="pill">Troubleshooting · checked {FC19}</span>
<h1>Spotify Wrapped Not Showing? 9 Fixes That Actually Work</h1><p class="by">{BY} · Published Oct 19, 2026 · Last updated Oct 19, 2026</p>
<p><b>Short answer:</b> nine times out of ten it's one of three things: Wrapped isn't out yet, your app needs an update, or you didn't hit the eligibility bar. Here's the full checklist, built from Spotify's own 2025 rules. We'll update it the day Wrapped 2026 drops, which we expect on Wednesday, December 2 {EXPP}.</p>
{wrnav("../../../",WRT)}
<h2>🛠️ The checklist</h2><ol>{"".join(f"<li><b>{esc(a)}</b> {esc(b)}</li>" for a,b in TFIX)}</ol>
<h2>📏 The 2025 eligibility rules at a glance</h2><table><tr><th>Minimum songs</th><td>30 songs streamed for more than 30 seconds each</td></tr><tr><th>Minimum artists</th><td>5 different artists</td></tr><tr><th>Doesn't count toward the minimum</th><td>Private Mode streams; songs and playlists excluded from your Taste Profile</td></tr><tr><th>Who gets it</th><td>Free and Premium users in nearly all markets where Spotify is live</td></tr><tr><th>Where</th><td>Spotify mobile app (iOS and Android)</td></tr></table>
<p class="src">From Spotify's 2025 Wrapped announcement. Spotify hasn't published 2026 rules yet.</p>
<h2>😬 Wrapped looks wrong?</h2><p>Spotify explained some of the surprises in 2025: Top Songs rank by number of listens (a listen is more than 30 seconds), Top Artists use a weighted count that favors primary artists over features, and the year stops in mid November. Sleep sounds and white noise get filtered out. If your kid's bedtime playlist crashed your Wrapped, Private Mode or Exclude from Taste Profile is your friend next year.</p>
<p>Want the other recaps too? <a href="../apple-music-replay-2026/">Apple Music Replay 2026</a> and <a href="../youtube-music-recap-2026/">YouTube Music Recap 2026</a> have their own fixes.</p>
{fhtml(TQ)}{wrrel("../../../")}{srcl(TSRC)}</article>'''
TTITLE="Spotify Wrapped Not Showing? 9 Fixes for Wrapped 2026"
TDESC="Why your Spotify Wrapped isn't showing and how to fix it: launch timing, app updates, the 30 songs and 5 artists rule, Private Mode and more, from Spotify's own rules."
page(WRT+"index.html",TTITLE,TDESC,tbody,ld=[art19(TTITLE,TDESC,WRT,TSRC,"Spotify Wrapped troubleshooting"),{"@context":"https://schema.org","@type":"HowTo","name":"How to fix Spotify Wrapped not showing","step":[{"@type":"HowToStep","position":i+1,"name":a,"text":b} for i,(a,b) in enumerate(TFIX)]},faqld(TQ),crumbs(WRCR+[("Wrapped not showing",WRT)])],article=False,cat="music")
# ---- Apple Music Replay ----
AQ=[("When does Apple Music Replay 2026 come out?","Apple hasn't announced a date. The year-end Replay dropped December 2, 2025, December 3, 2024, November 28, 2023 and November 29, 2022, so late November to early December is the safe bet. Monthly Replay stats are available in the Music app all year."),
("How do I see my Apple Music Replay?","In the Music app, go to Home, scroll to Replay: Your Top Music and tap Go back in time. On the web, go to replay.music.apple.com, sign in with the Apple Account you use for Apple Music and tap Jump In."),
("Why don't I see Apple Music Replay?","Apple says to make sure Use Listening History is turned on for all your devices. You'll get a notification once you've played enough music for Replay to be ready."),
("Do I need an Apple Music subscription for Replay?","Replay is built from your Apple Music listening history, and Apple says to sign in with the same Apple Account you use with your Apple Music subscription.")]
ASRC=[S_APSUP,S_APUSA,S_APAP]
APH=[("2025","December 2"),("2024","December 3"),("2023","November 28"),("2022","November 29")]
abody=f'''<article><p class="by"><a href="../../">🎧 Music</a> › <a href="../">Spotify Wrapped 2026</a> › Apple Music Replay 2026</p><span class="pill">Year-end date not announced · checked {FC19}</span>
<h1>Apple Music Replay 2026: How to Find Your Year in Music</h1><p class="by">{BY} · Published Oct 19, 2026 · Last updated Oct 19, 2026</p>
<p><b>Short answer:</b> good news, you don't have to wait for all of it. Apple Music Replay now shows your top songs, artists and albums <b>every month</b> in the Music app. The big year-end Replay and highlight reel usually land in <b>late November or early December</b> {EXPP}. Apple hasn't announced the 2026 date yet.</p>
{wrnav("../../../",WRA)}
<h2>📅 Year-end Replay release history</h2><table><tr><th>Year</th><th>Year-end Replay</th></tr>{"".join(f"<tr><td><b>{a}</b></td><td>{b}</td></tr>" for a,b in APH)}</table><p class="src">As reported by USA Today and AP. Apple doesn't pre-announce the date.</p>
<h2>📱 How to see Apple Music Replay in the app</h2><ol><li>Update your iPhone, iPad or Android to the latest OS.</li><li>Open the Music app and go to <b>Home</b>.</li><li>Scroll down to <b>Replay: Your Top Music</b>.</li><li>Tap <b>Go back in time</b> to open your listening stats.</li></ol>
<h2>💻 How to see it on the web</h2><ol><li>Go to <b>replay.music.apple.com</b> on any phone or computer.</li><li>Sign in with the same Apple Account you use for Apple Music.</li><li>Tap or click <b>Jump In</b>.</li></ol>
<h2>✨ What you get</h2><ul><li><b>Monthly insights:</b> top songs, artists and albums by plays and time listened, plus milestones.</li><li><b>Year-end Replay:</b> top songs, artists, albums, genres, playlists and stations at the end of the calendar year.</li><li><b>Highlight reel:</b> an audio and visual recap you can share as a video.</li><li><b>Top listener badges:</b> Apple tells you if you're in the top 100, 500 or 1,000 listeners of an artist or genre.</li><li><b>Your Replay playlist:</b> updated weekly, plus an All Time playlist and past years.</li></ul>
<h2>🛠️ Replay not showing?</h2><p>Apple's fix: turn on <b>Use Listening History</b> on every device. On iPhone or iPad it's Settings > Apps > Music. On a Mac, open Music > Settings > General. On Android, tap More > Settings in the Apple Music app. Once you've played enough music, Apple sends a notification that Replay is ready.</p>
<p>Also on Spotify? Track the <a href="../">Spotify Wrapped 2026 release date</a>, and if it doesn't show, here are the <a href="../wrapped-not-showing/">Wrapped fixes</a>.</p>
{fhtml(AQ)}{wrrel("../../../")}{srcl(ASRC)}</article>'''
ATITLE="Apple Music Replay 2026: How to Find Your Year in Music"
ADESC="When Apple Music Replay 2026 lands, how to see your monthly and year-end Replay in the app or on the web, and what to do if Replay isn't showing."
page(WRA+"index.html",ATITLE,ADESC,abody,ld=[art19(ATITLE,ADESC,WRA,ASRC,"Apple Music Replay 2026"),{"@context":"https://schema.org","@type":"HowTo","name":"How to see your Apple Music Replay","step":[{"@type":"HowToStep","position":1,"text":"Open the Music app and go to Home."},{"@type":"HowToStep","position":2,"text":"Scroll down to Replay: Your Top Music."},{"@type":"HowToStep","position":3,"text":"Tap Go back in time to open your listening stats."}]},faqld(AQ),crumbs(WRCR+[("Apple Music Replay 2026",WRA)])],article=False,cat="music")
# ---- YouTube Music Recap ----
YQ=[("When does YouTube Music Recap 2026 come out?","YouTube hasn't announced it. The 2025 YouTube Music Recap started rolling out around November 24, 2025, and YouTube's broader YouTube Recap launched December 2, 2025. Expect late November to early December."),
("What listening counts toward YouTube Music Recap?","YouTube says the end-of-year Recap uses music listening from January 1 to November 15, across YouTube platforms."),
("How much do I need to listen to get a YouTube Music Recap?","At least 10 hours of music listening from January 1 to November 15, plus at least 5 songs with repeat listens, per YouTube Music Help. Seasonal Recaps need 4 hours per season."),
("Why don't I have a YouTube Music Recap?","Common reasons: your watch history was paused, you have auto-delete set for activity older than 3 months, you mostly listen to made-for-kids music, or you didn't hit the listening minimum.")]
YSRC=[S_YTHELP,S_YTBLOG,S_9TO5,S_APAP]
ybody=f'''<article><p class="by"><a href="../../">🎧 Music</a> › <a href="../">Spotify Wrapped 2026</a> › YouTube Music Recap 2026</p><span class="pill">Counts Jan 1 to Nov 15 · checked {FC19}</span>
<h1>YouTube Music Recap 2026: When It Drops and How to Find Yours</h1><p class="by">{BY} · Published Oct 19, 2026 · Last updated Oct 19, 2026</p>
<p><b>Short answer:</b> YouTube Music counts your listening from <b>January 1 to November 15</b> for the year-end Recap, officially. The 2025 Recap started rolling out around November 24, so late November is a solid guess for 2026 {EXPP}. Here's how to find it and how to make sure you qualify.</p>
{wrnav("../../../",WRY)}
<table><tr><th>Listening window (official)</th><td>January 1 to November 15</td></tr><tr><th>Minimum listening</th><td>10 hours of music, plus 5 songs with repeat listens</td></tr><tr><th>2025 rollout</th><td>Around November 24, 2025 (YouTube Music); YouTube Recap followed December 2</td></tr><tr><th>2026 date</th><td>Not announced {EXPP}</td></tr></table>
<h2>📱 How to find your YouTube Music Recap</h2><ol><li>Sign in to the <b>YouTube Music</b> app.</li><li>Tap your <b>profile photo</b>, then <b>Your Recap</b>.</li><li>Tap <b>Get your Recap</b>. You can download or share the stories.</li></ol>
<p>In the main YouTube app, YouTube Recap shows up under the <b>You</b> tab. If you're eligible for both, the last card offers <b>Get your Music Recap</b>, which jumps you to the full Music Recap. Seeing "Nothing to hear here"? Your 2026 Recap isn't ready yet.</p>
<h2>🛠️ Recap missing? Check these</h2><ul><li><b>Watch history:</b> if it was paused during January 1 to November 15, that listening isn't included.</li><li><b>Auto-delete:</b> an auto-delete setting for activity older than 3 months can wipe out your Recap. Turning it off late may not bring it back.</li><li><b>Kids content:</b> Recap isn't available if you mostly listen to made-for-kids music or podcasts.</li><li><b>Not enough listening:</b> you need 10 hours of music in the window.</li></ul>
<p>Comparing recaps with friends? Track the <a href="../">Spotify Wrapped 2026 date</a> and <a href="../apple-music-replay-2026/">Apple Music Replay 2026</a>.</p>
{fhtml(YQ)}{wrrel("../../../")}{srcl(YSRC)}</article>'''
YTITLE="YouTube Music Recap 2026: Release Date and How to Find It"
YDESC="YouTube Music Recap 2026 counts listening from Jan 1 to Nov 15. When it rolls out, how to find Your Recap, the 10 hour rule and fixes if it's missing."
page(WRY+"index.html",YTITLE,YDESC,ybody,ld=[art19(YTITLE,YDESC,WRY,YSRC,"YouTube Music Recap 2026"),faqld(YQ),crumbs(WRCR+[("YouTube Music Recap 2026",WRY)])],article=False,cat="music")
LM.update({B+"/"+p:PUB19 for p in (WR,WRT,WRA,WRY)})
WRAPLINK='<div class="card picks" style="margin:14px 0"><span class="pill">Expected Wed Dec 2</span><h3>🎁 Spotify Wrapped 2026 release date tracker</h3><p>When Wrapped drops, when tracking stops, and how to fix it if yours doesn\'t show. Plus Apple Music Replay and YouTube Music Recap.</p><div class="links"><a class="in" href="{r}music/spotify-wrapped-2026/">Open the tracker →</a><a class="in" href="{r}music/spotify-wrapped-2026/wrapped-not-showing/">Wrapped not showing? →</a></div></div>'
SUBX["charts"]='<p>Wondering where your own year lands? Track the <a href="../spotify-wrapped-2026/">Spotify Wrapped 2026 release date</a>, plus <a href="../spotify-wrapped-2026/apple-music-replay-2026/">Apple Music Replay</a> and <a href="../spotify-wrapped-2026/youtube-music-recap-2026/">YouTube Music Recap</a>.</p>'
