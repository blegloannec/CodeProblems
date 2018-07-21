#!/usr/bin/env python

from fractions import gcd

# solution naive
def naive():
    cpt = 0
    for d in xrange(5,12001):
        for n in xrange(d/3+1,d/2+1):
            if gcd(n,d)==1:
                cpt += 1
    return cpt

# meilleure solution (en O(solution))
# parcours de l'arbre des fractions (Stern-Brocot)
# en exploitant la propriete du median des
# suites de Farey
def arbrebfs():
    cpt = 0
    Q = [(1,2,1,3)]
    while Q:
        p1,q1,p2,q2 = Q.pop()
        if q1+q2>12000:
            continue
        cpt += 1
        Q.append((p1,q1,p1+p2,q1+q2))
        Q.append((p1+p2,q1+q2,p2,q2))
    return cpt

#print naive()
print arbrebfs()
