#!/usr/bin/env python

# runs in <50s with pypy

def dp(n):
    R = [[int(i<=2) for i in xrange(n)]]
    p10 = 1
    while R[-1][0]==1: # tant qu'il n'y a que la solution 0
        p10 = (p10*10)%n
        R.append([sum(R[-1][(r-i*p10)%n] for i in xrange(3)) for r in xrange(n)])
    # on a trouve un solution de taille len(R)
    # remontee pour calculer la plus petite solution
    r,f = 0,0
    for l in xrange(len(R)-1,0,-1):
        p10 = pow(10,l,n)
        # test de debut de range pour eviter la solution 0
        # l'ordre du range assure la plus petite solution
        # lexicographique
        for i in xrange(int(l==len(R)-1),3):
            if R[l-1][(r-i*p10)%n]>0:
                r = (r-i*p10)%n
                f = 10*f+i
                break
    f = 10*f+r
    return f

print 2+sum(dp(n)/n for n in xrange(3,10001))
