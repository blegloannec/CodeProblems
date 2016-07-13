#!/usr/bin/env python

# le nb de facteurs p dans n!
# est sum(n/p^i pour tout i)
# donc si on connait la decomposition de n en base p
# c'est la somme des valeurs successives de
# la construction de n a partir de ses chiffres
# par Horner

def ST(p,q):
    S = 290797
    T = [S%p]
    for i in xrange(1,q+1):
        S = (S*S)%50515093
        T.append(S%p)
    return T

def cpt(T,p,m):
    res = 0
    h = 0
    for i in xrange(len(T)-1,0,-1):
        h = (h*p+T[i])%m
        res = (res+h)%m
    return res

def main():
    #p,q = 3,10**4
    #m = 3**20
    p,q = 61,10**7
    m = 61**10
    T = ST(p,q)
    print cpt(T,p,m)

main()
