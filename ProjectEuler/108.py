#!/usr/bin/env python

# On remarque que x,y > 0 donc x,y > n
# On peut reecrire X = x-n > 0 et Y = y-n > 0
# 1/(X+n) + 1/(Y+n) = 1/n
# <=> n(2n+X+Y) = (X+n)(Y+n)
# <=> n^2 = XY
# On a dont autant de solutions (X,Y) que de diviseurs de n^2
# carre <=> nb impair de diviseurs
# Comme on veut eliminer la symetrie X/Y, il faut faire attention
# a la solution (n,n)
# nb sol = ((nb div de n^2)-1)/2 + 1

def sieve(N):
    P = [True for _ in xrange(N)]
    Factors = [[] for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,N):
        if P[i]:
            Factors[i].append((i,1))
            for k in xrange(2*i,N,i):
                P[k] = False
                l = k/i
                j = 1
                while l%i==0:
                    l /= i
                    j += 1
                Factors[k].append((i,j))
    return P,Factors

NMAX = 1000000
_,Factor = sieve(NMAX)

def nb_div_n2(n):
    nb = 1
    for (_,m) in Factor[n]:
        nb *= (2*m+1)
    return nb

def nb_sol(n):
    return 1+(nb_div_n2(n)-1)/2

def main():
    n = 1
    while nb_sol(n)<=1000:
        n += 1
    print n

main()
