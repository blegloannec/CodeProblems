#!/usr/bin/env python3

order = input()
side = input()

opp_side = {'R':'L','L':'R','U':'D','D':'U'}

vis,opp = 1,1
for c in order:
    if c==side:
        opp += vis
        vis = 1
    elif c==opp_side[side]:
        vis += opp
        opp = 1
    else:
        vis *= 2
        opp *= 2
print(vis)
