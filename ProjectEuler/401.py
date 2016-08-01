#!/usr/bin/env python

# chaque nombre 1 <= d <= N contribue int(N/d) fois
# donc S2(N) = sum( int(N/d)*d^2, d=1..N )
# on regroupe par intervalles de nombres pour lesquels
# int(N/d) = k (const), i.e. a = N/(k+1) < d <= b = N/k
# la contribution d'un tel intervalle est k * sum( d^2, d=a..b )
# qui se calcule en O(1)

M = 10**9

def carres(n):
    return n*(n+1)*(2*n+1)/6

def carres2(a,b):
    return carres(b)-carres(a-1)

def S2(N):
    k = N
    s = 0
    while k>0:
        a,b = N/(k+1)+1,N/k
        s = (s + k*carres2(a,b))%M
        k = N/(b+1)
    return s

print S2(10**15)
