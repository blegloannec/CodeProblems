#!/usr/bin/env python

import sys

# la relation F est fonctionnelle donc graphe de deg sortant 1
# tout chemin aboutit a un cycle
# le graphe se partitionne en etoiles de chaines aboutissant a un cycle
# 1. si le cycle est de longueur 2 (couple) on cherche la plus longue chaine
#    xn -> ... -> x1 -> a <=> b <- y1 <- ... <- ym
#    cette chaine peut se concatener a n'importe quelle autre chaine du meme
#    type pour un autre couple pour former un cercle valide
#    la somme des chaines maximales pour chaque couple donne une solution
#    possible
# 2. si le cycle est de taille >=3 alors il constitue une solution possible
#    a lui seul et sans amelioration possible
# Solution generale : max(somme des chaines max, plus grand cycle)
# Algo en O(n), chaque sommet sera visite 1 seule fois

N = 0
F = []
invF = []
visited = []

def prof(a): # profondeur de l'arbre enracine en a (sommet d'un couple)
    visited[a] = True
    p = 0
    for b in invF[a]:
        if b!=F[a]: # utile seulement pour le couple de depart
            p = max(p,prof(b))
    return p+1

def cycle(a): # on cherche le cycle >=3 auquel aboutit a
    time = [None for _ in xrange(N)]
    visited[a] = True
    time[a] = 0
    a = F[a]
    t = 1
    while time[a]==None:
        if visited[a]:
            # sommet deja vu lors d'un appel precedent de cycle
            # on abandonne, le cycle a deja ete compte
            return 0
        visited[a] = True
        time[a] = t
        a = F[a]
        t += 1
    return t-time[a] # taille du cycle
    

def main():
    global N,F,invF,visited
    T = int(sys.stdin.readline())
    for t in range(1,T+1):
        N = int(sys.stdin.readline())
        F = map((lambda x: int(x)-1),sys.stdin.readline().split())
        # relation inverse
        invF = [[] for _ in xrange(N)]
        for a in xrange(N):
            invF[F[a]].append(a)
        # detection des couples
        couples = []
        for a in xrange(N):
            b = F[a]
            if b>a and F[b]==a:
                couples.append((a,b))
        visited = [False for _ in xrange(N)]
        # detection des chaines max autour des couples
        som_chaines = 0
        for (a,b) in couples:
            som_chaines += prof(a)+prof(b)
        # detection des cycles
        max_cycle = 0
        for a in xrange(N):
            if not visited[a]:
                max_cycle = max(max_cycle,cycle(a))
        print 'Case #%d: %d' % (t,max(som_chaines,max_cycle))

main()
