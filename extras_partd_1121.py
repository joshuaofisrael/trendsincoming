# --- 21 Nov 2026: Medicare Part D out-of-pocket cap and standard deductible for 2027.
# Figures only as printed by CMS (CY 2027 Rate Announcement, April 6, 2026, Attachment V)
# and restated on Medicare.gov (pages checked Nov 21, 2026). No estimates.
PUB21="2026-11-21"
PD="money/medicare-part-d-out-of-pocket-cap-2027/"
PHOTO["pharmacy-counter-bags"]="A pharmacy counter with plain paper bags in soft daylight"
KEYPH[PD]="pharmacy-counter-bags"
S_ANN=("CMS: Announcement of CY 2027 MA Capitation Rates and Part C and Part D Payment Policies (April 6, 2026), Attachment V","https://www.cms.gov/files/document/2027-announcement.pdf")
S_MCOST=("Medicare.gov: How much does Medicare drug coverage cost? (checked Nov 21, 2026)","https://www.medicare.gov/health-drug-plans/part-d/basics/costs")
S_MBASE=("Medicare.gov: Medicare costs, Part D out-of-pocket limit (checked Nov 21, 2026)","https://www.medicare.gov/basics/costs/medicare-costs")
S_MPP=("Medicare.gov: What's the Medicare Prescription Payment Plan? (fact sheet, $2,400 in 2027)","https://www.medicare.gov/publications/12211-whats-the-medicare-prescription-payment-plan-.pdf")
PDSRC=[S_ANN,S_MCOST,S_MBASE,S_MPP]
PDNOADV='<div class="warn"><b>No personal advice.</b> This page restates the 2027 Part D figures CMS and Medicare.gov have published. Trends Incoming is not an insurance agent. Nothing here is Medicare, tax or financial advice for any person\'s situation. Medicare.gov Plan Finder is the comparison tool on the agency site.</div>'
PDQ=[
("What is the Medicare Part D out-of-pocket cap for 2027?","$2,400. CMS calls it the annual out-of-pocket threshold in Attachment V of the April 6, 2026 rate announcement. Medicare.gov's cost pages, checked November 21, 2026, use the same figure and say covered Part D drugs have no out-of-pocket charge for the rest of the calendar year once spending reaches it."),
("What is the 2027 Medicare Part D deductible?","$700 in the defined standard benefit, up from $615 in 2026, in the same CMS tables. Medicare.gov states the rule for plans a different way: no Medicare drug plan may have a deductible more than $700 in 2027, and some plans have no deductible."),
("Are the $700 and the $2,400 the same kind of number?","No. $700 is the deductible in the defined standard benefit, and the most a plan is allowed to set. $2,400 is the annual out-of-pocket threshold. After that threshold, Medicare.gov says you pay nothing out of pocket for covered Part D drugs for the rest of the year."),
("Did CMS print a formula, or only the results?","Both. Section C of Attachment V says the 2027 deductible is the 2026 amount of $615 multiplied by the 2027 annual percentage increase and rounded to the nearest $5, and the threshold is the 2026 amount of $2,100 multiplied by that increase and rounded to the nearest $50. Table V-1 lists the 2027 annual percentage increase at 13.65 percent. Tables V-2 and V-6 print the results: $700 and $2,400."),
("Does the $2,400 include the plan premium?","Medicare.gov lists the monthly premium as its own line, separate from the yearly out-of-pocket limit. The prescription payment plan fact sheet says a person who uses that option keeps paying the plan premium each month, and that covered-drug out-of-pocket costs are capped at $2,400 in 2027."),
("Is this Medicare advice?","No. It is the published CMS and Medicare.gov figures, with links. A plan's own deductible can be lower than $700, and copays can differ by tier."),
]
pd_mid=nextreads("../../", [
    ("money/medicare-part-b-premium-2027/","Medicare Part B premium 2027","$209.40 a month, from the Nov 17 CMS fact sheet.","og/money.png"),
    ("money/medicare-open-enrollment-2027/","Medicare open enrollment 2027","The Oct 15 to Dec 7 window for 2027 coverage.","og/money.png"),
    ("money/social-security-2027/","Social Security COLA 2027","Official 3.6% COLA and January payment dates.","og/money.png"),
    ("money/2027-tax-numbers/","2027 official numbers tracker","Part D now sits next to Part B, COLA and the IRS rows.","og/money.png"),
], mid=True)
pd_end=nextreads("../../", [
    ("blog/medicare-open-enrollment-2027-starter/","Open enrollment starter","What the Dec 7 deadline covers, and what it does not.","og/money.png"),
    ("blog/social-security-cola-2027-explained/","How the 2027 COLA works","The 3.6% increase, in plain language, with the SSA release.","og/money.png"),
    ("money/open-enrollment-2027/","HealthCare.gov open enrollment","A different program, Nov 1 to Jan 15.","og/money.png"),
    ("money/retirement/","Retirement and Social Security","COLA, Part B and the 2027 savings limits on one hub.","og/money.png"),
])
pdbody=f'''<article><p class="by"><a href="../">💵 Money</a> › <a href="../retirement/">Retirement & Social Security</a> › Medicare Part D cap 2027</p><span class="pill" style="background:#1a7f37;color:#fff">CMS rate announcement, April 6, 2026</span>
<h1>Medicare Part D Cap 2027: $2,400 Out of Pocket, $700 Deductible</h1><p class="by">{BY} · Published Nov 21, 2026 · Figures checked against CMS and Medicare.gov on Nov 21, 2026</p>
<p><b>Short answer:</b> for 2027 the Medicare Part D annual out-of-pocket threshold is <b>$2,400</b>, and the defined standard deductible is <b>$700</b>. Both numbers are in Attachment V of the <a href="{S_ANN[1]}" rel="noopener" target="_blank">CY 2027 Rate Announcement</a> CMS dated April 6, 2026. <a href="{S_MCOST[1]}" rel="noopener" target="_blank">Medicare.gov's drug-cost page</a>, checked November 21, 2026, still shows the same pair: no drug plan may set a deductible above $700 in 2027, and out-of-pocket spending on covered Part D drugs reaches catastrophic coverage at $2,400.</p>
{PDNOADV}
<table><tr><th>2027 out-of-pocket threshold</th><td><b>$2,400</b> (2026: $2,100)</td></tr><tr><th>2027 defined standard deductible</th><td><b>$700</b> (2026: $615)</td></tr><tr><th>Plan deductible ceiling</th><td>Medicare.gov: no drug plan may charge more than $700 in 2027. Some plans charge less, or nothing.</td></tr><tr><th>After the threshold</th><td>No out-of-pocket charge for covered Part D drugs for the rest of the calendar year</td></tr><tr><th>Where CMS printed it</th><td>Tables V-2 and V-6, Attachment V</td></tr><tr><th>Annual percentage increase used</th><td>13.65% (Table V-1 and Table V-4)</td></tr></table>
{check_another("../../", PD)}
<h2>Two numbers, two jobs</h2>
<p>The easy mix-up is treating $700 and $2,400 as rivals for the same slot. They are not. The deductible is what a person pays at the start of the year, before the plan shares the cost, and only if that plan has a deductible. The threshold is the yearly ceiling on out-of-pocket spending for covered Part D drugs. Medicare.gov's cost table lists the 2027 out-of-pocket limit as $2,400 and says that figure includes the deductible, other out-of-pocket spending, and certain payments made on a person's behalf, such as through Extra Help.</p>
<p>A plan can sit under the deductible ceiling. Medicare.gov says some plans have no deductible at all. It cannot sit over it. The $700 in the CMS defined-standard table is also the number Medicare.gov uses as that ceiling.</p>
{pd_mid}
<h2>How CMS moved the 2026 numbers to 2027</h2>
<p>Attachment V does not ask anyone to guess. Section C says the defined standard deductible for 2027 is the 2026 amount of $615 multiplied by the 2027 annual percentage increase, then rounded to the nearest multiple of $5. The out-of-pocket threshold is the 2026 amount of $2,100 multiplied by that same increase, then rounded to the nearest multiple of $50. Table V-1 and Table V-4 both put the 2027 annual percentage increase at 13.65 percent. Tables V-2 and V-6 then print the rounded results side by side with 2026.</p>
<table><tr><th></th><th>2026</th><th>2027</th></tr><tr><td>Defined standard deductible</td><td>$615</td><td><b>$700</b></td></tr><tr><td>Out-of-pocket threshold</td><td>$2,100</td><td><b>$2,400</b></td></tr><tr><td>Defined standard coinsurance after the deductible, non-LIS</td><td>25%</td><td>25%</td></tr></table>
<p class="src">CMS, CY 2027 Rate Announcement, Attachment V, Tables V-2 and V-6, April 6, 2026. The 25 percent coinsurance is the defined standard benefit in Table V-6. A real plan can use copays or different tier percentages. Its own Annual Notice of Change is the document that shows which.</p>
<h2>The three stages Medicare.gov describes for 2027</h2>
<p>Medicare.gov's drug-cost page, checked November 21, 2026, still describes three stages, and it prints the 2027 dollars in parentheses next to the 2026 ones.</p>
<ol>
<li><b>Deductible.</b> If the plan has one, the enrollee pays the drug costs until that deductible is met. The page says no plan's deductible may be more than $615 in 2026 or $700 in 2027.</li>
<li><b>Initial coverage.</b> After the deductible, the page says the enrollee pays 25 percent coinsurance for generic and brand-name drugs until out-of-pocket spending on covered Part D drugs reaches $2,100 in 2026 or $2,400 in 2027, counting certain payments made on the enrollee's behalf. That is the handoff to catastrophic coverage.</li>
<li><b>Catastrophic coverage.</b> The same page says there is no out-of-pocket charge for covered Part D drugs for the rest of the calendar year.</li>
</ol>
<p>The <a href="{S_MBASE[1]}" rel="noopener" target="_blank">Medicare costs table</a> states the yearly Part D out-of-pocket limit as "$2,100 (in 2026) ($2,400 in 2027)" and uses the same "includes the deductible and certain payments made on your behalf" wording.</p>
<h2>The premium is a separate line</h2>
<p>Medicare.gov lists the monthly premium on its own, above the deductible and the yearly limit. The <a href="{S_MPP[1]}" rel="noopener" target="_blank">Medicare Prescription Payment Plan fact sheet</a> is about spreading pharmacy bills across the year, and it is explicit on the ceiling: in one calendar year a person using that option never pays more than the amount they would have paid at the pharmacy, and never more than the out-of-pocket maximum for covered drugs, which the sheet sets at $2,400 in 2027. The same sheet says the plan premium, if there is one, is still paid every month. The cap is a drug-cost ceiling. It is not a premium waiver.</p>
<h2>Extra Help copays in the same CMS tables</h2>
<p>People with the full low-income subsidy do not use the $700 deductible. Table V-2 of the rate announcement sets their 2027 deductible at $0 and prints maximum copays up to the out-of-pocket threshold:</p>
<table><tr><th>Full subsidy group, 2027</th><th>Generic or preferred multi-source</th><th>Other drugs</th></tr>
<tr><td>Institutionalized, or receiving home and community-based services</td><td>$0</td><td>$0</td></tr>
<tr><td>Full-benefit dual eligible, income at or under 100% of the poverty line</td><td>$1.65</td><td>$5.00</td></tr>
<tr><td>Full-benefit dual eligible between 100% and 150% of poverty, and the other full-subsidy non-dual group in Table V-2</td><td>$5.80</td><td>$14.40</td></tr>
</table>
<p class="src">2026 copays in the same table were $1.60 and $4.90 for the at-or-under-100% group, and $5.10 and $12.65 for the higher full-subsidy group. The 2027 out-of-pocket threshold those copays run up to is the same $2,400.</p>
<h2>Why the page exists in November</h2>
<p><a href="../medicare-open-enrollment-2027/">Medicare open enrollment</a> runs through December 7, 2026, for coverage that starts January 1, 2027. The Part D parameters themselves have been in the rate announcement since April. They are on this page because that window is when plan materials and Medicare.gov's cost pages are the ones people compare, and because the <a href="../2027-tax-numbers/">2027 numbers tracker</a> had Part B and not Part D. The Part B premium, a different CMS release, is <a href="../medicare-part-b-premium-2027/">$209.40 a month</a>.</p>
<p>HealthCare.gov enrollment is a different program with different dates. Those dates are on the <a href="../open-enrollment-2027/">HealthCare.gov open enrollment page</a>.</p>
{fhtml(PDQ)}
{pd_end}
{srclist(PDSRC)}</article>'''
PDTITLE="Medicare Part D Cap 2027: $2,400 Out of Pocket, $700 Deductible"
PDDESC="The 2027 Part D out-of-pocket threshold is $2,400 and the standard deductible is $700, from the CMS rate announcement of April 6, 2026."
assert len(PDDESC)<=155, len(PDDESC)
pdld=[
{"@context":"https://schema.org","@type":"Article","headline":PDTITLE,"description":PDDESC,"datePublished":PUB21,"dateModified":PUB21,"mainEntityOfPage":B+"/"+PD,"author":{"@type":"Organization","name":"The Trends Incoming team","url":B+"/about/"},"publisher":pub,"citation":[u for _,u in PDSRC],"about":{"@type":"Thing","name":"2027 Medicare Part D out-of-pocket threshold"}},
faqld(PDQ),
crumbs([("Home",""),("Money","money/"),("Retirement & Social Security","money/retirement/"),("Medicare Part D cap 2027",PD)]),
]
HUBMAP[PD]=("money-benefits","2027-01-01","Medicare Part D cap 2027","The 2027 out-of-pocket threshold is $2,400 and the defined standard deductible is $700.")
page(PD+"index.html",PDTITLE,PDDESC,pdbody,ld=pdld,article=False,cat="money")
PDLINK='<div class="card picks" style="margin:14px 0"><span class="pill" style="background:#1a7f37;color:#fff">Official: $2,400</span><h3>💊 Medicare Part D cap 2027</h3><p>The $2,400 out-of-pocket threshold and the $700 defined standard deductible, from the April 6 CMS rate announcement.</p><div class="links"><a class="in" href="{r}money/medicare-part-d-out-of-pocket-cap-2027/">See the cap →</a></div></div>'
SDESC["medicare-open-enrollment-2027"]="Oct 15 to Dec 7, 2026 is Medicare open enrollment for 2027 Advantage and Part D plans. Separate from HealthCare.gov."
