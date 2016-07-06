#!/usr/bin/env python

import sys

# P(n,k) = luck max pour les n premiers contests
# avec exatement k defaites sur les contests importants
def progdyn(n,k):
    if n<0:
        if k==0:
            return 0
        else:
            return -float('inf')
    if k<0:
        return -float('inf')
    if P[n][k]!=None:
        return P[n][k]
    if T[n]==1:
        res = max(progdyn(n-1,k)-L[n],progdyn(n-1,k-1)+L[n])
    else:
        res = max(progdyn(n-1,k)-L[n],progdyn(n-1,k)+L[n])
    P[n][k] = res
    return res

def main():
    global L,T,P
    N,K = map(int,sys.stdin.readline().split())
    L,T = [0 for _ in xrange(N)],[0 for _ in xrange(N)]
    for i in xrange(N):
        L[i],T[i] = map(int,sys.stdin.readline().split())
    P = [[None for _ in xrange(K+1)] for _ in xrange(N)]
    print max(progdyn(N-1,k) for k in xrange(K+1))
    
main()
