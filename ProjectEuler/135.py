#!/usr/bin/env python

# x^2-y^2-z^2 = n
# on peut supposer x>y>z et donc x = 2y-z
# d'ou (2y-z)^2 - y^2 -z^2 = y(3y-4z) = n
# donc y | n et 4z = 3y-n/y
# donc 4 | 3y-n/y > 0

# runs in 7s with pypy

def sieve_decomp(N):
    P = [True for _ in xrange(N)]
    Decomp = [[] for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,N):
        if P[i]:
            Decomp[i].append((i,1))
            for k in xrange(2*i,N,i):
                P[k] = False
                m = 1
                l = k/i
                while l%i==0:
                    l /= i
                    m += 1
                Decomp[k].append((i,m))
    return P,Decomp

# generateur des diviseurs
def divisors(F,i=0):
    if i==len(F):
        yield 1
    else:
        p,m = F[i]
        f = 1
        for _ in xrange(m+1):
            for d in divisors(F,i+1):
                yield f*d
            f *= p

def main():
    N,K = 10**6,10
    _,Decomp = sieve_decomp(N)
    cpt = 0
    for n in xrange(1155,N):
        cpt0 = 0
        for y in divisors(Decomp[n]):
            Z = 3*y-n/y
            if Z>0 and Z%4==0:
                cpt0 += 1
        if cpt0==K:
            cpt += 1
    print cpt

main()
