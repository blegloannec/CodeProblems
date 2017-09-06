#!/usr/bin/env python3

P = 10**9+7
MMAX = 1001

def main():
    # pre-calcul du nb de moyens de remplir une ligne
    L = [0]*MMAX
    L[0] = 1
    for i in range(1,MMAX):
        for j in range(1,min(4,i)+1):
            L[i] = (L[i] + L[i-j]) % P
    # traitement des requetes
    T = int(input())
    for _ in range(T):
        N,M = map(int,input().split())
        NonSolid = [pow(L[m],N,P) for m in range(M+1)]
        Solid = [0]*(M+1)
        for m in range(M+1):
            Solid[m] = NonSolid[m]
            for j in range(1,m):
                Solid[m] = (Solid[m] - Solid[j]*NonSolid[m-j]) % P
        print(Solid[M])

main()
