#!/usr/bin/env python

import sys

# Interpolation de Lagrange en les points (xi,yi)
# P(X) = sum( yi*prod( (X-xj)/(xi-xj), xj=/=xi ), i )
# posons wi = prod( 1/(xi-xj), j=/=i )
# et Q(X) = prod( X-xi, i )
# alors P(X) = Q(X)*sum( yi*wi/(X-xi), i )
# Evaluation en O(n) si l'on a pre-calcule les wi
# et ajout simple d'un point en mettant a jour les wi

M = 10**9+7

def bezout(a,b):
    if b==0:
        return (a,1,0)
    g,u,v = bezout(b,a%b)
    return (g,v,u-(a/b)*v)

memo = {}
def inv_mod(a,n=M):
    if a in memo:
        return memo[a]
    _,u,_ = bezout(a,n)
    memo[a] = u%n
    return memo[a]

def U(n):
    res = 0
    for i in xrange(N,-1,-1):
        res = (n*res + A[i])%M
    return res

def main():
    global N,A
    N = int(sys.stdin.readline())
    A = map(int,sys.stdin.readline().split())
    Y,W,P = [],[],[]
    for x in xrange(1,N+1):
        Y.append(U(x))
        # m-a-j des wi
        for i in xrange(len(W)):
            W[i] = (W[i]*inv_mod((i+1)-x))%M
        # nouveau coeff
        W.append(1)
        for i in xrange(1,x):
            W[-1] = (W[-1]*inv_mod(x-i))%M
        # calcul de Q(x+1)
        q = 1
        for i in xrange(1,x+1):
            q = (q*((x+1)-i))%M
        # calcul de P(x+1)
        p = 0
        for i in xrange(x):
            p = (p+Y[i]*W[i]*inv_mod((x+1)-(i+1)))%M
        p = (p*q)%M
        P.append(p)
    print ' '.join(map(str,P))

main()
