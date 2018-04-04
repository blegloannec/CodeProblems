#!/usr/bin/env python3

import sys

def sieve_list(N):
    P = [True]*N
    L = []
    for i in range(2,N):
        if P[i]:
            L.append(i)
            for k in range(2*i,N,i):
                P[k] = False
    return L

P = sieve_list(32000)

def decomp(n):
    F = []
    i = 0
    while n>1 and P[i]*P[i]<=n:
        m = 0
        while n%P[i]==0:
            n //= P[i]
            m += 1
        if m>0:
            F.append((P[i],m))
        i += 1
    if n>1:
        F.append((n,1))
    return F

def div_sum(n):
    D = decomp(n)
    S = 1
    for p,m in D:
        S *= (1-p**(m+1))//(1-p)
    return S

def main():
    for L in sys.stdin.readlines():
        n = int(L)
        d = abs(div_sum(n)-2*n)
        s = '' if d==0 else 'almost ' if d<=2 else 'not '
        print('%d %sperfect' % (n,s))

main()
