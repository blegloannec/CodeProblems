#!/usr/bin/env python

# En reflechissant a la meilleure strategie...
# m,n >= 2
# Le cas S(2,2) = 5 est un cas particulier
# Pour une grille 2xn, l'optimal est L(n) = (n-1) + 1 + 2*3 + 5*(n-3) = 6n-9
# Pour nxn, l'optimal est C(n) = (2*n-3) + 1 + 3*(2*n-3) = 8n-11
# (descente en diagonale)
# Pour mxn avec m>n>2, l'optimal est :
# S(m,n) = m-n + C(n) + 3 + 5*(m-n-1) = 6m+2n-13
# (descente en diagonale, puis deplacement le long de la derniere ligne)
# on retrouve L(m) = S(m,2)

def sieve(N):
    L = []
    P = [True for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,N):
        if P[i]:
            L.append(i)
            for k in xrange(2*i,N,i):
                P[k] = False
    return L

def main():
    P = sieve(10**6)
    cpt = 0
    for i in xrange(1,len(P)):
        p = P[i]
        # actually cannot happen:
        #if (p*p+11)%8==0:
        #    cpt += 1
        a = (p*p+13)/2
        # 3m + n = a
        # n = a-3m et n<m donc a < 4m
        # et n>1 donc a-1 > 3m
        mmax = (a-2)/3
        if mmax>2:
            cpt += 2*(mmax-(a+3)/4+1)
    print cpt

main()
