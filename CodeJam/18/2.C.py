#!/usr/bin/env python3

from collections import defaultdict

def aug(u,G,M,seen):
    for v in G[u]:
        if not seen[v]:
            seen[v] = True
            if M[v]==None or aug(M[v],G,M,seen):
                M[v] = u
                return True
    return False

def bip_match(G,Us,Vs):
    M = [None]*Vs
    for u in range(Us):
        aug(u,G,M,[False]*Vs)
    return M

def solve(P):
    Di = {}
    Dj = {}
    Q = []
    for i,j in P:
        if i not in Di:
            Di[i] = len(Di)
        if j not in Dj:
            Dj[j] = len(Dj)
        Q.append((Di[i],Dj[j]))
    G = [[] for _ in range(len(Di))]
    for i,j in Q:
        G[i].append(j)
    M = bip_match(G,len(Di),len(Dj))
    return len(Q)-sum(int(m!=None) for m in M)
    

def main():
    T = int(input())
    for t in range(1,T+1):
        N = int(input())
        G = [list(map(int,input().split())) for _ in range(N)]
        D = defaultdict(list)
        for i in range(N):
            for j in range(N):
                D[G[i][j]].append((i,j))
        res = sum(solve(D[c]) for c in D)
        print('Case #%d: %d' % (t,res))

main()
