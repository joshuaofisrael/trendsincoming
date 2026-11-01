# Daily update, Sun Nov 1, 2026 (PA batch). Every fact opened on the linked ESPN page on Nov 1.
_E1="https://www.espn.com/wnba/story/_/id/50343701/golden-state-valkyries-win-game-7-secure-first-wnba-title"
G7R_SRC=[("ESPN: Golden State Valkyries win Game 7, secure first WNBA title (Oct 31)",_E1)]
for _s in ("wnba-finals-game-7-2026","wnba-finals-2026"):
    for i,sb in enumerate(SUBS):
        if sb[1]==_s: SUBS[i]=(sb[0],sb[1],sb[2],sb[3],sb[4],G7R_SRC+list(sb[5]))
_subrep("wnba-finals-game-7-2026",[s for s in SUBS if s[1]=="wnba-finals-game-7-2026"][0][:3]+("The Golden State Valkyries beat the Atlanta Dream 68-63 in Game 7 on Oct 31 to win their first WNBA title, 4-3. Gabby Williams scored 30 and was named Finals MVP, per ESPN.",)+[s for s in SUBS if s[1]=="wnba-finals-game-7-2026"][0][4:])
STITLE.update({"wnba-finals-game-7-2026":"WNBA Finals Game 7: Valkyries beat Dream 68-63 for first title",
"wnba-finals-2026":"WNBA Finals 2026: Valkyries win the title in Game 7, every result"})
SDESC.update({"wnba-finals-game-7-2026":"Golden State beat Atlanta 68-63 in the first Game 7 in WNBA Finals history. Gabby Williams scored 30, 28 in the second half, and was named Finals MVP, per ESPN.",
"wnba-finals-2026":"The Golden State Valkyries are 2026 WNBA champions after a 68-63 Game 7 win over the Atlanta Dream on Oct 31. Finals MVP Gabby Williams scored 30. Every result."})
_g7=SUBDEEP["wnba-finals-game-7-2026"]
_g7["intro"]=f"<b>The Golden State Valkyries are WNBA champions.</b> They beat the Atlanta Dream <b>68-63</b> on Saturday, October 31, at Chase Center in the first Game 7 in WNBA Finals history, winning the series 4-3, per <a href=\"{_E1}\" {EXT}>ESPN</a>. Gabby Williams scored 30 points, 28 of them in the second half, and was named Finals MVP."
_g7["facts"]=[("Final score","Valkyries 68, Dream 63"),("Series","Valkyries win 4-3"),("Finals MVP","Gabby Williams, 30 points (28 in the second half)"),("Where","Chase Center, San Francisco, Sat Oct 31"),("History","First Game 7 in WNBA Finals history"),("Franchise","Golden State's first title, in its second season")]
_g7["body"]=f'''<h2>How Golden State won it</h2><p>Williams took over after halftime. She outscored the Dream 15-14 by herself in the third quarter and ran off 15 straight points across the third and fourth, which ESPN, citing Elias, says no player had done in a WNBA Finals game before. Her 30 points tied the record for a winner-take-all Finals game, and her 28 in the second half were the most in any half of a WNBA postseason game, per <a href="{_E1}" {EXT}>ESPN</a>.</p>
<h2>Why it is a landmark</h2><p>Per ESPN and Elias, the Valkyries are the third team across the NBA, BAA and WNBA to win a title within their first two seasons, and the first WNBA champion without a single All-WNBA selection that season. Williams also had three 25-point games in the series, tied for the most in a single WNBA Finals.</p>
<h2>Keep reading</h2><ul><li><a href="../wnba-finals-2026/">Every Finals result</a></li><li><a href="{R2}news/november-2026-whats-coming/">What's coming in November 2026</a></li></ul>'''
_g7["faq"]=[("Who won the 2026 WNBA Finals?","The Golden State Valkyries, who beat the Atlanta Dream 68-63 in Game 7 on October 31, 2026, to win the series 4-3, per ESPN."),("Who was the 2026 WNBA Finals MVP?","Gabby Williams of the Valkyries. She scored 30 points in Game 7, 28 of them in the second half."),("Is this the Valkyries' first WNBA title?","Yes. Golden State won it in the franchise's second season."),("Was this the first Game 7 in WNBA Finals history?","Yes, per ESPN.")]
_wf=SUBDEEP["wnba-finals-2026"]
_wf["intro"]=f"<b>The Golden State Valkyries won the 2026 WNBA Finals,</b> beating the Atlanta Dream 68-63 in Game 7 on October 31 to take the series 4-3, per <a href=\"{_E1}\" {EXT}>ESPN</a>. Gabby Williams was Finals MVP. <a href=\"../wnba-finals-game-7-2026/\">Game 7 recap</a>."
_wf["facts"]=[("Champion","Golden State Valkyries (first title)"),("Series","Valkyries win 4-3"),("Game 7","Valkyries 68, Dream 63, Sat Oct 31"),("Finals MVP","Gabby Williams")]+[f for f in _wf["facts"] if f[0] not in("Series","Champion","Game 7","Finals MVP")]
_wf["faq"]=[("Who won the 2026 WNBA championship?","The Golden State Valkyries beat the Atlanta Dream 4-3, winning Game 7 68-63 on October 31, 2026, per ESPN.")]+[q for q in _wf["faq"] if "Game 7" not in q[0] and "tied" not in q[1]]
HUBMAP["sports/wnba-finals-game-7-2026/"]=("sports","2026-10-31","Valkyries win WNBA title","68-63 in Game 7; Williams Finals MVP.")
