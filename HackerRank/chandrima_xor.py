#!/usr/bin/env python3

# le nb de mots sur {0,1} de taille n ne comportant pas le motif 11
# est Fibo(n+1) (trivial)
# on calcule le k-ieme nombre recherche en remplissant ses lettres
# de la gauche vers la droite et en decrementant k du nb de mots elimines
# (si k >= Fibo(i) = nb de mots de taille i commencant par 0, alors on met
#  un 1 en position i, on soustrait Fibo(i) a k, puis on continue en i-1)
# NB : ce sont les "Fibbinary numbers" http://oeis.org/A003714

P = 10**9+7
Amax = 10**18

F = [1,2]
while F[-1]<Amax:
    F.append(F[-1]+F[-2])

def get_kth(k):
    n = len(F)-1
    res = 0
    while n>0:
        res <<= 1
        if k>=F[n-1]:
            k -= F[n-1]
            res |= 1
        n -= 1
    return res

def main():
    N = int(input())
    A = list(map(int,input().split()))
    X = 0
    for a in A:
        X ^= get_kth(a)
    print(X%P)

main()
