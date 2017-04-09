#!/usr/bin/env python3

from collections import defaultdict

# NB : le code suivant est legerement simplifie (et commente)
#      par rapport au code soumis

# a chaque instant, la configuration peut etre vue comme
# un ensemble d'intervalles de places libres
# chaque nouvelle personne se place au centre d'un plus
# grand intervalle libre, le remplacant alors par deux
# intervalles 2 fois plus petits

def stalls(N,K):
    IntCount = defaultdict(int) # nb d'intervalles par taille
    IntCount[N] = 1
    while K>0:
        # s la plus grande taille d'intervalle dispo
        # on ne peut en realite jamais avoir plus de 3 elements simultanement
        # dans IntCount, donc on prend le max en O(1)
        # (le code initialement soumis utilisait un tas, mais c'est inutile...)
        s = max(IntCount)
        k = min(K,IntCount[s])
        # on place k personnes a la fois
        # k croit exponentiellement, donc O(log N) etapes
        K -= k
        # on supprime les intervalles de taille s
        # NB : a la toute derniere etape il en reste IntCount[s]-k,
        #      potientiellement >0, mais on n'a pas besoin de cette info ici
        del IntCount[s]
        l = (s-1)//2
        if l>0:
            IntCount[l] += k
        r = s-1-l
        if r>0:
            IntCount[r] += k
    return (l,r)

def main():
    T = int(input())
    for t in range(1,T+1):
        N,K = map(int,input().split())
        z,y = stalls(N,K)
        print('Case #%d: %d %d' % (t,y,z))

main()
