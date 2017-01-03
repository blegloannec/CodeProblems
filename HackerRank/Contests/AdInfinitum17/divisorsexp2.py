#!/usr/bin/env python

import sys

# on ajoute iterativement les facteurs premiers pi^(a+i) a n
# si l'on connait S(n) = sum( s1(x), x|n ) avec s1(x) la somme des
# diviseurs de x, alors pour n' = n * pi^(a+i), on a
# S(n') = sum( s1(x) + s1(x*pi) + s1(x*pi^2) + ... + s1(x*pi^(a+i)), x|n )
# et s1(x*p^b) = s1(x) + s1(x)*p + s1(x)*p^2 + ... + s1(x)*p^b
#              = s1(x) * sum(p^j, 0<=j<=b)
# on sortant les sommes
# S(n') = S(n) * sum(sum(pi^j, 0<=j<=k), 0<=k<=a+i)
#       = S(n) * (a+i+1 - (p-p^(a+i+2))/(1-p))/(1-p)

def sieve_list(N):
    P = [True for _ in xrange(N)]
    L = []
    P[0] = False
    P[1] = False
    for i in xrange(2,N):
        if P[i]:
            L.append(i)
            for k in xrange(2*i,N,i):
                P[k] = False
    return L

Pr = sieve_list(2*10**6)

P = 10**9+7

def bezout(a,b):
    if b==0:
        return (a,1,0)
    g,u,v = bezout(b,a%b)
    return (g,v,u-(a/b)*v)

def inv_mod(a,n=P):
    _,u,_ = bezout(a,n)
    return u

IPr = [inv_mod(1-Pr[i]) for i in xrange(10**5+1)]

def main():
    q = int(sys.stdin.readline())
    for _ in xrange(q):
        m,a = map(int,sys.stdin.readline().split())
        res = 1
        for i in xrange(1,m+1):
            p = Pr[i-1]
            ip = IPr[i-1]
            res = (res * ip*(a+i+1-(p-pow(p,a+i+2,P))*ip))%P
        print res

main()
