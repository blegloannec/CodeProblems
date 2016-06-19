#!/usr/bin/env python

from math import sqrt

# cf problem 72 (Farey sequences)
# R(d) = phi(d) / (d-1)

# cf problem 69 (totient)
# phi(d)/d = Prod( 1 - 1/p, p|n premier )
# est minimise localement pour les 2*3*5*7*11*13*...

def eratosthene(n):
    l = range(2,n+1)
    s = int(sqrt(n))+1
    for i in xrange(2,s):
        for k in xrange(2*i,n+1,i):
            l[k-2] = -1
    return filter((lambda x: x>0),l)

def main():
    P = eratosthene(100)
    p,q = 15499,94744
    i = 0
    n = 2
    phi = 1
    while phi*q>=p*(n-1):
        i += 1
        n *= P[i]
        phi *= P[i]-1
    # le premier tel n valide est 2*...*29
    # la solution est parmi les multiples du precedent
    # ie de 2*...*23
    n /= P[i]
    phi /= P[i]-1
    i = 2
    while i*phi*q>=p*(i*n-1):
        i += 1
    print i*n

main()
