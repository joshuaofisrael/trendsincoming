# --- 2027 tax numbers hub: brackets + calculator, 401k/IRA, HSA, mileage (added 2026-10-18). exec'd from build.py ---
PUB18="2026-10-18"; MOD18="2026-10-18"
TX="money/2027-tax-numbers/"
TXB=TX+"2027-tax-brackets/"; TXK=TX+"401k-ira-limits-2027/"; TXH=TX+"hsa-limits-2027/"; TXM=TX+"irs-mileage-rate-2027/"; TXG=TX+"gift-estate-tax-2027/"
PB="money/medicare-part-b-premium-2027/"
PUB18B="2026-11-18"
S_RP2532=("IRS Rev. Proc. 2025-32: 2026 inflation adjustments (tax tables, standard deduction)","https://www.irs.gov/pub/irs-drop/rp-25-32.pdf")
S_IR103=("IRS IR-2025-103: tax year 2026 inflation adjustments (Oct 9, 2025)","https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2026-including-amendments-from-the-one-big-beautiful-bill")
S_PGP=("IRS 2026 to 2027 priority guidance plan (lists the 2027 inflation revenue procedure for October 2026)","https://www.irs.gov/pub/irs-counsel/2026-2027-initial-pgp.pdf")
S_NEWS=("IRS newsroom: news releases for the current month","https://www.irs.gov/newsroom/news-releases-for-current-month")
S_TR=("Thomson Reuters Checkpoint: projected 2027 figures (Sep 11, 2026, estimates, not IRS)","https://tax.thomsonreuters.com/news/key-2027-figures-calculated-by-thomson-reuters-checkpoint-based-on-inflation-data-now-available/")
S_WK=("Wolters Kluwer: projected 2027 federal tax brackets (estimates, not IRS)","https://www.wolterskluwer.com/en/expert-insights/projected-2027-federal-tax-brackets")
S_IR111=("IRS IR-2025-111: 401(k) limit increases to $24,500 for 2026, IRA limit increases to $7,500","https://www.irs.gov/newsroom/401k-limit-increases-to-24500-for-2026-ira-limit-increases-to-7500")
S_N2567=("IRS Notice 2025-67: 2026 retirement plan cost-of-living adjustments","https://www.irs.gov/pub/irs-drop/n-25-67.pdf")
S_IRA=("IRS: IRA contribution limits","https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-topics-ira-contribution-limits")
S_401=("IRS: 401(k) and profit-sharing plan contribution limits","https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-topics-401k-and-profit-sharing-plan-contribution-limits")
S_MIL=("Milliman: 2027 IRS limits, final estimates (Oct 15, 2026, estimates, not IRS)","https://www.milliman.com/en/insight/2027-irs-limits-forecast-final-estimates")
S_IR133=("IRS IR-2026-133: tax year 2027 inflation adjustments (Nov 5, 2026, official)","https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2027-taxpayers-continue-to-benefit-from-the-working-families-tax-cuts")
S_RP2635=("IRS Rev. Proc. 2026-35: 2027 inflation adjustments (official)","https://www.irs.gov/pub/irs-drop/rp-26-35.pdf")
S_IR136=("IRS IR-2026-136: 401(k) limit increases to $25,500 for 2027 (Nov 12, 2026, official)","https://www.irs.gov/newsroom/401k-limit-increases-to-25500-for-2027-ira-limit-remains-7500")
S_N2666=("IRS Notice 2026-66: 2027 retirement plan cost-of-living adjustments (official)","https://www.irs.gov/pub/irs-drop/n-26-66.pdf")
S_RP2624=("IRS Rev. Proc. 2026-24: 2027 HSA and HDHP amounts (official)","https://www.irs.gov/pub/irs-drop/rp-26-24.pdf")
S_IRB2625=("Internal Revenue Bulletin 2026-25 (publishes Rev. Proc. 2026-24)","https://www.irs.gov/irb/2026-25_irb")
S_RP2519=("IRS Rev. Proc. 2025-19: 2026 HSA and HDHP amounts","https://www.irs.gov/pub/irs-drop/rp-25-19.pdf")
S_P969=("IRS Publication 969: Health Savings Accounts","https://www.irs.gov/publications/p969")
S_MILE=("IRS: standard mileage rates (all years)","https://www.irs.gov/tax-professionals/standard-mileage-rates")
S_IR128=("IRS IR-2025-128: 2026 business rate 72.5 cents (Dec 29, 2025)","https://www.irs.gov/newsroom/irs-sets-2026-business-standard-mileage-rate-at-725-cents-per-mile-up-25-cents")
S_N2610=("IRS Notice 2026-10: 2026 standard mileage rates","https://www.irs.gov/pub/irs-drop/n-26-10.pdf")
S_IRB2629=("Internal Revenue Bulletin 2026-29: Announcement 2026-11, rates raised from July 1, 2026","https://www.irs.gov/irb/2026-29_irb")
NOADV='<div class="warn"><b>No personal tax advice.</b> This page is general information from official IRS releases. Numbers marked <b>projected</b> are estimates, not IRS figures. Trends Incoming is not a tax preparer, and nothing here is tax, legal or financial advice for your situation. Check IRS.gov or a qualified tax professional before you act.</div>'
PROJ='<span class="pill" style="background:#ff4fa3;color:#fff">PROJECTED</span>'
OFF='<span class="pill" style="background:#1a7f37;color:#fff">OFFICIAL IRS</span>'
def taxnav(r,cur):
    L=[(TX,"🧾 Hub: all 2027 tax numbers"),(TXB,"📊 2027 tax brackets and standard deduction"),(TXB+"#calculator","🧮 Bracket calculator"),(TXK,"🏦 401(k) and IRA limits 2027"),(TXH,"🩺 HSA limits 2027"),(TXG,"🎁 Gift and estate tax 2027"),(TXM,"🚗 IRS mileage rate 2027")]
    return '<div class="cats" style="margin:14px 0">'+"".join(f'<a href="{r}{p}">{esc(t)}</a>' for p,t in L if p!=cur)+'</div>'
def taxrel(r):
    return f'<h2>Related on Trends Incoming</h2><ul><li><a href="{r}money/social-security-2027/">Social Security 2027: 3.6% COLA calculator and payment dates</a></li><li><a href="{r}{PB}">Medicare Part B premium 2027: $209.40 a month (official)</a></li><li><a href="{r}money/medicare-open-enrollment-2027/">Medicare open enrollment 2027 (Oct 15 to Dec 7)</a></li><li><a href="{r}money/open-enrollment-2027/">HealthCare.gov open enrollment 2027 (Nov 1 to Jan 15)</a></li><li><a href="{r}money/minimum-wage-2027/">Minimum wage 2027 by state: every January 1 raise</a></li><li><a href="{r}money/retirement/">Retirement and Social Security trends</a></li></ul>'
def taxart(title,desc,path,cites):
    return {"@context":"https://schema.org","@type":"Article","headline":title,"description":desc,"datePublished":PUB18,"dateModified":MOD18,"mainEntityOfPage":B+"/"+path,"author":{"@type":"Organization","name":"The Trends Incoming team","url":B+"/about/"},"publisher":pub,"citation":[u for _,u in cites],"about":{"@type":"Thing","name":"US federal tax numbers for 2027"}}
TXCR=[("Home",""),("Money","money/"),("2027 tax numbers",TX)]
def mny(n): return f"${n:,}"
# ---- bracket data (2026 official: Rev. Proc. 2025-32; 2027 projected: Thomson Reuters Checkpoint, Sep 11, 2026) ----
RATES=[10,12,22,24,32,35,37]
ST=[("single","Single"),("mfj","Married filing jointly / surviving spouse"),("hoh","Head of household"),("mfs","Married filing separately")]
B26={"single":[12400,50400,105700,201775,256225,640600],"mfj":[24800,100800,211400,403550,512450,768700],"hoh":[17700,67450,105700,201750,256200,640600],"mfs":[12400,50400,105700,201775,256225,384350]}
B27={"single":[12800,52025,109125,208325,264550,661375],"mfj":[25600,104050,218250,416650,529100,793650],"hoh":[18250,69650,109100,208300,264550,661350],"mfs":[12800,52025,109125,208325,264550,396825]}
SD26={"single":16100,"mfj":32200,"hoh":24150,"mfs":16100}; SD27={"single":16600,"mfj":33200,"hoh":24925,"mfs":16600}
def brows(bk):
    out=""
    for i,r in enumerate(RATES):
        lo=0 if i==0 else bk[i-1]
        rng=(f"$0 to {mny(bk[0])}" if i==0 else (f"Over {mny(lo)}" if i==6 else f"{mny(lo)} to {mny(bk[i])}"))
        out+=f"<tr><td><b>{r}%</b></td><td>{rng}</td></tr>"
    return out
def btable(key,label,b,cap):
    return f'<h3>{esc(label)}</h3><table><caption class="src" style="caption-side:bottom;text-align:left">{cap}</caption><tr><th>Rate</th><th>Taxable income</th></tr>{brows(b[key])}</table>'
def sidebyside(key,label):
    rows=""
    for i,r in enumerate(RATES):
        def rg(bk):
            return (f"Up to {mny(bk[0])}" if i==0 else (f"Over {mny(bk[5])}" if i==6 else f"{mny(bk[i-1])} to {mny(bk[i])}"))
        rows+=f"<tr><td><b>{r}%</b></td><td>{rg(B26[key])}</td><td>{rg(B27[key])}</td></tr>"
    return f'<h3>{esc(label)}</h3><table><tr><th>Rate</th><th>2026 {OFF}</th><th>2027 {OFF}</th></tr>{rows}</table>'
CALCDATA=json.dumps({"2026":{"b":B26,"sd":SD26,"lab":"2026 official IRS brackets"},"2027":{"b":B27,"sd":SD27,"lab":"2027 official IRS brackets (Rev. Proc. 2026-35)"}})
CALCJS="""<script>(function(){var D=__D__,R=[0.10,0.12,0.22,0.24,0.32,0.35,0.37];
var y=document.getElementById("ty"),s=document.getElementById("tst"),i=document.getElementById("tinc"),c=document.getElementById("tsd"),o=document.getElementById("tres"),b=document.getElementById("tgo");
function f(n){return n.toLocaleString("en-US",{style:"currency",currency:"USD",maximumFractionDigits:0})}
function go(){var v=parseFloat(i.value),d=D[y.value],bk=d.b[s.value];if(!(v>=0)||i.value===""){o.textContent="Type an income amount to see your bracket.";return}
var ti=c.checked?Math.max(0,v-d.sd[s.value]):v,t=0,lo=0,top=R[0];
for(var k=0;k<7;k++){var hi=k<6?bk[k]:Infinity;if(ti>lo){t+=(Math.min(ti,hi)-lo)*R[k];top=R[k]}lo=hi;if(ti<=hi)break}
var eff=ti>0?(t/ti*100):0;
o.innerHTML="<b>"+d.lab+"</b><br>Taxable income used: "+f(ti)+(c.checked?" (after a "+f(d.sd[s.value])+" standard deduction)":"")+"<br>Top bracket: <b>"+Math.round(top*100)+"%</b><br>Estimated regular federal income tax before credits: <b>"+f(Math.round(t))+"</b><br>Average rate on taxable income: "+eff.toFixed(1)+"%<br><small>Estimate only, not tax advice. Leaves out credits, capital gains and qualified dividend rates, AMT, payroll and state taxes.</small>"}
b.addEventListener("click",go);i.addEventListener("keydown",function(e){if(e.key==="Enter"){e.preventDefault();go()}});[y,s,c].forEach(function(x){x.addEventListener("change",function(){if(i.value!=="")go()})})})();</script>""".replace("__D__",CALCDATA)
SEL='style="font:inherit;padding:6px 10px;border:2px solid #16121f;border-radius:10px;margin:6px 0"'
CALC=f'''<div class="card" id="calculator" style="background:#effcff;margin:14px 0"><h2 style="margin-top:0">🧮 What bracket am I in? Quick calculator</h2>
<p class="warn" style="margin-top:6px"><b>Estimate only, not personal tax advice.</b> It runs in your browser and nothing is sent anywhere. The 2027 option uses projected brackets until the IRS publishes the official ones.</p>
<form id="taxcalc" onsubmit="return false"><label for="ty"><b>Tax year</b></label><br><select id="ty" {SEL}><option value="2026">2026 (official IRS)</option><option value="2027">2027 (projected)</option></select><br>
<label for="tst"><b>Filing status</b></label><br><select id="tst" {SEL}>{"".join(f'<option value="{k}">{esc(v)}</option>' for k,v in ST)}</select><br>
<label for="tinc"><b>Income ($)</b></label><br><input id="tinc" type="number" min="0" max="100000000" step="1" inputmode="numeric" placeholder="e.g. 85000" {SEL.replace('margin:6px 0','margin:6px 0;width:12em')}><br>
<label><input type="checkbox" id="tsd" checked> Subtract the standard deduction for me (uncheck if you typed taxable income)</label><br>
<button type="button" id="tgo" style="font:inherit;font-weight:800;border:2px solid #16121f;border-radius:10px;background:#ffd60a;padding:6px 14px;cursor:pointer;margin-top:8px">Show my bracket</button>
<p id="tres" aria-live="polite" style="font-size:1.02rem;margin-top:10px"></p></form></div>{CALCJS}'''
# ---------------- brackets page ----------------
BQ=[("What are the 2027 tax brackets?","Official since November 5, 2026 (IRS IR-2026-133, Rev. Proc. 2026-35). The seven rates stay 10%, 12%, 22%, 24%, 32%, 35% and 37%, as set by permanent law. For single filers the 10% bracket runs up to $12,800 and the 37% rate starts above $661,375; for married filing jointly it's up to $25,600 and above $793,650. Full table below."),
("What is the standard deduction for 2027?","Official: $16,600 for single filers and married filing separately, $33,200 for married filing jointly, and $24,925 for head of household, per Rev. Proc. 2026-35. The 2026 amounts were $16,100, $32,200 and $24,150."),
("When did the IRS announce the 2027 tax brackets?","November 5, 2026, in news release IR-2026-133 and Revenue Procedure 2026-35, covering almost 70 tax provisions for tax year 2027."),
("What are the 2027 tax brackets for married filing jointly?","Official: 10% up to $25,600; 12% to $104,050; 22% to $218,250; 24% to $416,650; 32% to $529,100; 35% to $793,650; 37% above that, per Rev. Proc. 2026-35."),
("Do the 2026 or 2027 brackets apply to the return I file in 2027?","The 2026 brackets. The IRS says the tax year 2026 amounts generally apply to returns filed in 2027. The 2027 brackets apply to returns filed in 2028."),
("Does moving into a higher bracket mean all my income is taxed at that rate?","No. Each rate applies only to the slice of taxable income inside its range. That's why your average rate is always lower than your top bracket.")]
def bsd():
    return f'<table><tr><th>Filing status</th><th>2026 {OFF}</th><th>2027 {OFF}</th></tr><tr><td>Single; married filing separately</td><td>$16,100</td><td>$16,600</td></tr><tr><td>Married filing jointly; surviving spouse</td><td>$32,200</td><td>$33,200</td></tr><tr><td>Head of household</td><td>$24,150</td><td>$24,925</td></tr><tr><td>Extra for age 65+ or blind, married</td><td>$1,650</td><td>$1,700</td></tr><tr><td>Extra for age 65+ or blind, unmarried</td><td>$2,050</td><td>$2,100</td></tr></table>'
BSRC=[S_IR133,S_RP2635,S_RP2532,S_IR103]
bbody=f'''<article><p class="by"><a href="../../">💵 Money</a> › <a href="../">2027 tax numbers</a> › 2027 tax brackets</p><span class="pill" style="background:#1a7f37;color:#fff">Official since Nov 5, 2026</span>
<h1>2027 Tax Brackets and Standard Deduction (IRS Official Numbers)</h1><p class="by">{BY} · Published Oct 18, 2026 · Last updated Nov 18, 2026</p>
<p><b>Short answer:</b> it's official. On <b>November 5, 2026</b> the IRS released the 2027 tax brackets and standard deduction in news release <b>IR-2026-133</b> and <b>Revenue Procedure 2026-35</b>. The seven rates are unchanged by law; only the income thresholds moved up with inflation. Here are the full official 2026 and 2027 numbers, plus a calculator.</p>
{NOADV}
<table><tr><th>2027 brackets and standard deduction</th><td>{OFF} IRS IR-2026-133 / Rev. Proc. 2026-35, Nov 5, 2026</td></tr><tr><th>Tax rates</th><td>10%, 12%, 22%, 24%, 32%, 35%, 37% (permanent law, unchanged)</td></tr><tr><th>2027 standard deduction, single</th><td>$16,600 (2026: $16,100)</td></tr><tr><th>2027 standard deduction, joint</th><td>$33,200 (2026: $32,200)</td></tr><tr><th>2027 standard deduction, head of household</th><td>$24,925 (2026: $24,150)</td></tr></table>
{taxnav("../../../",TXB)}
{CALC}
<h2>📊 2026 vs 2027 tax brackets, side by side</h2><p>Both years are now official: 2026 from IRS Rev. Proc. 2025-32, 2027 from IRS Rev. Proc. 2026-35 (Nov 5, 2026). Taxable income is income after deductions.</p>
{"".join(sidebyside(k,l) for k,l in ST)}
<h2>💵 Standard deduction: 2026 vs 2027, both official</h2>{bsd()}
<p>Also still in effect for 2025 through 2028: a separate senior deduction of up to $6,000 per person age 65 or older, phased down above $75,000 of modified AGI ($150,000 joint). It sits on top of the standard deduction above.</p>
<h2>🔍 How the inflation adjustment works</h2><p>Brackets and the standard deduction are indexed to inflation by law (Internal Revenue Code section 1(f)). The IRS compares the chained consumer price index (C-CPI-U) for a 12-month base period with a prior base year, then rounds each increase down to the next $50 ($25 for single and married filing separately brackets). Rev. Proc. 2026-35 is the IRS's own calculation under that formula, so these figures are final, not an estimate.</p>
<h2>🧾 Worked example (2026, official)</h2><p>A single filer with $60,000 of taxable income in 2026 pays 10% on the first $12,400 ($1,240), 12% on the next $38,000 ($4,560) and 22% on the last $9,600 ($2,112). Total: <b>$7,912</b> before credits. That matches the IRS table: $5,800 plus 22% of the amount over $50,400. Top bracket 22%, average rate about 13.2%.</p>
<h2>📅 Where the rest of the 2027 numbers stand</h2><ul><li><b>Brackets and standard deduction:</b> official (IR-2026-133, Nov 5, 2026).</li><li><b>401(k) and IRA limits:</b> official (IR-2026-136, Nov 12, 2026). See our <a href="../401k-ira-limits-2027/">401(k) and IRA limits page</a>.</li><li><b>HSA limits:</b> official at $4,500 and $9,000. See <a href="../hsa-limits-2027/">HSA limits 2027</a>.</li><li><b>Gift and estate tax:</b> official (IR-2026-133, Nov 5, 2026). See <a href="../gift-estate-tax-2027/">gift and estate tax 2027</a>.</li><li><b>Mileage rate:</b> still not announced; IRS notice expected in December 2026. See <a href="../irs-mileage-rate-2027/">IRS mileage rate 2027</a>.</li></ul>
{fhtml(BQ)}{taxrel("../../../")}{srclist(BSRC)}</article>'''
BTITLE="2027 Tax Brackets and Standard Deduction (IRS Official Numbers)"
BDESC="Official IRS 2027 tax brackets and standard deduction (IR-2026-133, Nov 5, 2026) for every filing status, with 2026 numbers and a bracket calculator."
def dsetld():
    return {"@context":"https://schema.org","@type":"Dataset","name":"US federal income tax brackets and standard deduction, 2026 and 2027, both official","description":"Taxable income thresholds for the seven federal income tax rates by filing status. 2026 values are from IRS Rev. Proc. 2025-32. 2027 values are official, from IRS Rev. Proc. 2026-35 (Nov 5, 2026).","url":B+"/"+TXB,"creator":{"@type":"Organization","name":"The Trends Incoming team","url":B+"/about/"},"isBasedOn":[S_RP2532[1],S_RP2635[1]],"temporalCoverage":"2026/2027","spatialCoverage":"United States","isAccessibleForFree":True,"dateModified":PUB18B,"variableMeasured":["Tax rate","Taxable income threshold","Standard deduction"]}
bld=[taxart(BTITLE,BDESC,TXB,BSRC),dsetld(),faqld(BQ),crumbs(TXCR+[("2027 tax brackets",TXB)])]
page(TXB+"index.html",BTITLE,BDESC,bbody,ld=bld,article=False,cat="money")
# ---------------- 401k / IRA ----------------
KQ=[("How much can I put in my 401(k) in 2027?","$25,500, per IRS news release IR-2026-136 (Nov 12, 2026) and Notice 2026-66. That's up $1,000 from the official 2026 limit of $24,500."),
("What is the 401(k) catch-up limit for 2027?","Official: $8,500 for ages 50 and older and $11,750 for ages 60 to 63, per IR-2026-136. Official 2026 amounts were $8,000 and $11,250."),
("What is the IRA contribution limit for 2027?","$7,500, unchanged from 2026, per IR-2026-136. The catch-up for age 50 and older is $1,100, also unchanged."),
("When did the IRS announce 2027 401(k) limits?","November 12, 2026, in news release IR-2026-136 and Notice 2026-66."),
("What is the total 401(k) limit including employer contributions for 2027?","Official: $75,000 for employee plus employer additions combined, up from $72,000 in 2026, per Notice 2026-66 (Internal Revenue Code section 415(c)(1)(A)). Catch-up contributions sit on top. Your plan's own rules can be lower.")]
KSRC=[S_IR136,S_N2666,S_IR111,S_401,S_IRA]
krows=[("401(k), 403(b), governmental 457, TSP: employee deferral","$24,500","$25,500"),("Catch-up, age 50 and older","$8,000","$8,500"),("Catch-up, ages 60 to 63","$11,250","$11,750"),("Total additions, employee plus employer (415(c))","$72,000","$75,000"),("Roth catch-up wage threshold (prior-year FICA wages)","$150,000","$155,000"),("Traditional and Roth IRA","$7,500","$7,500"),("IRA catch-up, age 50 and older","$1,100","$1,100"),("SIMPLE IRA / SIMPLE 401(k)","$17,000","$17,500")]
kbody=f'''<article><p class="by"><a href="../../">💵 Money</a> › <a href="../">2027 tax numbers</a> › 401(k) and IRA limits 2027</p><span class="pill" style="background:#1a7f37;color:#fff">Official since Nov 12, 2026</span>
<h1>401k and IRA Contribution Limits for 2027</h1><p class="by">{BY} · Published Oct 18, 2026 · Last updated Nov 18, 2026</p>
<p><b>Short answer:</b> it's official. The IRS announced the 2027 retirement plan limits on <b>November 12, 2026</b> in news release <b>IR-2026-136</b> and <b>Notice 2026-66</b>. The 401(k) limit rises <b>$1,000 to $25,500</b>; the IRA limit stays at $7,500. Here's every number.</p>
{NOADV}
{taxnav("../../../",TXK)}
<h2>🏦 2026 vs 2027, both official</h2><table><tr><th>Limit</th><th>2026 {OFF}</th><th>2027 {OFF}</th></tr>{"".join(f"<tr><td>{esc(a)}</td><td>{b}</td><td>{c}</td></tr>" for a,b,c in krows)}</table>
<p class="src">2026: IRS IR-2025-111 and Notice 2025-67. 2027: IRS IR-2026-136 and Notice 2026-66, Nov 12, 2026.</p>
<h2>📉 2026 vs 2027 IRA income phase-outs (official)</h2><table><tr><th>Who</th><th>2026 range (modified AGI)</th><th>2027 range (modified AGI)</th></tr><tr><td>Traditional IRA deduction: single, covered by a workplace plan</td><td>$81,000 to $91,000</td><td>$83,000 to $93,000</td></tr><tr><td>Traditional IRA deduction: married filing jointly, contributor covered</td><td>$129,000 to $149,000</td><td>$133,000 to $153,000</td></tr><tr><td>Traditional IRA deduction: contributor not covered, spouse covered</td><td>$242,000 to $252,000</td><td>$250,000 to $260,000</td></tr><tr><td>Roth IRA: single and head of household</td><td>$153,000 to $168,000</td><td>$158,000 to $173,000</td></tr><tr><td>Roth IRA: married filing jointly</td><td>$242,000 to $252,000</td><td>$250,000 to $260,000</td></tr><tr><td>Married filing separately (both)</td><td>$0 to $10,000 (not indexed)</td><td>$0 to $10,000 (not indexed)</td></tr></table>
<h2>🔍 How the adjustment works</h2><p>The 401(k) family of limits is indexed by law (Internal Revenue Code section 415(d)) to the CPI-U average for July through September compared with a base quarter. Each increase is rounded down: to $500 for deferrals and catch-ups, $500 for total additions and $5,000 for the Roth catch-up wage threshold. Notice 2026-66 is the IRS's own published calculation, so these are final figures, not an estimate.</p>
<p>Also funding health costs pre-tax? The <a href="../hsa-limits-2027/">2027 HSA limits</a> are official too. And see where your income lands with the <a href="../2027-tax-brackets/#calculator">bracket calculator</a>.</p>
{fhtml(KQ)}{taxrel("../../../")}{srclist(KSRC)}</article>'''
KTITLE="401k and IRA Contribution Limits for 2027"
KDESC="Official 2027 401(k) limit is $25,500 (IRS IR-2026-136, Nov 12, 2026); IRA stays at $7,500. Catch-ups, phase-outs and SIMPLE limits, all official."
kld=[taxart(KTITLE,KDESC,TXK,KSRC),faqld(KQ),crumbs(TXCR+[("401(k) and IRA limits 2027",TXK)])]
page(TXK+"index.html",KTITLE,KDESC,kbody,ld=kld,article=False,cat="money")
# ---------------- HSA ----------------
HQ=[("What is the HSA limit for 2027?","Official: $4,500 for self-only coverage and $9,000 for family coverage, set by IRS Revenue Procedure 2026-24. That's up from $4,400 and $8,750 in 2026."),
("What is the HSA catch-up contribution for 2027?","$1,000 extra if you're 55 or older. That amount is fixed in the law and isn't indexed for inflation."),
("What counts as a high-deductible health plan in 2027?","For 2027, the deductible must be at least $1,750 for self-only or $3,500 for family coverage, and out-of-pocket costs (not premiums) can't exceed $8,700 self-only or $17,400 family."),
("Are the 2027 HSA limits official?","Yes. Unlike brackets and 401(k) limits, the IRS publishes HSA amounts in the spring. Rev. Proc. 2026-24 is on IRS.gov.")]
HSRC=[S_RP2624,S_IRB2625,S_RP2519,S_P969]
hbody=f'''<article><p class="by"><a href="../../">💵 Money</a> › <a href="../">2027 tax numbers</a> › HSA limits 2027</p><span class="pill" style="background:#1a7f37;color:#fff">Official IRS numbers</span>
<h1>HSA Limits 2027: $4,500 Self-Only, $9,000 Family (Official)</h1><p class="by">{BY} · Published Oct 18, 2026 · Last updated Oct 18, 2026</p>
<p><b>Short answer:</b> this one's locked in. IRS Revenue Procedure 2026-24 sets the 2027 health savings account limit at <b>$4,500 for self-only</b> coverage and <b>$9,000 for family</b> coverage. That's $100 and $250 more than 2026. If you're picking a plan in open enrollment right now, these are the real numbers.</p>
{NOADV}
{taxnav("../../../",TXH)}
<h2>🩺 HSA and HDHP numbers: 2026 vs 2027 (all official)</h2><table><tr><th>Item</th><th>2026 {OFF}</th><th>2027 {OFF}</th></tr><tr><td>HSA contribution limit, self-only</td><td>$4,400</td><td><b>$4,500</b></td></tr><tr><td>HSA contribution limit, family</td><td>$8,750</td><td><b>$9,000</b></td></tr><tr><td>Catch-up, age 55 and older (set by law, not indexed)</td><td>$1,000</td><td>$1,000</td></tr><tr><td>HDHP minimum deductible, self-only</td><td>$1,700</td><td>$1,750</td></tr><tr><td>HDHP minimum deductible, family</td><td>$3,400</td><td>$3,500</td></tr><tr><td>HDHP out-of-pocket maximum, self-only</td><td>$8,500</td><td>$8,700</td></tr><tr><td>HDHP out-of-pocket maximum, family</td><td>$17,000</td><td>$17,400</td></tr><tr><td>Excepted benefit HRA, max newly available</td><td>$2,200</td><td>$2,250</td></tr><tr><td>Direct primary care arrangement fee cap (monthly)</td><td>$150 / $300</td><td>$150 / $300</td></tr></table>
<p class="src">2027: IRS Rev. Proc. 2026-24 (published in Internal Revenue Bulletin 2026-25). 2026: IRS Rev. Proc. 2025-19.</p>
<h2>Why it's in the news now</h2><p>Open season is here. <a href="../../medicare-open-enrollment-2027/">Medicare open enrollment</a> runs through December 7, and <a href="../../open-enrollment-2027/">HealthCare.gov open enrollment</a> starts November 1, with most workplace benefits windows in between. People comparing a high-deductible plan want the 2027 HSA math, and unlike the brackets, it's already official. One heads up: once you're enrolled in Medicare, you generally can't make new HSA contributions. IRS Publication 969 has the rules.</p>
<p>Next: check the official <a href="../401k-ira-limits-2027/">2027 401(k) and IRA limits</a>, the <a href="../gift-estate-tax-2027/">2027 gift and estate tax numbers</a>, and where you land on the <a href="../2027-tax-brackets/">2027 tax brackets</a>.</p>
{fhtml(HQ)}{taxrel("../../../")}{srclist(HSRC)}</article>'''
HTITLE="HSA Limits 2027: $4,500 Self-Only, $9,000 Family (Official IRS)"
HDESC="Official 2027 HSA limits from IRS Rev. Proc. 2026-24: $4,500 self-only, $9,000 family, $1,000 catch-up at 55, plus 2027 HDHP deductible and out-of-pocket limits."
hld=[taxart(HTITLE,HDESC,TXH,HSRC),faqld(HQ),crumbs(TXCR+[("HSA limits 2027",TXH)])]
page(TXH+"index.html",HTITLE,HDESC,hbody,ld=hld,article=False,cat="money")
# ---------------- gift / estate tax ----------------
GQ=[("What is the gift tax exclusion for 2027?","$20,000 per recipient, up from $19,000 in 2026, per IRS news release IR-2026-133 (Nov 5, 2026) and Rev. Proc. 2026-35. You can give that amount to as many people as you like in 2027 without filing a gift tax return or touching your lifetime exclusion."),
("What is the estate tax exemption for 2027?","$15,480,000 per person, up from $15,000,000 for people who died in 2026, per IR-2026-133. A married couple can generally shield about $30.96 million combined with portability."),
("What is the gift tax exclusion for a non-citizen spouse in 2027?","$201,000, up from $194,000 in 2026, per IR-2026-133. This separate, larger exclusion applies only to gifts to a spouse who is not a US citizen."),
("Is the generation-skipping transfer tax exemption the same as the estate tax exemption?","Yes. IRS Rev. Proc. 2026-35 says the $15,480,000 basic exclusion amount for 2027 is also used to set the generation-skipping transfer exemption under Internal Revenue Code section 2631(c)."),
("Do most people owe federal estate or gift tax?","No. With a $15,480,000 per-person exemption in 2027, only very large estates and lifetime gifts are affected. This page is general information, not tax or legal advice; talk to a qualified estate planning attorney or tax professional about your own situation.")]
GSRC=[S_IR133,S_RP2635]
gbody=f'''<article><p class="by"><a href="../../">💵 Money</a> › <a href="../">2027 tax numbers</a> › Gift and estate tax 2027</p><span class="pill" style="background:#1a7f37;color:#fff">Official since Nov 5, 2026</span>
<h1>Gift and Estate Tax Numbers for 2027 (Official IRS Figures)</h1><p class="by">{BY} · Published Nov 18, 2026 · Last updated Nov 18, 2026</p>
<p><b>Short answer:</b> the IRS announced the 2027 gift and estate tax numbers on <b>November 5, 2026</b>, alongside the rest of the 2027 inflation adjustments, in news release <b>IR-2026-133</b> and <b>Revenue Procedure 2026-35</b>. The annual gift tax exclusion rises to <b>$20,000</b> per recipient, and the estate tax basic exclusion amount rises to <b>$15,480,000</b> per person.</p>
{NOADV}
{taxnav("../../../",TXG)}
<h2>🎁 2026 vs 2027 gift and estate tax numbers, both official</h2><table><tr><th>Item</th><th>2026 {OFF}</th><th>2027 {OFF}</th></tr><tr><td>Annual gift tax exclusion, per recipient</td><td>$19,000</td><td><b>$20,000</b></td></tr><tr><td>Annual exclusion for gifts to a non-citizen spouse</td><td>$194,000</td><td><b>$201,000</b></td></tr><tr><td>Estate tax basic exclusion amount, per person</td><td>$15,000,000</td><td><b>$15,480,000</b></td></tr><tr><td>Generation-skipping transfer tax exemption</td><td>$15,000,000</td><td><b>$15,480,000</b></td></tr></table>
<p class="src">Source for both years: IRS IR-2026-133 and Rev. Proc. 2026-35 (2027); the 2026 figures are the amounts the same release quotes as the prior year.</p>
<h2>🔍 What changed and why</h2><p>The annual gift exclusion and the estate tax basic exclusion amount are both indexed to inflation under the Internal Revenue Code. The One Big Beautiful Bill Act raised the estate and gift tax basic exclusion amount to $15,000,000 starting in 2026, and it's indexed for inflation each year after that. The 2027 figure of $15,480,000 is the first inflation adjustment under that higher base.</p>
<h2>🧮 What this means in practice</h2><p>In 2027, you can give up to $20,000 to any number of people without filing IRS Form 709 or using any of your lifetime exemption. A married couple can combine their annual exclusions to give $40,000 per recipient. For estates, the $15,480,000 exemption is the amount you can pass on, during life or at death, before federal estate or gift tax applies; with portability, a surviving spouse can generally use any exemption their late spouse didn't use, for a combined shield of roughly $30.96 million.</p>
<p>Also new for 2027: the <a href="../2027-tax-brackets/">tax brackets and standard deduction</a> and <a href="../401k-ira-limits-2027/">401(k) and IRA limits</a> are official too.</p>
{fhtml(GQ)}{taxrel("../../../")}{srclist(GSRC)}</article>'''
GTITLE="Gift and Estate Tax Numbers for 2027 (Official IRS Figures)"
GDESC="Official 2027 gift and estate tax numbers from IRS IR-2026-133: $20,000 annual gift exclusion, $15,480,000 estate tax exemption, both up from 2026."
gld=[taxart(GTITLE,GDESC,TXG,GSRC),faqld(GQ),crumbs(TXCR+[("Gift and estate tax 2027",TXG)])]
page(TXG+"index.html",GTITLE,GDESC,gbody,ld=gld,article=False,cat="money")
# ---------------- mileage ----------------
MQ=[("What is the IRS mileage rate for 2027?","Not announced yet. The IRS guidance plan lists the 2027 standard mileage rate notice for December 2026. The current business rate is 76 cents a mile for July 1 through December 31, 2026."),
("What is the IRS mileage rate right now?","For miles driven July 1 to December 31, 2026: 76 cents for business, 23.5 cents for medical and military moving, and 14 cents for charity. For January 1 to June 30, 2026 it was 72.5, 20.5 and 14 cents."),
("Why did the mileage rate change in the middle of 2026?","The IRS raised the business, medical and moving rates from July 1, 2026 in Announcement 2026-11, citing recent increases in fuel prices. It last did a midyear change in 2022."),
("Will the charity mileage rate change in 2027?","Unlikely. The 14 cents a mile charity rate is fixed in the tax code (section 170(i)), so only Congress can change it."),
("Can employees deduct unreimbursed mileage?","Generally no. The deduction for unreimbursed employee expenses is permanently disallowed for most employees, with exceptions such as reservists, some government officials, performing artists and eligible educators. Self-employed people can still use the rate. IRS Notice 2026-10 has the details.")]
MSRC=[S_MILE,S_IRB2629,S_IR128,S_N2610,S_PGP]
MH=[("2026 (Jul 1 to Dec 31)","76","23.5","14"),("2026 (Jan 1 to Jun 30)","72.5","20.5","14"),("2025","70","21","14"),("2024","67","21","14"),("2023","65.5","22","14"),("2022 (Jul 1 to Dec 31)","62.5","22","14"),("2022 (Jan 1 to Jun 30)","58.5","18","14")]
mbody=f'''<article><p class="by"><a href="../../">💵 Money</a> › <a href="../">2027 tax numbers</a> › IRS mileage rate 2027</p><span class="pill">IRS 2027 notice expected December 2026</span>
<h1>IRS Mileage Rate 2027: When It's Announced and Today's 76 Cent Rate</h1><p class="by">{BY} · Published Oct 18, 2026 · Last updated Oct 18, 2026</p>
<p><b>Short answer:</b> the 2027 rate isn't out. The IRS usually announces it in late December, and this year's guidance plan says December. Right now the business rate is <b>76 cents a mile</b> for driving from July 1 to December 31, 2026, after a rare midyear bump for fuel prices. Here's every current rate and the history.</p>
{NOADV}
{taxnav("../../../",TXM)}
<h2>🚗 Current and 2027 rates (cents per mile)</h2><table><tr><th>Use</th><th>Jan 1 to Jun 30, 2026 {OFF}</th><th>Jul 1 to Dec 31, 2026 {OFF}</th><th>2027</th></tr><tr><td>Business and self-employed</td><td>72.5</td><td><b>76</b></td><td>Not announced (due December)</td></tr><tr><td>Medical; military moving</td><td>20.5</td><td><b>23.5</b></td><td>Not announced (due December)</td></tr><tr><td>Charity</td><td>14</td><td>14</td><td>14 (fixed by law)</td></tr></table>
<h2>🔍 Our projection, and why it's not a number</h2><p>{PROJ} For charity we can say 14 cents with confidence, because the tax code sets it. For business, medical and moving, we deliberately don't print a 2027 number. Unlike brackets, these rates aren't set by an inflation formula. The IRS bases the business rate on an annual study of the fixed and variable costs of running a car (gas, insurance, maintenance, depreciation), and the medical and moving rate on the variable costs only. So our working baseline is the current 76 cents and 23.5 cents. Where 2027 lands depends mostly on fuel prices this fall, which have been high (see our <a href="../../gas-prices-2026/">gas prices page</a>). It can go down too: the January rate fell for 2020 and again for 2021.</p>
<h2>📈 Rate history (cents per mile, official)</h2><table><tr><th>Period</th><th>Business</th><th>Medical / moving</th><th>Charity</th></tr>{"".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>" for a,b,c,d in MH)}</table>
<p class="src">From the IRS standard mileage rates page. Older years are listed there too.</p>
<p>More 2027 numbers, all official: <a href="../2027-tax-brackets/">tax brackets and standard deduction</a>, <a href="../401k-ira-limits-2027/">401(k) and IRA limits</a>, <a href="../hsa-limits-2027/">HSA limits</a> and <a href="../gift-estate-tax-2027/">gift and estate tax</a>.</p>
{fhtml(MQ)}{taxrel("../../../")}{srclist(MSRC)}</article>'''
MTITLE="IRS Mileage Rate 2027: Release Date and Current 76 Cent Rate"
MDESC="The 2027 IRS standard mileage rate is due in December. Today's rates: 76 cents business, 23.5 cents medical and 14 cents charity for July to December 2026, plus history."
mld=[taxart(MTITLE,MDESC,TXM,MSRC),faqld(MQ),crumbs(TXCR+[("IRS mileage rate 2027",TXM)])]
page(TXM+"index.html",MTITLE,MDESC,mbody,ld=mld,article=False,cat="money")
# ---------------- hub ----------------
XQ=[("Are the 2027 tax brackets out?","Yes, since November 5, 2026 (IRS IR-2026-133 and Rev. Proc. 2026-35)."),
("Which 2027 tax numbers are already official?","Brackets and standard deduction, 401(k) and IRA limits, HSA limits, and gift and estate tax numbers are all official. Only the IRS mileage rate is still pending, expected in December 2026."),
("When did each 2027 IRS number come out?","HSA limits: spring 2026 (Rev. Proc. 2026-24). Brackets, standard deduction and gift/estate tax: November 5, 2026 (IR-2026-133). 401(k), IRA and other retirement limits: November 12, 2026 (IR-2026-136). Mileage rate: still pending, expected December 2026."),
("Is this tax advice?","No. This hub is general information built from IRS releases. For your own situation, use IRS.gov or a qualified tax professional.")]
XSRC=[S_IR133,S_RP2635,S_IR136,S_N2666,S_RP2624,S_MILE]
xrows=[("2027 tax brackets and standard deduction",TXB,"Official","Nov 5, 2026 (IR-2026-133)","$16,100 / $32,200 / $24,150 standard deduction"),("401(k) and IRA limits 2027",TXK,"Official","Nov 12, 2026 (IR-2026-136)","$24,500 401(k), $7,500 IRA"),("HSA limits 2027",TXH,"Official","Out (Rev. Proc. 2026-24)","$4,400 / $8,750"),("Gift and estate tax 2027",TXG,"Official","Nov 5, 2026 (IR-2026-133)","$19,000 gift exclusion, $15,000,000 estate exemption"),("IRS mileage rate 2027",TXM,"Pending, no number yet","December 2026 (expected)","76 cents business (Jul to Dec 2026)")]
xbody=f'''<article><p class="by"><a href="../">💵 Money</a> › 2027 tax numbers</p><span class="pill" style="background:#1a7f37;color:#fff">4 of 5 numbers now official</span>
<h1>2027 Tax Numbers: Brackets, 401(k), HSA, Gift/Estate and Mileage, Tracked Live</h1><p class="by">{BY} · Published Oct 18, 2026 · Last updated Nov 18, 2026</p>
<p>Every fall the IRS resets the numbers that shape next year's money moves. This hub tracks all of them in one place: what's <b>official</b>, and when each IRS release is due. As of November 18, 2026, the 2027 tax brackets, standard deduction, 401(k)/IRA limits, HSA limits and gift/estate tax numbers are all official. Only the mileage rate is still pending. We flip each page to official numbers the day the IRS posts them.</p>
{NOADV}
<h2>📋 Status board (checked Nov 18, 2026)</h2><table><tr><th>Number</th><th>2027 status</th><th>IRS release</th><th>Official 2026 figure</th></tr>{"".join(f'<tr><td><a href="../../{p}"><b>{esc(n)}</b></a></td><td>{esc(s)}</td><td>{esc(w)}</td><td>{esc(v)}</td></tr>' for n,p,s,w,v in xrows)}</table>
<div class="grid">
<div class="card"><span class="pill" style="background:#1a7f37;color:#fff">Official</span><h3>📊 2027 tax brackets and standard deduction</h3><p>Official 2026 and 2027 brackets for every filing status, side by side, and a quick "what bracket am I in" calculator.</p><div class="links"><a class="in" href="../../{TXB}">See the brackets →</a><a class="in" href="../../{TXB}#calculator">Open the calculator →</a></div></div>
<div class="card"><span class="pill" style="background:#1a7f37;color:#fff">Official</span><h3>🏦 401(k) and IRA limits 2027</h3><p>Official $25,500 401(k) limit, catch-ups for 50+ and 60 to 63, and the 2027 IRA phase-outs.</p><div class="links"><a class="in" href="../../{TXK}">See the limits →</a></div></div>
<div class="card"><span class="pill" style="background:#1a7f37;color:#fff">Official</span><h3>🩺 HSA limits 2027</h3><p>$4,500 self-only, $9,000 family, plus 2027 high-deductible plan rules. Handy during open enrollment.</p><div class="links"><a class="in" href="../../{TXH}">See HSA limits →</a></div></div>
<div class="card"><span class="pill" style="background:#1a7f37;color:#fff">Official</span><h3>🎁 Gift and estate tax 2027</h3><p>$20,000 annual gift exclusion and a $15,480,000 estate tax exemption, both official for 2027.</p><div class="links"><a class="in" href="../../{TXG}">See the numbers →</a></div></div>
<div class="card"><span class="pill">Due December</span><h3>🚗 IRS mileage rate 2027</h3><p>Today's 76 cent business rate, the midyear 2026 change, and the full history.</p><div class="links"><a class="in" href="../../{TXM}">See mileage rates →</a></div></div>
</div>
<h2>🔍 How we label numbers</h2><p><b>Official IRS</b> means the figure is in an IRS revenue procedure, notice or news release, linked in the sources. We don't publish projections as if they were figures; where a number isn't out yet, like the 2027 mileage rate, we say so instead of guessing.</p>
<h2>📅 Refresh calendar</h2><ul><li><b>November 2026:</b> IRS 2027 inflation adjustments landed Nov 5 (brackets, standard deduction, gift/estate tax) and Nov 12 (401(k), IRA, SIMPLE).</li><li><b>December 2026 (expected):</b> IRS 2027 standard mileage rates.</li><li><b>January 2027:</b> filing season opens for 2026 returns; we refresh everything again.</li></ul>
{fhtml(XQ)}{taxrel("../../")}{srclist(XSRC)}</article>'''
XTITLE="2027 Tax Numbers: Brackets, 401(k), HSA, Gift/Estate and Mileage Tracker"
XDESC="Every 2027 IRS number in one place: tax brackets, standard deduction, 401(k), IRA, HSA and gift/estate tax limits, and the mileage rate, with release dates."
xld=[taxart(XTITLE,XDESC,TX,XSRC),faqld(XQ),crumbs(TXCR),{"@context":"https://schema.org","@type":"ItemList","name":"2027 tax numbers pages","itemListElement":[{"@type":"ListItem","position":i+1,"url":B+"/"+p,"name":n} for i,(n,p,_,_,_) in enumerate(xrows)]}]
page(TX+"index.html",XTITLE,XDESC,xbody,ld=xld,article=False,cat="money")
LM.update({B+"/"+p:PUB18B for p in (TX,TXB,TXK,TXH,TXM,TXG)})
TAXLINK='<div class="card picks" style="margin:14px 0"><span class="pill">IRS 2027 numbers</span><h3>🧾 2027 tax numbers: brackets, 401(k), HSA, gift/estate, mileage</h3><p>What\'s official (almost everything now) and a quick bracket calculator. Updated the day the IRS posts each number.</p><div class="links"><a class="in" href="{r}money/2027-tax-numbers/">Open the tracker →</a><a class="in" href="{r}money/2027-tax-numbers/2027-tax-brackets/#calculator">Bracket calculator →</a></div></div>'
SUBX={"medicare-open-enrollment-2027":'<p>Comparing plans with a health savings account in mind? The <a href="../2027-tax-numbers/hsa-limits-2027/">2027 HSA limits</a> are official at $4,500 and $9,000. See every <a href="../2027-tax-numbers/">2027 tax number</a> in one place, and the official <a href="../medicare-part-b-premium-2027/">2027 Medicare Part B premium</a>.</p>',
"retirement":'<p>Planning 2027 savings? See the official <a href="../2027-tax-numbers/401k-ira-limits-2027/">2027 401(k) and IRA limits</a> and the <a href="../2027-tax-numbers/2027-tax-brackets/">2027 tax brackets</a>.</p>'}
