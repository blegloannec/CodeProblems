#!/usr/bin/env python

# approche similaire au pb 407
# runs in ~4min with pypy

# a^2 = 1 [n]
# (a-1)(a+1) = 0 [n]
# gcd(a-1,a+1) = 2
# donc il existe m1 et m2 p-e-e ou avec 2 comme seul facteur premier
# en commun tq n = m1*m2 et a = 1 [m1] et a = -1 [m2]
# on essaye pour tous les m1 enumeres a partir de la decomposition
# de n et on garde le plus grand a<n-1 (calcule par thm chinois)

def sieve_decomp(N):
    P = [True for _ in xrange(N)]
    Decomp = [[] for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,N):
        if P[i]:
            Decomp[i].append(i)
            for k in xrange(2*i,N,i):
                P[k] = False
                m = i
                l = k/i
                while l%i==0:
                    l /= i
                    m *= i
                Decomp[k].append(m)
    return P,Decomp

# sous-ensembles de la decomp
def gen(d,i=0,n=1):
    if i==len(d):
        yield n
    else:
        for a in gen(d,i+1,n):
            yield a
        for a in gen(d,i+1,n*d[i]):
            yield a

def bezout(a,b):
    if b==0:
        return (a,1,0)
    g,u,v = bezout(b,a%b)
    return (g,v,u-(a/b)*v)

def inv_mod(a,n):
    g,u,_ = bezout(a,n)
    return u%n # %n pour valeur >0

def rev_chinois(a,p,b,q):
    g,u,v = bezout(p,q)
    assert(g==1)
    return (b*u*p+a*v*q)%(p*q)

def fact2(n):
    n2 = 1
    while n%2==0:
        n /= 2
        n2 *= 2
    return n,n2

# thm chinois pour p et q avec 2 comme seul
# facteur premier en commun
def rev_chinois2(a,p,b,q):
    p,p2 = fact2(p)
    q,q2 = fact2(q)
    if p2>=q2:
        if a%q2!=b%q2:
            return None,None
        c,r = a%p2,p2
    else:
        if a%p2!=b%p2:
            return None,None
        c,r = b%q2,q2
    return rev_chinois(a%p,p,rev_chinois(b%q,q,c,r),q*r),p*q*r
        
def l(n,d):
    res = 0
    for u in gen(d):
        m1,m2 = u,n/u
        x = rev_chinois(1,m1,-1,m2)
        if res<x<n-1:
            res = x
        # transfert des 2 de m1 vers m2
        while m1%2==0:
            m1,m2 = m1/2,m2*2
            # solution x unique modulo n0 <= n
            x,n0 = rev_chinois2(1,m1,-1,m2)
            if x!=None:
                # on maximise x
                x += n0*((n-x)/n0)
                if res<x<n-1:
                    res = x
    return res

def tl(n):
    for i in xrange(n-2,0,-1):
        if (i*i)%n==1:
            return i

def main():
    N = 2*10**7+1
    _,D = sieve_decomp(N)
    res = 0
    for i in xrange(3,N):
        res += l(i,D[i])
    print res

main()
