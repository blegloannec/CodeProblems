#!/usr/bin/env python3

def binom2(n):
    return n*(n-1)//2

k,m,n = map(int,input().split())
total = binom2(k+m+n)
dom = binom2(k)+k*(m+n) + 3*binom2(m)/4 + m*n/2
print(dom/total)
