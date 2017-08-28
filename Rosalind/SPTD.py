#!/usr/bin/env python3

import rosalib

S = list(input().split())
S = {S[i]:i for i in range(len(S))}
Sall = frozenset(range(len(S)))
T1 = {}
R1 = rosalib.parse_newick(input(),T1,False)  # we do not unroot it
T2 = {}
R2 = rosalib.parse_newick(input(),T2,False)  # we do not unroot it

# similar to character table building from CTBL
def dfs(T,u,Splits):
    if u[0]!='@':
        return frozenset([S[u]])
    Su = frozenset()
    for v in T[u]:
        Su |= dfs(T,v,Splits)
    if 1<len(Su)<len(S)-1: # nontrivial char
        if 0 in Su:
            Splits.add(Su)
        else:
            Splits.add(Sall-Su) # on ajoute le complementaire
    return Su

S1 = set()
dfs(T1,R1,S1)
S2 = set()
dfs(T2,R2,S2)
d = 2*(len(S)-3)-2*len(S1&S2)
print(d)
