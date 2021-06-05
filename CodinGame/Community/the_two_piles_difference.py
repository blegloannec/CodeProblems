#!/usr/bin/env python3

# Prog. dyn. stockant explicitement les (somme,produit) des sous-ensembles.
# Si l'on voulait n'utiliser (quasiment) pas d'espace, on pourrait faire une
# prog. dyn pour compter et la remonter pour enumerer les sous-ensembles (il
# n'y en aurait ici au plus quelques millions vu les entrees).
# Mais ici (vu la taille des entrees) on a largement assez d'espace, on
# utilise juste une petite observation (mais loin d'etre indispensable) :
# les elements sont <=20 et un sous-ensemble considere est de taille <=20
# donc la somme est <=400, ce qui limite considerablement le nb de sommes
# possibles, par contre les produits peuvent aller jusqu'a 20^20, sauf
# que pour S0 = (somme des N//2 plus grands elements)^2 et M0 une borne qcq sur
# l'optimal, par exemple M0 = abs(S0-(produit des N//2 plus petits elements)),
# il est unutile de stocker les produits >S0+M0 car il conduiront necessairement
# a des ecarts >M0. Cela permet de faire chuter considerablement le nombre
# de sous-ensembles consideres/stockes.

from collections import defaultdict

memo = {}
# dp(n,i) = ensemble des (somme,produit) des sous-ensembles de taille n
#           en considerant les i premiers elements de L
def dp(n,i):
    if n==0:
        return set([(0,1)])
    if i<0:
        return set()
    if (n,i) in memo:
        return memo[n,i]
    res = set()
    x,m = L[i]
    for k in range(min(n,m)+1):
        for (s,p) in dp(n-k,i-1):
            s0,p0 = s+k*x,p*x**k
            if p0<=Pmax:
                res.add((s0,p0))
    memo[n,i] = res
    return res

def main():
    global L,Pmax
    N = int(input())
    L = list(map(int,input().split()))
    S = sum(L)
    L.sort()
    S0 = sum(L[N//2:])**2
    P0 = 1
    for i in range(N//2):
        P0 *= L[i]
    M0 = abs(S0-P0)
    Pmax = S0+M0
    D = defaultdict(int)
    for x in L:
        D[x] += 1
    L = [(x,D[x]) for x in D]
    M = M0
    for (s,p) in dp(N//2,len(L)-1):
        M = min(M,abs((S-s)**2-p))
    print(M)

main()
