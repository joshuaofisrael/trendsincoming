# --- 2027 tax numbers hub: brackets + calculator, 401k/IRA, HSA, mileage (added 2026-10-18). exec'd from build.py ---
PUB18="2026-10-18"; MOD18="2026-10-18"; MOD19="2026-11-19"; MOD20="2026-11-20"
TX="money/2027-tax-numbers/"
TXB=TX+"2027-tax-brackets/"; TXS=TX+"standard-deduction-2027/"; TXK=TX+"401k-ira-limits-2027/"; TXH=TX+"hsa-limits-2027/"; TXM=TX+"irs-mileage-rate-2027/"; TXG=TX+"gift-estate-tax-2027/"
PHOTO["calculator-tax-forms"]="Calculator, ballpoint pen and a stack of printed forms on a wooden table in window light, with a speckled mug to the side"
KEYPH[TXS]=KEYPH[TXB]=KEYPH[TX]="calculator-tax-forms"
PB="money/medicare-part-b-premium-2027/"
PDP="money/medicare-part-d-out-of-pocket-cap-2027/"
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
    L=[(TX,"🧾 Hub: all 2027 tax numbers"),(TXS,"💵 Standard deduction 2027"),(TXB,"📊 2027 tax brackets"),(TXB+"#calculator","🧮 Bracket calculator"),(TXK,"🏦 401(k) and IRA limits 2027"),(TXH,"🩺 HSA limits 2027"),(TXG,"🎁 Gift and estate tax 2027"),(TXM,"🚗 IRS mileage rate 2027")]
    return '<div class="cats" style="margin:14px 0">'+"".join(f'<a href="{r}{p}">{esc(t)}</a>' for p,t in L if p!=cur)+'</div>'
def taxrel(r):
    return f'<h2>Related on Trends Incoming</h2><ul><li><a href="{r}money/social-security-2027/">Social Security 2027: 3.6% COLA calculator and payment dates</a></li><li><a href="{r}{PB}">Medicare Part B premium 2027: $209.40 a month (official)</a></li><li><a href="{r}{PDP}">Medicare Part D cap 2027: $2,400 out of pocket, $700 deductible</a></li><li><a href="{r}money/medicare-open-enrollment-2027/">Medicare open enrollment 2027 (Oct 15 to Dec 7)</a></li><li><a href="{r}money/open-enrollment-2027/">HealthCare.gov open enrollment 2027 (Nov 1 to Jan 15)</a></li><li><a href="{r}money/minimum-wage-2027/">Minimum wage 2027 by state: every January 1 raise</a></li><li><a href="{r}money/fafsa-deadlines/">FAFSA 2027-28 deadlines</a></li><li><a href="{r}money/retirement/">Retirement and Social Security trends</a></li></ul>'
def taxart(title,desc,path,cites,mod=None):
    return {"@context":"https://schema.org","@type":"Article","headline":title,"description":desc,"datePublished":PUB18,"dateModified":mod or MOD18,"mainEntityOfPage":B+"/"+path,"author":{"@type":"Organization","name":"The Trends Incoming team","url":B+"/about/"},"publisher":pub,"citation":[u for _,u in cites],"about":{"@type":"Thing","name":"US federal tax numbers for 2027"}}
TXCR=[("Home",""),("Money","money/"),("2027 tax numbers",TX)]
def tax_compare(r,cur=None):
    opts=[(TX,"2027 official numbers tracker"),(TXS,"Standard deduction 2027"),(TXB,"2027 tax brackets"),(TXK,"401(k) and IRA limits 2027"),(TXH,"HSA limits 2027"),(TXG,"Gift and estate tax 2027"),(TXM,"IRS mileage rate 2027"),("money/social-security-2027/","Social Security COLA 2027"),(PB,"Medicare Part B premium 2027"),(PDP,"Medicare Part D cap 2027"),("money/minimum-wage-2027/","Minimum wage by state 2027"),("money/fafsa-deadlines/","FAFSA 2027-28 deadlines")]
    return '<aside class="compare" aria-label="Check another 2027 number"><h2>Check another 2027 number</h2><p>Official figures only, linked to the primary release.</p><ul>'+"".join(f'<li><a href="{r}{h}">{esc(t)}</a></li>' for h,t in opts if h!=cur)+'</ul></aside>'
def tax_next(r,extra=()):
    items=[("money/social-security-2027/","Social Security COLA 2027","Official 3.6% COLA and January payment dates.","og/money.png"),(PB,"Medicare Part B premium 2027","$209.40 a month, official from CMS.","og/money.png"),("money/minimum-wage-2027/","Minimum wage by state 2027","Every January 1 raise, with CSV.","og/money.png"),("money/fafsa-deadlines/","FAFSA 2027-28 deadlines","Open date and federal/state deadlines.","og/education.png")]+list(extra)
    cards="".join(f'<a class="nrcard" href="{r}{h}"><img src="{r}{th}" width="320" height="180" alt="" loading="lazy" decoding="async"><span class="nrt"><b>{esc(ti)}</b><br>{esc(bl)}</span></a>' for h,ti,bl,th in items[:4])
    return f'<section class="nr" aria-label="Related next reads"><h2>Related next reads</h2><div class="nrgrid">{cards}</div></section>'
def tax_next_mid(r,cur=None):
    items=[(TXS,"Standard deduction 2027","$16,600 single, $33,200 joint, $24,925 head of household.","og/money.png"),(TXB,"2027 tax brackets","Official brackets beside the standard deduction.","og/money.png"),(TXK,"401(k) and IRA limits 2027","Official $25,500 401(k) limit.","og/money.png"),(TXH,"HSA limits 2027","Official $4,500 / $9,000 contribution limits.","og/money.png"),(TXG,"Gift and estate tax 2027","$20,000 gift exclusion and $15.48M estate exemption.","og/money.png"),(TX,"2027 official numbers tracker","Every figure, agency and release date.","og/money.png")]
    items=[i for i in items if i[0]!=cur][:4]
    cards="".join(f'<a class="nrcard" href="{r}{h}"><img src="{r}{th}" width="320" height="180" alt="" loading="lazy" decoding="async"><span class="nrt"><b>{esc(ti)}</b><br>{esc(bl)}</span></a>' for h,ti,bl,th in items)
    return f'<section class="nr" aria-label="Keep reading"><h2>Keep reading</h2><div class="nrgrid">{cards}</div></section>'
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
<p class="warn" style="margin-top:6px"><b>Estimate only, not personal tax advice.</b> It runs in your browser and nothing is sent anywhere. Both years use the IRS revenue procedure for that year. It leaves out credits, the age and blindness add-ons, capital gains rates, AMT, payroll tax and state tax.</p>
<form id="taxcalc" onsubmit="return false"><label for="ty"><b>Tax year</b></label><br><select id="ty" {SEL}><option value="2026">2026 (Rev. Proc. 2025-32)</option><option value="2027">2027 (Rev. Proc. 2026-35)</option></select><br>
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
<h1>2027 Tax Brackets and Standard Deduction (IRS Official Numbers)</h1><p class="by">{BY} · Published Oct 18, 2026 · Last updated Nov 20, 2026</p>
<p><b>Short answer:</b> it's official. On <b>November 5, 2026</b> the IRS released the 2027 tax brackets and standard deduction in news release <b>IR-2026-133</b> and <b>Revenue Procedure 2026-35</b>. The seven rates are unchanged by law; only the income thresholds moved up with inflation. Here are the full official 2026 and 2027 numbers, plus a calculator.</p>
{NOADV}
<table><tr><th>2027 brackets and standard deduction</th><td>{OFF} IRS IR-2026-133 / Rev. Proc. 2026-35, Nov 5, 2026</td></tr><tr><th>Tax rates</th><td>10%, 12%, 22%, 24%, 32%, 35%, 37% (permanent law, unchanged)</td></tr><tr><th>2027 standard deduction, single</th><td>$16,600 (2026: $16,100)</td></tr><tr><th>2027 standard deduction, joint</th><td>$33,200 (2026: $32,200)</td></tr><tr><th>2027 standard deduction, head of household</th><td>$24,925 (2026: $24,150)</td></tr></table>
{taxnav("../../../",TXB)}
{tax_compare("../../../",TXB)}
{CALC}
<h2>📊 2026 vs 2027 tax brackets, side by side</h2><p>Both years are now official: 2026 from IRS Rev. Proc. 2025-32, 2027 from IRS Rev. Proc. 2026-35 (Nov 5, 2026). Taxable income is income after deductions.</p>
{"".join(sidebyside(k,l) for k,l in ST)}
<h2>💵 Standard deduction: 2026 vs 2027, both official</h2>{bsd()}
<p>That table is the short version. The <a href="../standard-deduction-2027/">2027 standard deduction page</a> separates the four filing statuses, the $1,700 and $2,100 additional amounts for age or blindness, and the dependent cap, each tied to the revenue procedure section that prints it.</p>
<p>Also still in effect for 2025 through 2028: a separate senior deduction of up to $6,000 per person age 65 or older, phased down above $75,000 of modified AGI ($150,000 joint). It sits on top of the standard deduction above.</p>
<h2>🔍 How the inflation adjustment works</h2><p>Brackets and the standard deduction are indexed to inflation by law (Internal Revenue Code section 1(f)). The IRS compares the chained consumer price index (C-CPI-U) for a 12-month base period with a prior base year, then rounds each increase down to the next $50 ($25 for single and married filing separately brackets). Rev. Proc. 2026-35 is the IRS's own calculation under that formula, so these figures are final, not an estimate.</p>
<h2>🧾 Worked example (2026, official)</h2><p>A single filer with $60,000 of taxable income in 2026 pays 10% on the first $12,400 ($1,240), 12% on the next $38,000 ($4,560) and 22% on the last $9,600 ($2,112). Total: <b>$7,912</b> before credits. That matches the IRS table: $5,800 plus 22% of the amount over $50,400. Top bracket 22%, average rate about 13.2%.</p>
<h2>📅 Where the rest of the 2027 numbers stand</h2><ul><li><b>Brackets and standard deduction:</b> official (IR-2026-133, Nov 5, 2026).</li><li><b>401(k) and IRA limits:</b> official (IR-2026-136, Nov 12, 2026). See our <a href="../401k-ira-limits-2027/">401(k) and IRA limits page</a>.</li><li><b>HSA limits:</b> official at $4,500 and $9,000. See <a href="../hsa-limits-2027/">HSA limits 2027</a>.</li><li><b>Gift and estate tax:</b> official (IR-2026-133, Nov 5, 2026). See <a href="../gift-estate-tax-2027/">gift and estate tax 2027</a>.</li><li><b>Mileage rate:</b> still not announced; IRS notice expected in December 2026. See <a href="../irs-mileage-rate-2027/">IRS mileage rate 2027</a>.</li></ul>
{fhtml(BQ)}{tax_next("../../../")}{taxrel("../../../")}{srclist(BSRC)}</article>'''
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
{tax_compare("../../../",TXK)}
<h2>🏦 2026 vs 2027, both official</h2><table><tr><th>Limit</th><th>2026 {OFF}</th><th>2027 {OFF}</th></tr>{"".join(f"<tr><td>{esc(a)}</td><td>{b}</td><td>{c}</td></tr>" for a,b,c in krows)}</table>
<p class="src">2026: IRS IR-2025-111 and Notice 2025-67. 2027: IRS IR-2026-136 and Notice 2026-66, Nov 12, 2026.</p>
<h2>📉 2026 vs 2027 IRA income phase-outs (official)</h2><table><tr><th>Who</th><th>2026 range (modified AGI)</th><th>2027 range (modified AGI)</th></tr><tr><td>Traditional IRA deduction: single, covered by a workplace plan</td><td>$81,000 to $91,000</td><td>$83,000 to $93,000</td></tr><tr><td>Traditional IRA deduction: married filing jointly, contributor covered</td><td>$129,000 to $149,000</td><td>$133,000 to $153,000</td></tr><tr><td>Traditional IRA deduction: contributor not covered, spouse covered</td><td>$242,000 to $252,000</td><td>$250,000 to $260,000</td></tr><tr><td>Roth IRA: single and head of household</td><td>$153,000 to $168,000</td><td>$158,000 to $173,000</td></tr><tr><td>Roth IRA: married filing jointly</td><td>$242,000 to $252,000</td><td>$250,000 to $260,000</td></tr><tr><td>Married filing separately (both)</td><td>$0 to $10,000 (not indexed)</td><td>$0 to $10,000 (not indexed)</td></tr></table>
<h2>🔍 How the adjustment works</h2><p>The 401(k) family of limits is indexed by law (Internal Revenue Code section 415(d)) to the CPI-U average for July through September compared with a base quarter. Each increase is rounded down: to $500 for deferrals and catch-ups, $500 for total additions and $5,000 for the Roth catch-up wage threshold. Notice 2026-66 is the IRS's own published calculation, so these are final figures, not an estimate.</p>
<p>Also funding health costs pre-tax? The <a href="../hsa-limits-2027/">2027 HSA limits</a> are official too. And see where your income lands with the <a href="../2027-tax-brackets/#calculator">bracket calculator</a>.</p>
{fhtml(KQ)}{tax_next("../../../")}{taxrel("../../../")}{srclist(KSRC)}</article>'''
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
{tax_compare("../../../",TXH)}
<h2>🩺 HSA and HDHP numbers: 2026 vs 2027 (all official)</h2><table><tr><th>Item</th><th>2026 {OFF}</th><th>2027 {OFF}</th></tr><tr><td>HSA contribution limit, self-only</td><td>$4,400</td><td><b>$4,500</b></td></tr><tr><td>HSA contribution limit, family</td><td>$8,750</td><td><b>$9,000</b></td></tr><tr><td>Catch-up, age 55 and older (set by law, not indexed)</td><td>$1,000</td><td>$1,000</td></tr><tr><td>HDHP minimum deductible, self-only</td><td>$1,700</td><td>$1,750</td></tr><tr><td>HDHP minimum deductible, family</td><td>$3,400</td><td>$3,500</td></tr><tr><td>HDHP out-of-pocket maximum, self-only</td><td>$8,500</td><td>$8,700</td></tr><tr><td>HDHP out-of-pocket maximum, family</td><td>$17,000</td><td>$17,400</td></tr><tr><td>Excepted benefit HRA, max newly available</td><td>$2,200</td><td>$2,250</td></tr><tr><td>Direct primary care arrangement fee cap (monthly)</td><td>$150 / $300</td><td>$150 / $300</td></tr></table>
<p class="src">2027: IRS Rev. Proc. 2026-24 (published in Internal Revenue Bulletin 2026-25). 2026: IRS Rev. Proc. 2025-19.</p>
<h2>Why it's in the news now</h2><p>Open season is here. <a href="../../medicare-open-enrollment-2027/">Medicare open enrollment</a> runs through December 7, and <a href="../../open-enrollment-2027/">HealthCare.gov open enrollment</a> starts November 1, with most workplace benefits windows in between. People comparing a high-deductible plan want the 2027 HSA math, and unlike the brackets, it's already official. One heads up: once you're enrolled in Medicare, you generally can't make new HSA contributions. IRS Publication 969 has the rules.</p>
<p>Next: check the official <a href="../401k-ira-limits-2027/">2027 401(k) and IRA limits</a>, the <a href="../gift-estate-tax-2027/">2027 gift and estate tax numbers</a>, and where you land on the <a href="../2027-tax-brackets/">2027 tax brackets</a>.</p>
{fhtml(HQ)}{tax_next("../../../")}{taxrel("../../../")}{srclist(HSRC)}</article>'''
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
{tax_compare("../../../",TXG)}
<h2>🎁 2026 vs 2027 gift and estate tax numbers, both official</h2><table><tr><th>Item</th><th>2026 {OFF}</th><th>2027 {OFF}</th></tr><tr><td>Annual gift tax exclusion, per recipient</td><td>$19,000</td><td><b>$20,000</b></td></tr><tr><td>Annual exclusion for gifts to a non-citizen spouse</td><td>$194,000</td><td><b>$201,000</b></td></tr><tr><td>Estate tax basic exclusion amount, per person</td><td>$15,000,000</td><td><b>$15,480,000</b></td></tr><tr><td>Generation-skipping transfer tax exemption</td><td>$15,000,000</td><td><b>$15,480,000</b></td></tr></table>
<p class="src">Source for both years: IRS IR-2026-133 and Rev. Proc. 2026-35 (2027); the 2026 figures are the amounts the same release quotes as the prior year.</p>
{tax_next_mid("../../../",TXG)}
<h2>🔍 What changed and why</h2><p>The annual gift exclusion and the estate tax basic exclusion amount are both indexed to inflation under the Internal Revenue Code. The One Big Beautiful Bill Act raised the estate and gift tax basic exclusion amount to $15,000,000 starting in 2026, and it's indexed for inflation each year after that. The 2027 figure of $15,480,000 is the first inflation adjustment under that higher base.</p>
<h2>🧮 What this means in practice</h2><p>In 2027, you can give up to $20,000 to any number of people without filing IRS Form 709 or using any of your lifetime exemption. A married couple can combine their annual exclusions to give $40,000 per recipient. For estates, the $15,480,000 exemption is the amount you can pass on, during life or at death, before federal estate or gift tax applies; with portability, a surviving spouse can generally use any exemption their late spouse didn't use, for a combined shield of roughly $30.96 million.</p>
<p>Also new for 2027: the <a href="../2027-tax-brackets/">tax brackets and standard deduction</a> and <a href="../401k-ira-limits-2027/">401(k) and IRA limits</a> are official too.</p>
{fhtml(GQ)}{tax_next("../../../")}{taxrel("../../../")}{srclist(GSRC)}</article>'''
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
mbody=f'''<article><p class="by"><a href="../../">💵 Money</a> › <a href="../">2027 tax numbers</a> › IRS mileage rate 2027</p><span class="pill">Still pending · checked Nov 19, 2026</span>
<h1>IRS Mileage Rate 2027: Still Not Out, Current Rate Is 76 Cents</h1><p class="by">{BY} · Published Oct 18, 2026 · Last updated Nov 19, 2026</p>
<p><b>Short answer:</b> the 2027 rate still is not out. We re-checked the <a href="{S_MILE[1]}" rel="noopener" target="_blank">IRS standard mileage rates page</a> and the 2026 to 2027 priority guidance plan on <b>November 19, 2026</b>. No 2027 notice has posted. The IRS usually announces the next year's rates in late December, and this year's guidance plan still points at December. Right now the business rate is <b>76 cents a mile</b> for driving from July 1 to December 31, 2026.</p>
{NOADV}
{taxnav("../../../",TXM)}
{tax_compare("../../../",TXM)}
<h2>🚗 Current and 2027 rates (cents per mile)</h2><table><tr><th>Use</th><th>Jan 1 to Jun 30, 2026 {OFF}</th><th>Jul 1 to Dec 31, 2026 {OFF}</th><th>2027 (checked Nov 19, 2026)</th></tr><tr><td>Business and self-employed</td><td>72.5</td><td><b>76</b></td><td>Not announced (due December)</td></tr><tr><td>Medical; military moving</td><td>20.5</td><td><b>23.5</b></td><td>Not announced (due December)</td></tr><tr><td>Charity</td><td>14</td><td>14</td><td>14 (fixed by law)</td></tr></table>
{tax_next_mid("../../../")}
<h2>🔍 Why we will not invent a 2027 number</h2><p>{PROJ} For charity we can say 14 cents with confidence, because the tax code sets it. For business, medical and moving, we deliberately do not print a 2027 figure. Unlike brackets, these rates are not set by an inflation formula. The IRS bases the business rate on an annual study of the fixed and variable costs of running a car (gas, insurance, maintenance, depreciation), and the medical and moving rate on the variable costs only. Our working baseline stays the current 76 cents and 23.5 cents until the notice lands. Fuel prices this fall have been high (see our <a href="../../gas-prices-2026/">gas prices page</a>), but the January rate has fallen in past years too.</p>
<h2>📈 Rate history (cents per mile, official)</h2><table><tr><th>Period</th><th>Business</th><th>Medical / moving</th><th>Charity</th></tr>{"".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>" for a,b,c,d in MH)}</table>
<p class="src">From the IRS standard mileage rates page. Older years are listed there too.</p>
<p>More 2027 numbers, all official: <a href="../2027-tax-brackets/">tax brackets and standard deduction</a>, <a href="../401k-ira-limits-2027/">401(k) and IRA limits</a>, <a href="../hsa-limits-2027/">HSA limits</a> and <a href="../gift-estate-tax-2027/">gift and estate tax</a>. Or open the full <a href="../">2027 official numbers tracker</a>.</p>
{fhtml(MQ)}{tax_next("../../../")}{taxrel("../../../")}{srclist(MSRC)}</article>'''
MTITLE="IRS Mileage Rate 2027: Still Not Out, Current Rate Is 76 Cents"
MDESC="Checked Nov 19, 2026: the 2027 IRS mileage rate is still pending. Current rates are 76 cents business, 23.5 cents medical, 14 cents charity."
mld=[taxart(MTITLE,MDESC,TXM,MSRC,mod=MOD19),faqld(MQ),crumbs(TXCR+[("IRS mileage rate 2027",TXM)])]
page(TXM+"index.html",MTITLE,MDESC,mbody,ld=mld,article=False,cat="money")
# ---------------- hub: 2027 official numbers tracker (link asset) ----------------
XQ=[("Are the 2027 tax brackets out?","Yes, since November 5, 2026 (IRS IR-2026-133 and Rev. Proc. 2026-35)."),
("Which 2027 tax numbers are already official?","Brackets and standard deduction, 401(k) and IRA limits, HSA limits, gift and estate tax, Social Security COLA, Medicare Part B premium, the Part D out-of-pocket threshold and standard deductible, and most January 1 state minimum wages are official. Only the IRS mileage rate is still pending, expected in December 2026."),
("When did each 2027 IRS number come out?","HSA limits: spring 2026 (Rev. Proc. 2026-24). Brackets, standard deduction (including the age and blindness add-ons) and gift/estate tax: November 5, 2026 (IR-2026-133 and Rev. Proc. 2026-35). 401(k), IRA and other retirement limits: November 12, 2026 (IR-2026-136). Mileage rate: still pending as of November 21, 2026. The Part D cap is a CMS figure, not an IRS one: April 6, 2026 rate announcement."),
("Can I reuse this tracker?","Yes. Download the CSV and cite this page. Free to use with a link back to Trends Incoming."),
("Is this tax advice?","No. This hub is general information built from IRS, SSA, CMS and state labor releases. For your own situation, use the linked agencies or a qualified professional.")]
S_SSA=("SSA press release: 3.6 percent benefit increase for 2027 (Oct 14, 2026)","https://www.ssa.gov/news/en/press/releases/2026-10-14.html")
S_CMS=("CMS fact sheet: 2027 Medicare Parts A & B Premiums and Deductibles (Nov 17, 2026)","https://www.cms.gov/newsroom/fact-sheets/2027-medicare-parts-b-premiums-deductibles")
S_PD=("CMS CY 2027 Rate Announcement, Attachment V Part D benefit parameters (April 6, 2026)","https://www.cms.gov/files/document/2027-announcement.pdf")
XSRC=[S_IR133,S_RP2635,S_IR136,S_N2666,S_RP2624,S_MILE,S_SSA,S_CMS,S_PD]
# Tracker rows: figure, value, agency, release date, source url, detail path
TRACK=[
("2027 tax brackets (single 10% top of band)","$12,800","IRS","2026-11-05",S_IR133[1],TXB),
("2027 standard deduction (single)","$16,600","IRS","2026-11-05",S_IR133[1],TXS),
("2027 standard deduction (married filing jointly)","$33,200","IRS","2026-11-05",S_IR133[1],TXS),
("2027 standard deduction (head of household)","$24,925","IRS","2026-11-05",S_IR133[1],TXS),
("2027 additional standard deduction, aged or blind (married)","$1,700","IRS","2026-11-05",S_RP2635[1],TXS),
("2027 additional standard deduction, aged or blind (unmarried)","$2,100","IRS","2026-11-05",S_RP2635[1],TXS),
("2027 401(k) employee deferral limit","$25,500","IRS","2026-11-12",S_IR136[1],TXK),
("2027 IRA contribution limit","$7,500","IRS","2026-11-12",S_IR136[1],TXK),
("2027 HSA contribution limit (self-only)","$4,500","IRS","2026 (Rev. Proc. 2026-24)",S_RP2624[1],TXH),
("2027 HSA contribution limit (family)","$9,000","IRS","2026 (Rev. Proc. 2026-24)",S_RP2624[1],TXH),
("2027 annual gift tax exclusion","$20,000","IRS","2026-11-05",S_IR133[1],TXG),
("2027 estate tax basic exclusion","$15,480,000","IRS","2026-11-05",S_IR133[1],TXG),
("2027 IRS business mileage rate","Not announced","IRS","",S_MILE[1],TXM),
("2027 Social Security COLA","3.6%","SSA","2026-10-14",S_SSA[1],"money/social-security-2027/"),
("2027 Medicare Part B standard premium","$209.40 / month","CMS","2026-11-17",S_CMS[1],PB),
("2027 Medicare Part D out-of-pocket threshold","$2,400","CMS","2026-04-06",S_PD[1],PDP),
("2027 Medicare Part D defined standard deductible","$700","CMS","2026-04-06",S_PD[1],PDP),
("2027 state minimum wages (Jan 1 raises)","See state table","State labor agencies","2026-10-19","https://trendsincoming.com/money/minimum-wage-2027/","money/minimum-wage-2027/"),
]
os.makedirs(TX,exist_ok=True)
csv_lines=["figure,value,agency,release_date,source_url,detail_url"]
for fig,val,agency,rel,src,path in TRACK:
    csv_lines.append(",".join([
        '"'+fig.replace('"','""')+'"',
        '"'+val.replace('"','""')+'"',
        agency,
        rel,
        src,
        B+"/"+path,
    ]))
open(TX+"2027-official-numbers.csv","w").write("\n".join(csv_lines)+"\n")
track_rows="".join(
    f'<tr><td><a href="../../{p}"><b>{esc(fig)}</b></a></td><td>{esc(val)}</td><td>{esc(agency)}</td><td>{esc(rel or "Pending")}</td><td><a href="{src}" rel="noopener" target="_blank">Source</a></td></tr>'
    for fig,val,agency,rel,src,p in TRACK
)
cite_box=f'''<div class="card" id="cite" style="background:#fff8e6;margin:14px 0"><h2 style="margin-top:0">Cite this tracker</h2>
<p>Trends Incoming. "2027 Official Numbers Tracker." Updated 2026-11-21. {B}/{TX}</p>
<p class="src">Suggested attribution: Data compiled by Trends Incoming from the linked IRS, SSA, CMS and state releases. Free to reuse with a link back.</p>
<p><a href="2027-official-numbers.csv">Download the table as CSV</a></p></div>'''
xbody=f'''<article><p class="by"><a href="../">💵 Money</a> › 2027 official numbers tracker</p><span class="pill" style="background:#1a7f37;color:#fff">Link asset · checked Nov 21, 2026</span>
<h1>2027 Official Numbers Tracker: Every Figure, Agency and Release Date</h1><p class="by">{BY} · Published Oct 18, 2026 · Last updated Nov 21, 2026</p>
<p>One table for the 2027 money numbers people look up every fall: IRS brackets and limits, Social Security COLA, Medicare Part B, the Part D out-of-pocket cap and standard deductible, state minimum wages, and the still-pending mileage rate. Each row names the publishing agency, the release date, and the primary source. Download the CSV or cite the box below. We flip a row the day the agency posts it. No estimates are labelled as official figures.</p>
{NOADV}
{tax_compare("../../",TX)}
<h2 id="tracker">📋 2027 official numbers (checked Nov 21, 2026)</h2>
<div style="overflow-x:auto"><table><tr><th>Figure</th><th>Value</th><th>Agency</th><th>Release date</th><th>Source</th></tr>{track_rows}</table></div>
{cite_box}
{tax_next_mid("../../")}
<h2>Child guides</h2>
<div class="grid">
<div class="card"><span class="pill" style="background:#1a7f37;color:#fff">Official</span><h3>📊 2027 tax brackets</h3><p>Official 2026 and 2027 brackets for every filing status, plus a bracket calculator.</p><div class="links"><a class="in" href="../../{TXB}">See the brackets →</a></div></div>
<div class="card"><span class="pill" style="background:#1a7f37;color:#fff">Official</span><h3>💵 Standard deduction 2027</h3><p>$16,600 single, $33,200 joint, $24,925 head of household, plus the age and blindness add-ons.</p><div class="links"><a class="in" href="../../{TXS}">See the deduction →</a></div></div>
<div class="card"><span class="pill" style="background:#1a7f37;color:#fff">Official</span><h3>🏦 401(k) and IRA limits 2027</h3><p>Official $25,500 401(k) limit, catch-ups, and IRA phase-outs.</p><div class="links"><a class="in" href="../../{TXK}">See the limits →</a></div></div>
<div class="card"><span class="pill" style="background:#1a7f37;color:#fff">Official</span><h3>🩺 HSA limits 2027</h3><p>$4,500 self-only, $9,000 family, plus HDHP rules.</p><div class="links"><a class="in" href="../../{TXH}">See HSA limits →</a></div></div>
<div class="card"><span class="pill" style="background:#1a7f37;color:#fff">Official</span><h3>🎁 Gift and estate tax 2027</h3><p>$20,000 gift exclusion and $15,480,000 estate exemption.</p><div class="links"><a class="in" href="../../{TXG}">See the numbers →</a></div></div>
<div class="card"><span class="pill">Due December</span><h3>🚗 IRS mileage rate 2027</h3><p>Still pending as of Nov 21, 2026. Current business rate: 76 cents.</p><div class="links"><a class="in" href="../../{TXM}">See mileage rates →</a></div></div>
<div class="card"><span class="pill" style="background:#1a7f37;color:#fff">Official</span><h3>💊 Medicare Part D cap 2027</h3><p>$2,400 out-of-pocket threshold and a $700 defined standard deductible, from the April 6 CMS rate announcement.</p><div class="links"><a class="in" href="../../{PDP}">See the Part D cap →</a></div></div>
</div>
<h2>🔍 How we label numbers</h2><p><b>Official</b> means the figure is in an agency revenue procedure, notice, fact sheet or news release, linked in the Source column. We do not publish projections as if they were figures. Where a number is not out yet, like the 2027 mileage rate, the Value cell says so.</p>
<h2>📅 Refresh calendar</h2><ul><li><b>April 6, 2026:</b> CMS Part D benefit parameters in the CY 2027 rate announcement ($2,400 threshold, $700 deductible).</li><li><b>October 14, 2026:</b> SSA 2027 COLA (3.6%).</li><li><b>November 5 and 12, 2026:</b> IRS inflation and retirement limits.</li><li><b>November 17, 2026:</b> CMS Part B premium.</li><li><b>December 2026 (expected):</b> IRS 2027 standard mileage rates.</li><li><b>January 2027:</b> filing season opens for 2026 returns; we refresh the tracker again.</li></ul>
{fhtml(XQ)}{tax_next("../../")}{taxrel("../../")}{srclist(XSRC)}</article>'''
XTITLE="2027 Official Numbers Tracker: Every Figure, Agency and Release Date"
XDESC="One table of 2027 IRS, SSA, CMS and state wage numbers with release dates, source links, CSV download and a cite-this box."
xld=[taxart(XTITLE,XDESC,TX,XSRC,mod="2026-11-21"),faqld(XQ),crumbs(TXCR),
{"@context":"https://schema.org","@type":"Dataset","name":"2027 official US money numbers tracker","description":"IRS, SSA, CMS and state minimum-wage figures for 2027 with agency, release date and source URL.","url":B+"/"+TX,"creator":{"@type":"Organization","name":"The Trends Incoming team","url":B+"/about/"},"isBasedOn":[u for _,u in XSRC],"temporalCoverage":"2027","spatialCoverage":"United States","isAccessibleForFree":True,"license":"https://creativecommons.org/licenses/by/4.0/","dateModified":"2026-11-21","distribution":[{"@type":"DataDownload","encodingFormat":"text/csv","contentUrl":B+"/"+TX+"2027-official-numbers.csv"}]},
{"@context":"https://schema.org","@type":"ItemList","name":"2027 tax numbers pages","itemListElement":[{"@type":"ListItem","position":i+1,"url":B+"/"+p,"name":n} for i,(n,p) in enumerate([("2027 standard deduction",TXS),("2027 tax brackets",TXB),("401(k) and IRA limits 2027",TXK),("HSA limits 2027",TXH),("Gift and estate tax 2027",TXG),("IRS mileage rate 2027",TXM)])]}]
page(TX+"index.html",XTITLE,XDESC,xbody,ld=xld,article=False,cat="money")
# ---------------- standard deduction (dedicated lookup) ----------------
SDQ=[
("What is the 2027 standard deduction for a single filer?","$16,600. Married people filing separate returns use the same $16,600. Both amounts are in IRS Revenue Procedure 2026-35, section 3.15, announced with news release IR-2026-133 on November 5, 2026."),
("What is the 2027 standard deduction for a married couple filing jointly?","$33,200, and a surviving spouse uses that same amount. IR-2026-133 says that is $1,000 more than 2026. Revenue Procedure 2025-32 set the 2026 joint amount at $32,200."),
("What is the 2027 head of household standard deduction?","$24,925. The 2026 amount in Revenue Procedure 2025-32 was $24,150. The difference between those two published figures is $775."),
("What is the extra standard deduction for age 65 or blindness in 2027?","Revenue Procedure 2026-35 sets the additional amount under section 63(f) for the aged or the blind at $1,700. The additional amount is $2,100 if the person is also unmarried and not a surviving spouse. For 2026 those amounts were $1,650 and $2,050."),
("What is the 2027 standard deduction cap for a dependent?","Someone who can be claimed as a dependent by another taxpayer cannot take more than the greater of $1,400, or $500 plus that person's earned income. For 2026 the cap was the greater of $1,350, or $450 plus earned income."),
("Do the 2027 amounts apply to the return filed in 2027?","No. IR-2026-133 says the tax year 2027 adjustments generally apply to returns filed in 2028. A return filed in 2027 is generally a 2026 return and uses the 2026 standard deduction."),
]
SDSRC=[S_IR133,S_RP2635,S_RP2532]
sbody=f'''<article><p class="by"><a href="../../">💵 Money</a> › <a href="../">2027 tax numbers</a> › Standard deduction 2027</p><span class="pill" style="background:#1a7f37;color:#fff">Official since Nov 5, 2026</span>
<h1>2027 Standard Deduction: $16,600 Single, $33,200 Joint, $24,925 Head of Household</h1><p class="by">{BY} · Published Nov 20, 2026 · Last updated Nov 20, 2026</p>
<p><b>Short answer, checked Nov 20, 2026:</b> for tax year 2027 the IRS standard deduction is <b>$16,600</b> for single filers and for married filing separately, <b>$33,200</b> for married filing jointly and surviving spouses, and <b>$24,925</b> for head of household. The additional amount for age 65 or blindness is <b>$1,700</b>, or <b>$2,100</b> if the person is unmarried and not a surviving spouse. Those figures are in <a href="{S_RP2635[1]}" rel="noopener" target="_blank">Revenue Procedure 2026-35</a>, section 3.15. <a href="{S_IR133[1]}" rel="noopener" target="_blank">News release IR-2026-133</a> (Nov 5, 2026) prints the three base amounts and says the joint figure is up $1,000 from 2026.</p>
{NOADV}
<table><tr><th>Filing status</th><th>2026, Rev. Proc. 2025-32</th><th>2027, Rev. Proc. 2026-35</th><th>Difference</th></tr>
<tr><td>Single; married filing separately</td><td>$16,100</td><td><b>$16,600</b></td><td>$500</td></tr>
<tr><td>Married filing jointly; surviving spouse</td><td>$32,200</td><td><b>$33,200</b></td><td>$1,000</td></tr>
<tr><td>Head of household</td><td>$24,150</td><td><b>$24,925</b></td><td>$775</td></tr>
<tr><td>Additional amount, aged or blind, married</td><td>$1,650</td><td><b>$1,700</b></td><td>$50</td></tr>
<tr><td>Additional amount, aged or blind, unmarried and not a surviving spouse</td><td>$2,050</td><td><b>$2,100</b></td><td>$50</td></tr>
<tr><td>Dependent cap: greater of this floor, or the earned-income add-on plus earned income</td><td>$1,350 floor, or $450 plus earned income</td><td><b>$1,400 floor, or $500 plus earned income</b></td><td>$50 on each piece</td></tr>
</table>
<p class="src">Base amounts also appear in IR-2026-133. The additional amounts and the dependent cap are in section 3.15 of each revenue procedure. The Difference column is subtraction of those two published figures, not a separate IRS release.</p>
{taxnav("../../../",TXS)}
{tax_compare("../../../",TXS)}
<h2>What the newsroom printed, and what it left in the PDF</h2>
<p>IR-2026-133 leads with three numbers: $33,200 joint, $16,600 single and married filing separately, and $24,925 head of household. It does not repeat the age or blindness add-on, and it does not repeat the dependent cap. Those sit in section 3.15 of Rev. Proc. 2026-35, the same procedure the news release points to for "details about these annual adjustments." The <a href="../2027-tax-brackets/">2027 tax brackets page</a> keeps a one-row version of the add-ons next to the rate tables. This page is the lookup for the deduction itself.</p>
{tax_next_mid("../../../",TXS)}
<h2>The additional amount for age or blindness</h2>
<p>Section 3.15(3) of Rev. Proc. 2026-35 says the additional standard deduction amount under Internal Revenue Code section 63(f), "for the aged or the blind," is $1,700 for 2027. It "is increased to $2,100 if the individual is also unmarried and not a surviving spouse." The 2026 procedure, Rev. Proc. 2025-32, used the same sentence with $1,650 and $2,050.</p>
<p>The procedure states that additional amount. It does not print a combined total for someone who is both 65 or older and blind. Section 63(f) is the code section the procedure cites for how the additional amount applies. This page does not add the figures together into a personal deduction.</p>
<h2>Dependents</h2>
<p>Section 3.15(2) caps the standard deduction of a person who may be claimed as a dependent by another taxpayer. For 2027 the cap is the greater of $1,400, or $500 plus that person's earned income. For 2026 it was the greater of $1,350, or $450 plus earned income. The same $1,400 figure shows up elsewhere in Rev. Proc. 2026-35 as the inflation-adjusted amount in section 63(c)(5)(A), which the procedure also uses in the kiddie-tax rules. That cross-reference is in section 3.02 of the 2027 procedure. It is a definition, not a suggestion about how a household should file.</p>
<h2>Which return these numbers belong on</h2>
<p>IR-2026-133 says the tax year 2027 adjustments generally apply to returns filed in 2028. The return most people file in spring 2027 is the 2026 return, and that return still uses the 2026 column above: $16,100, $32,200 and $24,150, from Rev. Proc. 2025-32.</p>
<p>The rate tables that sit on top of these deductions are on the <a href="../2027-tax-brackets/">2027 brackets page</a>, including the bracket calculator. Retirement caps for the same year are on the <a href="../401k-ira-limits-2027/">401(k) and IRA limits page</a>. The <a href="../">2027 official numbers tracker</a> lists every figure with the agency and the release date. Social Security's separate 2027 cost-of-living adjustment is on the <a href="../../social-security-2027/">COLA page</a>.</p>
{fhtml(SDQ)}{tax_next("../../../")}{taxrel("../../../")}{srclist(SDSRC)}</article>'''
SDTITLE="2027 Standard Deduction: $16,600 Single, $33,200 Joint, $24,925 Head of Household"
SDDESC="2027 standard deduction: $16,600 single, $33,200 joint, $24,925 head of household, plus $1,700 or $2,100 age and blindness add-ons."
assert len(SDDESC)<=155, len(SDDESC)
sdld=[taxart(SDTITLE,SDDESC,TXS,SDSRC,mod=MOD20),faqld(SDQ),crumbs(TXCR+[("Standard deduction 2027",TXS)])]
page(TXS+"index.html",SDTITLE,SDDESC,sbody,ld=sdld,article=False,cat="money")
LM.update({B+"/"+p:(MOD20 if p in (TX,TXB,TXS) else (MOD19 if p==TXM else PUB18B)) for p in (TX,TXB,TXK,TXH,TXM,TXG,TXS)})
TAXLINK='<div class="card picks" style="margin:14px 0"><span class="pill">2027 official numbers</span><h3>🧾 2027 official numbers tracker</h3><p>One table of IRS, SSA and CMS figures with release dates, a CSV download and a cite-this box.</p><div class="links"><a class="in" href="{r}money/2027-tax-numbers/">Open the tracker →</a><a class="in" href="{r}money/2027-tax-numbers/2027-tax-brackets/#calculator">Bracket calculator →</a></div></div>'
SUBX={"medicare-open-enrollment-2027":'<p>Comparing plans with a health savings account in mind? The <a href="../2027-tax-numbers/hsa-limits-2027/">2027 HSA limits</a> are official at $4,500 and $9,000. See every <a href="../2027-tax-numbers/">2027 official number</a> in one place, and the official <a href="../medicare-part-b-premium-2027/">2027 Medicare Part B premium</a>.</p>',
"retirement":'<p>Planning 2027 savings? See the official <a href="../2027-tax-numbers/401k-ira-limits-2027/">2027 401(k) and IRA limits</a>, the <a href="../2027-tax-numbers/2027-tax-brackets/">2027 tax brackets</a>, and the <a href="../2027-tax-numbers/">full 2027 tracker</a>.</p>'}
