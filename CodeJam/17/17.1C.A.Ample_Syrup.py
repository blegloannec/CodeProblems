#!/usr/bin/env python3

from math import *

# O(n^2 log n) good enough
def pick(P,K):
    Smax = 0
    for i in range(K-1,len(P)):
        # on prend P[i] comme base
        # et les K-1 les plus "epais" (en surface)
        # parmi les diametres inferieurs
        H = [h for (_,h) in P[:i]]
        H.sort(reverse=True)
        S = P[i][0]+P[i][1]+sum(H[:K-1])
        Smax = max(Smax,S)
    return Smax

def main():
    T = int(input())
    for t in range(1,T+1):
        N,K = map(int,input().split())
        P = []
        for _ in range(N):
            Ri,Hi = map(int,input().split())
            P.append((pi*Ri*Ri,2*pi*Ri*Hi))
        P.sort() # tri par (aire, surface epaisseur)
        print('Case #%d: %.9f' % (t,pick(P,K)))

main()
