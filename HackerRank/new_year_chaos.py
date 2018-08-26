#!/usr/bin/env python3

# Notons D (= 2 ici) le nombre de depassements max par personne.
# Les personnes necessairement doublees par la personne Q[i] sont
# exactement les valeurs Q[j] < Q[i] pour j > i, i.e. les *inversions*.

# Pour D infini, cela se calcule habituellement par tri fusion modifie
# en O(n log n).

# Pour D grand ou fonction de n, le nombre de telles personnes peut etre
# compte par Fenwick Tree en O(n log n) (independamment de D) :
#   Pour i = n-1 .. 0
#     Ci = FT.somme_interval(1,Q[i]-1)
#     Si Ci>D alors renvoyer "Too chaotic"
#     C += Ci
#     FT.incremente(Q[i])

# Mais ici D = 2 constant et petit, ce qui privilegie l'approche en O(D*n)
# ci-dessous.

D = 2

def swaps(Q):
    n = len(Q)
    C = 0
    for i in range(n-2,-1,-1):
        # Q[i+1:] est suppose trie ici
        # par echanges locaux (comme dans un tri a bulle) on amene Q[i]
        # a sa place dans Q[i:]
        # s'il y a besoin de plus de D echanges pour cela -> invalide
        # sinon on a trie Q[i:]
        c = 0
        while i+c+1<n and Q[i+c]>Q[i+c+1]:
            Q[i+c],Q[i+c+1] = Q[i+c+1],Q[i+c]
            c += 1
            if c>D:
                return 'Too chaotic'
        C += c
    return C

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        Q = list(map(int,input().split()))
        print(swaps(Q))

main()
