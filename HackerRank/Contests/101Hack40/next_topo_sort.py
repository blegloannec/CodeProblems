#!/usr/bin/env python

import sys
from heapq import *

# reused PE79+
def greedylex(G,prioq,nbpred):
    toposort = []
    while prioq:
        u = heappop(prioq)
        toposort.append(u)
        for v in G[u]:
            nbpred[v] -= 1
            if nbpred[v]==0:
                heappush(prioq,v)
    return toposort

def main():
    n,m = map(int,sys.stdin.readline().split())
    G = [[] for _ in xrange(n)]
    for _ in xrange(m):
        u,v = map(int,sys.stdin.readline().split())
        G[u-1].append(v-1)
    P = map((lambda x: int(x)-1),sys.stdin.readline().split())
    # on va reconstruire le graphe progressivement en prenant P a l'envers
    choix = []
    nbpred = [0 for _ in xrange(n)]
    for i in xrange(len(P)-1,-1,-1):
        # on ajoute le sommet P[i], sans predecesseur dans le graphe courant
        u = P[i]
        for v in G[u]:
            nbpred[v] += 1
        # on l'ajoute aux choix possibles pour le sommet a retirer a cet instant
        heappush(choix,-u)
        # on retire les sommets qui ne sont plus orphelins des choix possibles
        while choix[0]<-u and nbpred[-choix[0]]>0:
            heappop(choix)
        if choix[0]<-u:
            # on a trouve un sommet >u qui est un choix possible, c'est le
            # premier instant ou l'on peut "incrementer" le tri topologique P
            prioq = []
            while choix:
                v = -heappop(choix)
                if v==u:
                    # u0 replacant de u
                    u0 = prioq.pop()
                if nbpred[v]==0:
                    prioq.append(v)
            # on met a jour en choisissant u0 a la place de u
            for v in G[u0]:
                nbpred[v] -= 1
                if nbpred[v]==0:
                    prioq.append(v)
            heapify(prioq)
            # on relance un tri topologique lex min a partir de cet instant
            nouvtri = greedylex(G,prioq,nbpred)
            print ' '.join(map((lambda x: str(x+1)),P[:i]+[u0]+nouvtri))
            return
    # on n'a jamais trouve mieux, P etait maximal
    print -1

main()
