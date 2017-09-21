#!/usr/bin/env python3

import rosalib

T = {}
R = rosalib.parse_newick(input(),T,False)
F = rosalib.parse_fasta()
N = len(F[0][1])  # size of DNAs
DNA = {x:y for x,y in F}

def dfs(u,u0,i,si,ti):
    if DNA[u][i]==si:
        yield u
    elif DNA[u][i]==ti:
        for v in T[u]:
            yield from dfs(v,u,i,si,ti)

for s in T:
    for t in T[s]:
        for i in range(N):
            if DNA[s][i]!=DNA[t][i]:
                for w in dfs(t,s,i,DNA[s][i],DNA[t][i]):
                    print('%s %s %d %s->%s->%s' % (t,w,i+1,DNA[s][i],DNA[t][i],DNA[s][i]))
