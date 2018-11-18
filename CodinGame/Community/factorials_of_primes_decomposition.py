#!/usr/bin/env python3

from collections import defaultdict

NMAX = 20001

def sieve_decomp(N):
    P = [True]*N
    Decomp = [[] for _ in range(N)]
    for i in range(2,N):
        if P[i]:
            Decomp[i].append((i,1))
            for k in range(2*i,N,i):
                P[k] = False
                m = 1
                l = k//i
                while l%i==0:
                    l //= i
                    m += 1
                Decomp[k].append((i,m))
    return Decomp

Decomp = sieve_decomp(NMAX)

def sub_decomp(A,B,multB=1):
    for q in B:
        A[q] -= multB*B[q]
        if A[q]==0:
            del A[q]

FDecomp = [None]*NMAX
def fact_decomp(n):
    if FDecomp[n] is None:
        FDecomp[n] = defaultdict(int)
        for p,m in Decomp[n]:
            # adding (p!)^m
            FDecomp[n][p] += m
            if p>2:
                # removing ((p-1)!)^m
                # NB: ideally, e.g. if there were lots of queries per testcase,
                #     the prefix-sums of FDecomp could also be precomputed
                #     to avoid that loop
                for q in range(2,p):
                    sub_decomp(FDecomp[n],fact_decomp(q),m)
    return FDecomp[n]

def main():
    N = list(map(int,input().split('/')))
    FD = fact_decomp(N[0])
    if len(N)==2:
        sub_decomp(FD,fact_decomp(N[1]))
    print(' '.join('%d#%d' % (p,FD[p]) for p in sorted(FD,reverse=True)))

main()
