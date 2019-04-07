#!/usr/bin/env python3

from fractions import gcd

def decrypt(C):
    L = len(C)
    M = [None]*(L+1)
    i0 = next(i for i in range(L-1) if C[i]!=C[i+1])
    M[i0+1] = gcd(C[i0],C[i0+1])
    for i in range(i0+2,L+1):
        M[i] = C[i-1]//M[i-1]
    for i in range(i0,-1,-1):
        M[i] = C[i]//M[i+1]
    P = sorted(set(M))
    D = {P[i]:chr(i+ord('A')) for i in range(26)}
    return ''.join(D[m] for m in M)

if __name__=='__main__':
    T = int(input())
    for t in range(1,T+1):
        N,L = map(int,input().split())
        C = list(map(int,input().split()))
        print('Case #%d: %s' % (t,decrypt(C)))
