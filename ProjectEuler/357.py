#!/usr/bin/env python

from math import sqrt

# comme on compte 1 et n dans les diviseurs
# il faut n+1 premier

def sieve(N):
    P = [True for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,int(sqrt(N))+1):
        if P[i]:
            for k in xrange(2*i,N,i):
                P[k] = False
    return P

def main():
    N = 10**8
    P = sieve(N+2)
    s = 0
    for n in xrange(1,N+1):
        if P[n+1]:
            gen = True
            for d in xrange(1,int(sqrt(n))+1):
                if n%d==0:
                    if not P[d+n/d]:
                        gen = False
                        break
            if gen:
                s += n
    print s

main()
