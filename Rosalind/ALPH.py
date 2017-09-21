#!/usr/bin/env python3

import rosalib

A = ['A','C','G','T','-']

tree = input()
T = {}
R = rosalib.parse_newick(tree,T,False)
F = rosalib.parse_fasta()
N = len(F[0][1])  # size of DNAs
DNA = {x:y for x,y in F}

# dp(i,u,a) = min sum of hamming distances of i-th letters on edges of
#             the subtree rooted at node u using a in A as i-th letter
#             of node u's DNA strand
# O(len(T) * N * len(A))
memo,pred = {},{}
def dp(i,u,a):
    assert(u not in DNA)  # u is not a leaf
    if (i,u,a) in memo:
        return memo[i,u,a]
    smin,pmin = 0,[]
    for v in T[u]:
        if v in DNA:  # v leaf
            b = DNA[v][i]
            sv,pv = int(a!=b),b
        else:
            sv,pv = float('inf'),None
            for b in A:
                s = dp(i,v,b) + int(a!=b)
                if s<sv:
                    sv,pv = s,b
        smin += sv
        pmin.append(pv)
    memo[i,u,a] = smin
    pred[i,u,a] = tuple(pmin)
    return smin

sol = {u:[None]*N for u in T if u not in DNA}
def solution(i,u,a):
    if u not in DNA:
        sol[u][i] = a
        for iv in range(len(T[u])):
            solution(i,T[u][iv],pred[i,u,a][iv])

def dp_all(u):
    sall = 0
    for i in range(N):
        smin,amin = float('inf'),None
        for a in A:
            if dp(i,u,a)<smin:
                smin,amin = dp(i,u,a),a
        sall += smin
        solution(i,u,amin)
    return sall

print(dp_all(R))
for x in sol:
    print('>'+x)
    print(''.join(sol[x]))
