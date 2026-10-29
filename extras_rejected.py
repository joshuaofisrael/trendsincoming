# Legal-hold decisions (Joshua via Personal assistant, 29 Oct 2026): q19, q20, q23, q26 REJECTED, removed from the build.
_REJ_CARDS={"Israel votes today","DOJ sues over Alaska Senate certification"}
T[:]=[t for t in T if t[1] not in _REJ_CARDS]
SUBS[:]=[s for s in SUBS if s[1]!="israel-election-2026"]
POSTS[:]=[p for p in POSTS if p[0]!="election-sunday-serbia-brazil-2026"]
HELD.update({"world/israel-election-2026/","blog/election-sunday-serbia-brazil-2026/"})
