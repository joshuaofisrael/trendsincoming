# --- 19 Nov 2026 SEO batch: image-policy, FAFSA deadlines, engagement helpers. exec'd from build.py ---
PUB19="2026-11-19"
CHK="checked Nov 19, 2026"

# Photo bank image for FAFSA (and any money page that opts in)
PHOTO.update({"hands-counting-notes":"Hands counting paper notes on a wooden desk in soft natural light"})
# FAFSA embeds its own captioned figure (links to /image-policy/); do not also KEYPH-inject.

# ---------- shared engagement helpers ----------
def nextreads(r, items, mid=False):
    """3-4 closely related next-reads with thumbnails. items: (href, title, blurb, thumb_src_from_root)."""
    cards=""
    for href,title,blurb,thumb in items:
        cards+=f'<a class="nrcard" href="{r}{href}"><img src="{r}{thumb}" width="320" height="180" alt="" loading="lazy" decoding="async"><span class="nrt"><b>{esc(title)}</b><br>{esc(blurb)}</span></a>'
    label="Keep reading" if mid else "Related next reads"
    return f'<section class="nr" aria-label="{label}"><h2>{label}</h2><div class="nrgrid">{cards}</div></section>'

def check_another(r, current=None):
    opts=[
        ("money/2027-tax-numbers/","2027 official numbers tracker"),
        ("money/2027-tax-numbers/2027-tax-brackets/","2027 tax brackets"),
        ("money/2027-tax-numbers/401k-ira-limits-2027/","401(k) and IRA limits 2027"),
        ("money/2027-tax-numbers/hsa-limits-2027/","HSA limits 2027"),
        ("money/2027-tax-numbers/gift-estate-tax-2027/","Gift and estate tax 2027"),
        ("money/2027-tax-numbers/irs-mileage-rate-2027/","IRS mileage rate 2027"),
        ("money/social-security-2027/","Social Security COLA 2027"),
        ("money/medicare-part-b-premium-2027/","Medicare Part B premium 2027"),
        ("money/minimum-wage-2027/","Minimum wage by state 2027"),
        ("money/fafsa-deadlines/","FAFSA 2027-28 deadlines"),
        ("money/open-enrollment-2027/","HealthCare.gov open enrollment 2027"),
    ]
    lis="".join(f'<li><a href="{r}{h}">{esc(t)}</a></li>' for h,t in opts if h!=current)
    return f'<aside class="compare" aria-label="Check another 2027 number"><h2>Check another 2027 number</h2><p>Official figures only, linked to the primary release.</p><ul>{lis}</ul></aside>'

MONEY_TH="og/money.png"
EDU_TH="og/education.png"
NR_TAX=[
    ("money/social-security-2027/","Social Security COLA 2027","Official 3.6% COLA, payment dates and taxable max.",MONEY_TH),
    ("money/medicare-part-b-premium-2027/","Medicare Part B premium 2027","$209.40 a month, official from CMS.",MONEY_TH),
    ("money/minimum-wage-2027/","Minimum wage by state 2027","Every January 1 raise, with a CSV download.",MONEY_TH),
    ("money/fafsa-deadlines/","FAFSA 2027-28 deadlines","Open date, federal deadline and state dates from the form.",EDU_TH),
]
NR_FAFSA=[
    ("money/2027-tax-numbers/","2027 official numbers tracker","Every 2027 IRS, SSA and CMS figure in one table.",MONEY_TH),
    ("money/open-enrollment-2027/","HealthCare.gov open enrollment 2027","Nov 1 to Jan 15 window and Dec 15 Jan coverage deadline.",MONEY_TH),
    ("money/2027-tax-numbers/hsa-limits-2027/","HSA limits 2027","Official $4,500 / $9,000 contribution limits.",MONEY_TH),
    ("money/social-security-2027/","Social Security COLA 2027","3.6% COLA and January payment dates.",MONEY_TH),
]

# ---------- image policy page ----------
IMG_POLICY=f'''<nav class="crumbs" aria-label="Breadcrumb"><a href="../">Home</a> &gt; <span>Image policy</span></nav>
<h1>Image policy</h1>
<p class="by">{BY} · Published {PUB19} · Last updated {PUB19}</p>
<p>Photos and illustrations on Trends Incoming are <b>AI-generated</b> unless a caption says otherwise. They are illustrative only. They are not photographs of real people, places or events, and they were not taken at any event we report on.</p>
<p>Each article photo carries a caption that says it is AI-generated and links back to this page. Category cards and OG images generated with our own text-only card tool are labelled as our own work in the site image provenance record.</p>
<h2>What we do not use</h2>
<ul>
<li>Photos of real, identifiable people without a clear right to use them</li>
<li>Brand logos, watermarks or readable product packaging as decorative art</li>
<li>Staged fake news scenes presented as documentary photos</li>
</ul>
<h2>Questions</h2>
<p>If you have a question about an image, use the <a href="../contact/">contact form</a> or email <a href="mailto:{EMAIL}">{EMAIL}</a>. See also our <a href="../about/#editorial-policy">editorial policy</a> and <a href="../copyright/">copyright page</a>.</p>
'''
LG.POLICY_PAGES.add("image-policy/")
page("image-policy/index.html","Image policy","Trends Incoming image policy: article photos are AI-generated illustrations, labelled in captions, and are not photos of real events.",IMG_POLICY,article=False,rel=False,ld=[
    {"@context":"https://schema.org","@type":"WebPage","name":"Image policy","url":B+"/image-policy/","publisher":pub,"datePublished":PUB19,"dateModified":PUB19},
    crumbs([("Home",""),("Image policy","image-policy/")]),
])

# ---------- FAFSA 2027-28 deadlines (stable URL, update in place each cycle) ----------
FF="money/fafsa-deadlines/"
S_ED=("U.S. Department of Education Homeroom: The 2027-28 FAFSA Form Is Here (Sept 24, 2026)","https://www.ed.gov/about/homeroom-blog/2027-28-fafsar-form-here-earlier-start-students-and-families")
S_EDPR=("U.S. Department of Education press release: earliest FAFSA launch for a second consecutive year","https://www.ed.gov/about/news/press-release/us-department-of-education-announces-earliest-fafsa-launch-program-history-second-consecutive-year")
S_PDF=("Federal Student Aid: 2027-28 FAFSA form PDF (deadlines pages)","https://studentaid.gov/sites/default/files/2027-28-fafsa-form.pdf")
S_TOOL=("Federal Student Aid Financial Aid Toolkit: 2027-28 FAFSA Form Now Available","https://financialaidtoolkit.ed.gov/tk/announcement-detail.jsp?id=fafsa-updates")
S_NASFAA=("NASFAA: FSA officially launches 2027-28 FAFSA","https://www.nasfaa.org/news-item/39879/FSA_Officially_Launches_2027-28_FAFSA")
FFSRC=[S_EDPR,S_ED,S_PDF,S_TOOL,S_NASFAA]
FFNOADV='<div class="warn"><b>No financial-aid advice.</b> This page restates official federal and state deadline language from Federal Student Aid and the Department of Education. Trends Incoming is not a college counselor. Confirm your school and state deadlines with your financial aid office or the linked primary sources before you act.</div>'
# Representative early state deadlines copied from the official 2027-28 FAFSA PDF (page 2), checked Nov 19, 2026
STATE_ROWS=[
("Texas","Jan 15, 2027 (priority consideration)"),
("California","March 2, 2027 (many state aid programs; GPA also due); Sept 2, 2027 for additional community college Cal Grants"),
("Connecticut","Feb 15, 2027 (priority consideration)"),
("Indiana","April 15, 2027 (Frank O'Bannon, 21st Century, Workforce Ready, Adult Student Grant)"),
("New York","June 30, 2028 (more forms may be required)"),
("Pennsylvania","May 1, 2027 (most applicants); Aug 1, 2027 (first-time applicants at listed open-admission / short programs)"),
("Florida","May 15, 2027 (date processed)"),
("Illinois","As soon as possible after Oct 1, 2026 (MAP awards while funds exist)"),
]
FFQ=[
("When did the 2027-28 FAFSA open?","The Department of Education made the 2027-28 FAFSA available the week of September 23 to 24, 2026. The Homeroom blog dated September 24, 2026 says the form is available nationwide at fafsa.gov. That beat the October 1 statutory floor."),
("What is the federal FAFSA deadline for 2027-28?","Federal Student Aid must receive your application no later than June 30, 2028. Your college must also have your correct, complete information by your last day of enrollment in the 2027-28 school year. The printed form still says not to submit earlier than October 1, 2026."),
("Why file before the federal deadline?","State and college aid often run out earlier, and some awards are first-come, first-served. The official form says state or college deadlines may be as early as October 1, 2026."),
("Where do I find my state's FAFSA deadline?","Page 2 of the official 2027-28 FAFSA PDF lists state deadlines. A short sample is on this page; always confirm on the PDF or with your state agency."),
("Is this financial-aid advice?","No. We restate official dates and link the primary sources. Talk to your school's financial aid office about your own situation."),
]
ff_state="".join(f"<tr><td>{esc(s)}</td><td>{esc(d)}</td></tr>" for s,d in STATE_ROWS)
ff_mid=nextreads("../../", NR_FAFSA[:4], mid=True)
ff_end=nextreads("../../", NR_FAFSA)
ffbody=f'''<article><p class="by"><a href="../">💵 Money</a> › FAFSA 2027-28 deadlines</p><span class="pill" style="background:#1a7f37;color:#fff">Form open · {CHK}</span>
<h1>FAFSA 2027-28: Open Date and Every Deadline That Matters</h1><p class="by">{BY} · Published {PUB19} · Last updated {PUB19}</p>
<figure class="ph"><img src="../../assets/img/hands-counting-notes.webp" width="1280" height="720" alt="{esc(PHOTO['hands-counting-notes'])}" fetchpriority="high" decoding="async"><figcaption><a href="../../image-policy/">AI-generated image</a></figcaption></figure>
<p><b>Short answer:</b> the <b>2027-28 FAFSA</b> is open now at <a href="https://fafsa.gov" rel="noopener" target="_blank">fafsa.gov</a>. The Department of Education launched it the week of <b>September 23 to 24, 2026</b>, the second year in a row it beat the October 1 floor. The federal deadline is <b>June 30, 2028</b>. State and school deadlines are often much earlier, so the federal date is usually the wrong one to plan around.</p>
{FFNOADV}
<table><tr><th>Award year</th><td>July 1, 2027 to June 30, 2028</td></tr>
<tr><th>Form opened</th><td>Week of Sept 23 to 24, 2026 (ED Homeroom Sept 24, 2026; press release and FSA toolkit)</td></tr>
<tr><th>Statutory earliest (paper form)</th><td>October 1, 2026</td></tr>
<tr><th>Federal receipt deadline</th><td>June 30, 2028</td></tr>
<tr><th>Apply</th><td><a href="https://fafsa.gov" rel="noopener" target="_blank">fafsa.gov</a></td></tr>
<tr><th>Status {CHK}</th><td>Open to the general public; no change to the federal deadline since launch</td></tr></table>
{check_another("../../", FF)}
<h2>Federal deadline, in the form's own words</h2>
<p>The official <a href="{S_PDF[1]}" rel="noopener" target="_blank">2027-28 FAFSA PDF</a> says: for federal aid, submit as early as possible, but no earlier than October 1, 2026, and Federal Student Aid must receive the application no later than June 30, 2028. Your college must have your correct, complete information by your last day of enrollment in the 2027-28 school year.</p>
<p>Online filing at fafsa.gov is what FSA recommends if you are close to a deadline.</p>
{ff_mid}
<h2>State deadlines (sample from the official PDF)</h2>
<p>These lines are copied from the state-deadline pages of the same PDF ({CHK}). They are not a complete list. "As soon as possible" and "while funds exist" appear for several states, which is why filing early still matters even when a calendar date looks late.</p>
<div style="overflow-x:auto"><table><tr><th>State</th><th>Deadline language on the 2027-28 FAFSA PDF</th></tr>{ff_state}</table></div>
<p class="src">Full table: <a href="{S_PDF[1]}" rel="noopener" target="_blank">studentaid.gov 2027-28 FAFSA form PDF</a>. Schools can set earlier priority dates of their own.</p>
<h2>School deadlines</h2>
<p>Colleges often set priority filing dates for institutional aid that are earlier than both the federal and state dates. The form tells applicants to check with a high school counselor or the financial aid office at each college listed. List every school you are considering on the FAFSA so those offices can pull your data.</p>
<h2>What changed this cycle</h2>
<p>ED's Homeroom post (Sept 24, 2026) highlights real-time Student Aid Index and Pell Grant results for most filers, reusable parent information across siblings, a QR-code contributor invite, and clearer instructions. None of that changes the deadline math: early filing still wins for limited state and campus funds.</p>
<p>Also planning 2027 money? See the <a href="../2027-tax-numbers/">2027 official numbers tracker</a> and <a href="../open-enrollment-2027/">HealthCare.gov open enrollment dates</a>.</p>
{fhtml(FFQ)}
{ff_end}
{srclist(FFSRC)}</article>'''
FFTITLE="FAFSA 2027-28: Open Date and Every Deadline That Matters"
FFDESC="2027-28 FAFSA is open (launched week of Sept 23-24, 2026). Federal deadline June 30, 2028, plus state dates from the official form."
ffld=[
    {"@context":"https://schema.org","@type":"Article","headline":FFTITLE,"description":FFDESC,"datePublished":PUB19,"dateModified":PUB19,"mainEntityOfPage":B+"/"+FF,"author":{"@type":"Organization","name":"The Trends Incoming team","url":B+"/about/"},"publisher":pub,"citation":[u for _,u in FFSRC],"image":B+"/assets/img/og-hands-counting-notes.jpg","about":{"@type":"Thing","name":"FAFSA 2027-28 deadlines"}},
    faqld(FFQ),
    crumbs([("Home",""),("Money","money/"),("FAFSA 2027-28 deadlines",FF)]),
]
page(FF+"index.html",FFTITLE,FFDESC,ffbody,ld=ffld,article=False,cat="money")

# Point the education FAFSA trend card at the new stable guide
for i,t in enumerate(T):
    if "FAFSA" in t[1]:
        T[i]=(t[0],t[1],t[2],t[3],t[4],t[5],FF,t[7] if len(t)>7 else 0)
        break

HUBMAP[FF]=("money-benefits","2026-09-23","FAFSA 2027-28 deadlines","Open date, federal deadline June 30, 2028, and state dates from the official form.")
if "LM" in globals():
    LM.update({B+"/"+FF:PUB19, B+"/image-policy/":PUB19})
