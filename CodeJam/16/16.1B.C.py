#!/usr/bin/env python3

import sys

# On represente le pb par un graphe biparti dans lequel
# chaque topic "A B" donne un arc A-B.
# On cherche a maximiser le nb de faux topics, donc minimiser le nb
# de vrais topics, ie. trouver un ensemble minimal d'arcs couvrant tous
# les sommets. Un tel ensemble est obtenu en completant un couplage
# maximal (car ce dernier maximise le nb de sommets couverts par les arcs).
# On complete le couplage en ajoutant un arc par sommet non couvert.
# Ainsi si l'on a nbU et nbV sommets dans les 2 composantes U et V du graphe
# et que S est la taille d'un couplage maximal biparti,
# alors il faut ajouter nbU-S arcs pour couvrir U
# et nbV-S arcs pour couvrir V et l'on a ainsi construit une couverture
# par arcs minimale de taille nbU+nbV-S.
# Les arcs restants constituent un ensemble maximal de fake topics.

def augment(u,G,visit,match):
    for v in G[u]:
        if not visit[v]:
            visit[v] = True
            if match[v]==None or augment(match[v],G,visit,match):
                match[v] = u
                return True
    return False

def max_bipartite_matching(G,nbU,nbV):
    match = [None]*nbV
    for u in range(nbU):
        augment(u,G,[False]*nbV,match)
    return match

def main():
    T = int(sys.stdin.readline())
    for t in range(1,T+1):
        N = int(sys.stdin.readline())
        nbU,nbV = 0,0
        U,V = {},{}
        G = []
        for _ in range(N):
            u,v = sys.stdin.readline().split()
            if u not in U:
                U[u] = nbU
                nbU += 1
                G.append([])
            if v not in V:
                V[v] = nbV
                nbV += 1
            G[U[u]].append(V[v])
        MV = max_bipartite_matching(G,nbU,nbV)
        size = nbV - MV.count(None)
        fake = N - (nbU+nbV-size)
        print('Case #%d: %d'%(t,fake))

main()
