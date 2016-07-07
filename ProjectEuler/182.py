#!/usr/bin/env python

from fractions import gcd

# par thm chinois, on a
# m^e = m [n] <=> m^e = m [p] et m^e = m [q]
# et par Fermat, on a m^(p-1) = 1 [p]
# donc un considerera e%(p-1) et e%(q-1) dans
# les egalites de droite

p,q = 1009,3643
n = p*q
phi = (p-1)*(q-1)

# on precalcule pour chaque e < p-1
# le nb de messages m < p tels que m^e = m [p]
def precomp(p):
    T = [0 for _ in xrange(p-1)]
    for m in xrange(p):
        n = 1
        for e in xrange(p-1):
            if n==m:
                T[e] += 1
            n = (n*m)%p
    return T

def main():
    Tp = precomp(p)
    Tq = precomp(q)
    minnb = float('inf')
    for e in xrange(1,phi):
        if gcd(e,phi)==1:
            nb = Tp[e%(p-1)]*Tq[e%(q-1)]
            if nb<minnb:
                minnb = nb
                s = e
            elif nb==minnb:
                s += e
    print s

main()
