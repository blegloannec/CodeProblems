#!/usr/bin/env python3

import rosalib

# NB: "Given: An unrooted *binary* tree"

T = {}
R = rosalib.parse_newick(input(),T,False)  # we do not unroot it
S = sorted(X for X in T if X[0]!='@')  # named species (necessarily leaves?)
CharTbl = []

def dfs(u):
    Su = set()
    if u[0]!='@':
        Su.add(u)
    for v in T[u]:
        Su |= dfs(v)
    if 1<len(Su)<len(S)-1: # nontrivial char
        CharTbl.append([X in Su for X in S])
    return Su

dfs(R)
for L in CharTbl:
    print(''.join('1' if x else '0' for x in L))
