#!/usr/bin/env python3

# A chaque instant, on considere le graphe oriente et sans les sorties
# On note x(u) = le nb de sorties reliees au sommet u
# x(u) vaut 0, 1 ou 2 (mais la methode fonctionne pour des x(u)>=2)
# si x(u)<2, on pondere les arcs u -> v par la valeur 1-x(u)
# si x(u)>=2, on oublie les arcs sortants
# avec cette ponderation, la "distance" min de u a v est le nombre de minimal
# de "choix libres" pour le joueur lorsque le virus se deplace de maniere
# "optimale" de u a v
# (un choix libre est un choix non force, i.e. le virus n'est pas voisin d'une
# sortie, ce qui force l'arete a supprimer)
# 1. si x(v)>0 et que le virus est a distance d<x(v)-1 de v, alors il peut
# rejoindre v encore connecte a >=x(v)-d>=2 sorties et donc sortir
# cela ne doit donc jamais se produire
# 2. si x(v)>0 et que le virus est a distance d = x(v)-1, alors le joueur doit
# absolument deconnecter une sortie de v, sinon le virus peut forcer le cas 1
# au tour suivant

# avec ces observations, on sait faire le bon choix glouton a faire a chaque
# tour (cf code)

from heapq import *

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n,l,e = map(int,input().split())
G = [[] for _ in range(n)]
for _ in range(l):
    u,v = map(int,input().split())
    G[u].append(v)
    G[v].append(u)
E = [False]*n
for _ in range(e):
    E[int(input())] = True
V = [[] for _ in range(n)]
for u in range(n):
    if not E[u]:
        for v in G[u]:
            if E[v]:
                V[u].append(v)

def dijkstra(u0):
    D = [None]*n
    D[u0] = 0
    H = [(0,u0)]
    u0 = None
    while H:
        d,u = heappop(H)
        assert(d>=len(V[u])-1)
        if V[u] and d==len(V[u])-1:
            return u
        if u0==None and V[u]:
            u0 = u
        for v in G[u]:
            if not E[v] and D[v]==None:
                D[v] = d + 1-len(V[u])
                heappush(H,(D[v],v))
    return u0

# game loop
while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    u = dijkstra(si)
    v = V[u].pop()
    print(u,v)
