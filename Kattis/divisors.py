#!/usr/bin/env python3

import sys

N = 432

def sieve_list(N):
    P = [True]*N
    L = []
    for i in range(2,N):
        if P[i]:
            L.append(i)
            for k in range(2*i,N,i):
                P[k] = False
    return L

P = sieve_list(N)

def fact_val(n,p):  # p-valuation de n!
    cpt = 0
    q = p
    while q<=n:
        cpt += n//q
        q *= p
    return cpt

# decompositions primales des n!
D = [[fact_val(n,p) for p in P] for n in range(N)]  

def binom_nb_div(n,k):
    res = 1
    for i in range(len(P)):
        res *= D[n][i] - D[k][i] - D[n-k][i] + 1
    return res

def main():
    for L in sys.stdin.readlines():
        n,k = map(int,L.split())
        print(binom_nb_div(n,k))

main()
