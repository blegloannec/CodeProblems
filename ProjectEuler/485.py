#!/usr/bin/env python

def sieve_nb_divisors(N):
    P = [True for _ in xrange(N)]
    Nbdiv = [1 for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,N):
        if P[i]:
            Nbdiv[i] = 2
            for k in xrange(2*i,N,i):
                P[k] = False
                l = k/i
                j = 1
                while l%i==0:
                    l /= i
                    j += 1
                Nbdiv[k] *= j+1
    return P,Nbdiv

def S(Nbdiv,u,k):
    M = 0
    Cpt = [0 for _ in xrange(max(Nbdiv)+1)]
    for n in xrange(1,k+1):
        Cpt[Nbdiv[n]] += 1
        if Nbdiv[n]>M:
            M = Nbdiv[n]
    s = M
    for n in xrange(2,u-k+2):
        Cpt[Nbdiv[n-1]] -= 1
        Cpt[Nbdiv[n+k-1]] += 1
        if Nbdiv[n+k-1]>M:
            M = Nbdiv[n+k-1]
        while Cpt[M]==0:
            M -= 1
        s += M
    return s

def main():
    N = 10**8
    _,Nbdiv = sieve_nb_divisors(N+1)
    print S(Nbdiv,N,10**5)

main()
