#!/usr/bin/env python

from math import sqrt

# s(n) est multiplicative, si n = prod( pi^ai )
# alors s(n) = prod( s(pi^ai) )
# ou s(pi^ai) = 1 + pi + pi^2 + ... + pi^ai
# 2017 est premier donc si 2017 | s(n) alors
# 2017 divise l'un des s(pi^ai)
# on commence donc par chercher parmi les puissances de nb premiers

# runs in ~4s with pypy

M = 2017
N = 10**11

def sieve(N):
    P = [True for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,int(sqrt(N))+1):
        if P[i]:
            for k in xrange(2*i,N,i):
                P[k] = False
    return P

P = sieve(int(sqrt(N))+1)

def bezout(a,b):
    if b==0:
        return (a,1,0)
    g,u,v = bezout(b,a%b)
    return (g,v,u-(a/b)*v)

def rev_chinois(a,p,b,q):
    g,u,v = bezout(p,q)
    assert(g==1)
    return (b*u*p+a*v*q)%(p*q)

# pour les premiers de la forme k*M-1
def sieve2():
    P2 = [True for _ in xrange(N/M+1)]
    P2[0] = False
    for i in xrange(2,len(P)):
        if P[i]:
            if i==2017:
                continue
            # on marque les nb verifiant
            # x = 0 mod P[i]
            # x = -1 mod M
            x0 = rev_chinois(0,i,M-1,M)
            if x0==i:
                x0 += i*M
            for x in xrange(x0,N+1,i*M):
                P2[(x+1)/M] = False
    return P2

# pour inclusion-exclusion
L = []
def parmi(n,p,a=1):
    if p==0:
        yield a
    else:
        for i in xrange(p-1,n):
            if a*L[i]*L[0]**(p-1)>N:
                break
            for x in parmi(i,p-1,a*L[i]):
                yield x

def main():
    res = 0
    # on genere les p^a, p premier et a>=2,
    # tels que 2017 | s(p^a) = 1+p+p^2+...+p^a
    for p in xrange(len(P)):
        if P[p]:
            s,q = 1+p,p*p
            while q<=N:
                s = (s+q)%M
                if s==0:
                    L.append(q)
                    # on somme les multiples de q = p^a
                    # mais pas de p^(a+1)
                    l,l2 = N/q, N/(q*p)
                    res += q*l*(l+1)/2 - q*p*l2*(l2+1)/2
                q *= p
    # on genere les p premiers tels que
    # 2017 | s(p) = 1+p
    # p = k*2017 - 1
    PM = sieve2()
    for k in xrange(len(PM)-1):
        if PM[k]:
            p = k*M-1
            L.append(p)
            # on somme les multiples de p
            # mais pas de p^2
            l,l2 = N/p, N/(p*p)
            res += p*l*(l+1)/2 - p*p*l2*(l2+1)/2
    # inclusion-exclusion pour retirer les doublons
    L.sort()
    for k in xrange(2,3): # suffisant car L[0]**3 > N
        res0 = 0
        for x in parmi(len(L),k):
            l = N/x
            res0 += x*l*(l+1)/2 
        res += res0 if k%2==1 else -res0
    print res

main()
