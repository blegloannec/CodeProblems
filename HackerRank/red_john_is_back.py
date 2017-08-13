#!/usr/bin/env python3

from math import sqrt

NMAX = 40

def sieve(N):
    P = [True]*N
    P[0] = False
    P[1] = False
    for i in range(2,int(sqrt(N))+1):
        if P[i]:
            for k in range(2*i,N,i):
                P[k] = False
    return P
    
def main():
    # pre-comp
    U = [1,1,1,1]
    for i in range(4,NMAX+1):
        U.append(U[-1]+U[-4])
    PMAX = U[NMAX]
    P = sieve(PMAX+1)
    NP = [0]*(PMAX+1)
    for i in range(1,PMAX+1):
        NP[i] += NP[i-1] + int(P[i])
    # input
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(NP[U[N]])

main()
