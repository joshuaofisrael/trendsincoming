# --- 2026-10-30 Holiday restaurant gift card bonus desk (Trend Bot brief). Every offer re-read on the chain's own page on Oct 30, 2026. ---
GCP="money/holiday-gift-card-bonus-deals-2026/"
GCV="Oct 30, 2026"
GC_S=[("Applebee's: holiday gift card deals, buy $50 get a $10 bonus card","https://www.applebees.com/en/gift-cards/holiday"),
("Landry's: gift card terms and conditions, 2026 holiday reward card tiers","https://www.landrysinc.com/gift-card-overview/giftcard-faq"),
("Saltgrass Steak House: holiday gift cards","https://www.saltgrass.com/event/holiday-gift-cards/"),
("McCormick & Schmick's: holiday gift cards","https://www.mccormickandschmicks.com/event/holiday-gift-cards/"),
("Lou Malnati's: holiday gift cards and bonus certificates","https://www.loumalnatis.com/holidaybonus/"),
("Atlas Restaurant Group: gift card FAQ, 2026 holiday eGift promotion (PDF)","https://atlasrestaurantgroup.com/wp-content/uploads/2026/10/FAQ-Gift-Cards.pdf")]
# chain, buy, bonus, per100, window, usable, blackouts, where, link
GCO=[
("Applebee's","$50","$10 bonus card",20,"Oct 12, 2026 to Jan 3, 2027","Expiry printed on the bonus card; check your card terms","Per bonus card terms","Online and in restaurant (participating locations)",GC_S[0][1]),
("Lou Malnati's","$100 ($50 earns $10)","$25 bonus certificate",25,"Nov 16 to Dec 31, 2026","Jan 2 to Feb 28, 2027","Not on tastesofchicago.com; one per transaction","Online and in restaurant",GC_S[4][1]),
("Atlas Restaurant Group","$100 ($50 earns $10)","$25 bonus eGift card",25,"Nov 3 to Dec 31, 2026","Next visit through Jun 30, 2027","Not for tax, tips or delivery fees","Online only (eGift cards)",GC_S[5][1]),
("Landry's Tier 1 (Saltgrass, Bubba Gump, Rainforest Cafe, Joe's Crab Shack and more)","$50","$10 reward card",20,"Oct 1 to Dec 31, 2026","Jan 1 to Mar 31, 2027","Feb 12 to 14, 2027 and Restaurant Week offers; $25 minimum food purchase; $500 per household cap","Online and in restaurant",GC_S[2][1]),
("Landry's Tier 2 (McCormick & Schmick's, Del Frisco's Grille, Chart House and more)","$100","$20 reward card",20,"Oct 1 to Dec 31, 2026","Jan 1 to Mar 31, 2027","Feb 12 to 14, 2027 and Restaurant Week offers; $500 per household cap","Online and in restaurant",GC_S[3][1]),
]
GCO.sort(key=lambda o:-o[3])
GCF=[("What is the best restaurant gift card bonus for 2026?","On the offers we confirmed, Lou Malnati's and Atlas Restaurant Group give the most: a $25 bonus for every $100 in gift cards, worth $25 per $100. Applebee's and the Landry's restaurants give $20 per $100."),
("What is the Applebee's gift card deal for 2026?","Applebee's gives a $10 bonus card when you buy $50 in gift cards, online or in participating restaurants, from October 12, 2026 to January 3, 2027, according to its holiday gift card page. The bonus card has its own expiry and restrictions printed on the card."),
("When can I use my bonus card?","Most bonus cards do not work in December. Landry's reward cards work January 1 to March 31, 2027, except February 12 to 14. Lou Malnati's bonus cards work January 2 to February 28, 2027. Atlas bonus eGift cards work from your next visit until June 30, 2027."),
("Is a bonus card the same as a gift card?","No. The gift card you buy keeps its value, but the bonus or reward card is a promotional card with its own dates, minimum spend and blackout days. If it expires unused, it is worth nothing."),
("Where are Chili's, Outback, Olive Garden, Panera and Starbucks?","We checked their official gift card pages on October 30, 2026 and found no 2026 holiday bonus offer posted yet. We add a chain only after its own page confirms the offer, and we recheck twice a week through Black Friday.")]
GC_IL={"@context":"https://schema.org","@type":"ItemList","name":"2026 holiday restaurant gift card bonus offers","numberOfItems":len(GCO),"itemListElement":[{"@type":"ListItem","position":i+1,"name":f"{o[0]}: buy {o[1]}, get {o[2]}","url":o[8]} for i,o in enumerate(GCO)]}
GC_ROWS="".join(f'<tr><td><b>{esc(o[0])}</b></td><td>{esc(o[1])}</td><td>{esc(o[2])}</td><td data-v="{o[3]}">${o[3]}</td><td>{esc(o[4])}</td><td>{esc(o[5])}</td><td>{esc(o[6])}</td><td>{esc(o[7])}</td><td><a href="{o[8]}" rel="noopener" target="_blank">Official page</a></td><td>{GCV}</td></tr>' for o in GCO)
GC_BODY=f'''<article><span class="pill">Buy windows open now</span><h1>Holiday Gift Card Bonus Deals 2026: Every Restaurant Offer</h1><p class="by">{BY} · Every offer checked {GCV} on the restaurant's own page</p>
<p><b>Short answer:</b> the best confirmed 2026 restaurant gift card bonuses are <b>Lou Malnati's</b> and <b>Atlas Restaurant Group</b> at <b>$25 per $100</b>, then <b>Applebee's</b> (buy $50, get $10, through Jan 3, 2027) and the <b>Landry's</b> restaurants (Saltgrass, McCormick &amp; Schmick's, Del Frisco's Grille and more) at <b>$20 per $100</b>. Most bonus cards only work in early 2027, so they are a reward for you, not part of the gift.</p>
<p>Jump to: <a href="#table">the full table</a> · <a href="#best">best deal for your own dining</a> · <a href="#rules">bonus card rules</a> · <a href="#notyet">chains not posted yet</a></p>
<h2 id="table">Every confirmed offer</h2><p>Tap a column heading to sort. "Bonus per $100" is the bonus you get for each $100 spent on gift cards.</p>
<div class="tw"><table class="sortable"><thead><tr><th>Chain</th><th>Buy</th><th>Bonus</th><th>Bonus per $100</th><th>Buy window</th><th>Bonus usable</th><th>Blackouts and limits</th><th>Online or in store</th><th>Official link</th><th>Verified on</th></tr></thead><tbody>{GC_ROWS}</tbody></table></div>
<h2 id="best">Best deal for your own dining</h2><ol>
<li><b>Lou Malnati's, $25 per $100.</b> Best if you eat Chicago deep dish anyway. Buy from Nov 16, use the bonus Jan 2 to Feb 28, 2027.</li>
<li><b>Atlas Restaurant Group, $25 per $100.</b> The longest window: bonus eGift cards last until June 30, 2027. Online eGift cards only.</li>
<li><b>Applebee's, $20 per $100.</b> The widest reach and the longest buy window, through January 3, 2027.</li>
<li><b>Landry's, $20 per $100.</b> One reward card works across many brands, but it needs a minimum food purchase, skips Feb 12 to 14, and caps the promotion at $500 per household.</li></ol>
<h2 id="rules">Bonus card rules to know</h2><ul><li>The bonus card is separate from the gift card. It has its own start date, end date and limits.</li><li>Most bonus cards do not work in December. Put the first and last usable day in your calendar.</li><li>Many require a minimum food purchase and allow one card per table or visit.</li><li>Online purchases usually email the bonus to the buyer, not the gift recipient.</li></ul>
<h2 id="notyet">Chains not posted yet</h2><p>On {GCV} we checked the official gift card pages for <b>Chili's, Outback Steakhouse, Olive Garden, Panera Bread and Starbucks</b> and found no 2026 holiday bonus offer. We add each chain only once its own page confirms dates and terms, and recheck twice a week through Black Friday, Nov 27.</p>
{nyfh(GCF)}
<h2>More holiday money guides</h2><ul><li><a href="../../shopping/thanksgiving-dinner-deals-2026/">Thanksgiving 2026 dinner deals compared</a></li><li><a href="../../shopping/veterans-day-free-meals-deals-2026/">Veterans Day 2026 free meals and deals</a></li><li><a href="../../shopping/thanksgiving-black-friday-store-hours-2026/">Thanksgiving and Black Friday store hours 2026</a></li><li><a href="../../hubs/money-benefits/">All money and benefits guides</a></li><li><a href="../../hubs/coming-up/">Coming Up calendar</a></li></ul>
{srclist(GC_S)}</article>'''
page(GCP+"index.html","Holiday Gift Card Bonus Deals 2026: Every Restaurant Offer","Buy $50, get $10 and better. Every 2026 restaurant gift card bonus with dates, blackout days and when bonus cards work.",GC_BODY,ld=[GC_IL,nyfaq(GCF)],cat="shopping")
# sortable tables
JS+=r"""
(function(){document.querySelectorAll('table.sortable').forEach(function(t){t.querySelectorAll('th').forEach(function(h,i){h.style.cursor='pointer';h.addEventListener('click',function(){var b=t.tBodies[0],rs=[].slice.call(b.rows),a=h.dataset.a!=='1';h.dataset.a=a?'1':'0';rs.sort(function(x,y){var p=x.cells[i],q=y.cells[i],u=p.dataset.v,v=q.dataset.v;var r=(u!==undefined&&v!==undefined)?(u-v):p.textContent.localeCompare(q.textContent);return a?r:-r});rs.forEach(function(r){b.appendChild(r)})})})})})();
"""
# cross links
GCLINK=lambda r:f'<p class="warn">🎁 <b>Gift card bonuses:</b> <a href="{r}{GCP}">every 2026 restaurant gift card bonus deal</a>, from Applebee\'s buy $50 get $10 to $25 per $100 at Lou Malnati\'s, with the dates bonus cards work.</p>'
page(TGP+"index.html","Thanksgiving 2026 Dinner Deals: Aldi, Lidl, Target, Walmart Compared","Every 2026 Thanksgiving meal bundle and turkey price side by side, cost per person, what's included and start dates. Updated as stores post.",TG_BODY.replace("<h2>Quick answers</h2>",GCLINK("../../")+"<h2>Quick answers</h2>",1),ld=TG_LD,cat="shopping")
page(VDP+"index.html","Veterans Day 2026 Free Meals and Deals (Verified List, Nov 11)","Every verified Veterans Day 2026 free meal and discount for veterans and active duty, with proof of service rules and official links. Updated daily to Nov 11.",VD_BODY.replace("<h2>Quick answers</h2>",GCLINK("../../")+"<h2>Quick answers</h2>",1),ld=VD_LD,cat="shopping")
if "thanksgiving-black-friday-store-hours-2026" in SUBDEEP: SUBDEEP["thanksgiving-black-friday-store-hours-2026"]["body"]=GCLINK("../../")+SUBDEEP["thanksgiving-black-friday-store-hours-2026"]["body"]
else: print("WARN no SUBDEEP store hours")
