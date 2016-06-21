#!/usr/bin/env python

import sys
from collections import deque

# Note to myself: next time, READ THE F*** statement of the problem!

# Le pb est equivalent au maxflow dans le graphe COMPLET dont les
# capa des liens sont donnees par les DISTANCES dans un arbre (et non
# les MAX...), la source est 1 et le puits n

# mais pas besoin d'algo de flot ici, la mincut a lieu
# soit en coupant toutes les aretes du sommet 1, soit
# celles du sommet n
# cf edito pour preuve complete

def dfs(u0):
    D = [-1 for _ in xrange(n)]
    D[u0] = 0
    Q = deque()
    Q.append(u0)
    while Q:
        u = Q.popleft()
        for (v,c) in G[u]:
            if D[v]<0:
                D[v] = D[u]+c
                Q.append(v)
    return D

def main():
    global n,G
    n = int(sys.stdin.readline())
    G = [[] for _ in xrange(n)]
    for _ in xrange(n-1):
        a,b,c = map(int,sys.stdin.readline().split())
        G[a-1].append((b-1,c))
        G[b-1].append((a-1,c))
    D1 = dfs(0)
    Dn = dfs(n-1)
    print min(sum(D1),sum(Dn))

main()
