#!/usr/bin/env python

# really easy one!

def H(n):
    res = 0
    n -= 3
    s = 1
    while n>=0:
        # nb d'hexagones de taille s =
        # s * nb points du triangle central de taille
        #     n-3s (points a distance >=s du bord)
        res += s * (n+1)*(n+2)/2
        n -= 3
        s += 1
    return res

print sum(H(n) for n in xrange(3,12346))
