#!/usr/bin/env python

import sys

# pour le denominateur D, le nombre de nouvelles fractions <1/A
# est le nb de nb premiers avec D inferieurs a B = D/A
# pour compter ce nombre, on peut proceder par inclusion-exclusion
# http://stackoverflow.com/questions/12709813/modifying-euler-totient-function
# pour chaque facteur p de la decomposition de n, on a
# A/p multiples a retirer, puis rajouter les A/(p1*p2) multiples de 2 facteurs,
# puis retirer les A/(p1*p2*p3) multiples de 3 facteurs, etc.

def sieve_factors(N):
    P = [True for _ in xrange(N)]
    Factors = [[] for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,N):
        if P[i]:
            Factors[i].append(i)
            for k in xrange(2*i,N,i):
                P[k] = False
                Factors[k].append(i)
    return P,Factors

# Premiere version de l'indicatrice d'Euler par
# inclusion-exclusion (un peu trop lente)
# donne le nb de nb premiers avec n entre A et B
def parmi(n,p,F):
    if p==0:
        yield 1
    else:
        for i in xrange(p-1,n):
            for S in parmi(i,p-1,F):
                yield S*F[i]

def euler_bound(n,F,A,B):
    cpt = B-A
    for p in xrange(1,len(F)+1):
        sgn = 1-2*(p%2)
        for m in parmi(len(F),p,F):
            cpt += sgn*(B/m - A/m)
    return cpt

# Version optimisee en parcourant les sous-ensembles
# selon un code de Gray
# le bit qui change a l'etape n est donne par la
# valuation 2-adique de n
def val2(n):
    if n==0:
        return -1
    i = 0
    while n&1==0:
        n >>= 1
        i += 1
    return i

# pre-calcul pour le code de Gray
V = [val2(i) for i in xrange(1<<7)]
vu = [False for i in xrange(7)]
M = [False]
for i in xrange(1,1<<7):
    M.append(vu[V[i]])
    vu[V[i]] = not vu[V[i]]

def euler_bound2(n,F,A,B):
    cpt = B-A
    m = 1
    for p in xrange(1,1<<len(F)):
        f = F[V[p]]
        if M[p]:
            m /= f
        else:
            m *= f
        sgn = 1-2*(p%2)
        cpt += sgn*(B/m - A/m)
    return cpt


def main():
    A,D = map(int,sys.stdin.readline().split())
    _,F = sieve_factors(D+1)
    cpt = 0
    for n in xrange(2,D+1):
        cpt += euler_bound2(n,F[n],(n+A)/(A+1)-1,n/A)
    print cpt-2

main()
