#!/usr/bin/env python

from math import sqrt

# a,b,c progression geometrique <=> b^2 = ac (symetrique en a/c)
# Ecrivons la DE de n^2 par d, n^2 = qd + r avec {q,d,r} en
# progression geometrique.
# On a toujours r<d, donc la progression geometrique est stricte
# (raison rationnelle >1), et soit :
# 1. r<d<q et d^2 = qr
# 2. r<q<d et q^2 = dr
# 3. q<r<d, et r^2 = qd
#    mais alors n^2 = r^2 + r = r(r+1), impossible
# Seuls les cas 1 et 2 sont possibles, mais alors comme r < q et d, on
# a dans les 2 cas aussi bien l'unique DE par d que par q et leur role
# est donc bien symetrique.
# On peut donc supposer sans perte de generalite que r<d<q avec d <= n
# car parmi d et q il y en a au moins un <= n).

# Ecrivons la raison s = d/r = q/d = A/B > 1 irreductible, gcd(A,B) = 1
# d = Ar/B et q = A^2r/B^2, n^2 = A^3r^2/B^3 + r
# comme q est un entier et que A premier avec B, B^2 | r
# on peut donc ecrire r = B^2r' et n^2 = A^3r'^2B + B^2r'
# avec 1 <= B < A < 10^(12/3) et r' >= 1

def is_sqrt(n):
    s = int(sqrt(n))
    return s*s==n

def main():
    N = 10**12
    S = 0
    # un meme nb peut avoir plusieurs DE progressives
    nbs = set()
    for A in xrange(2,10**4):
        for B in xrange(1,A):
            rp = 1
            n2 = A**3*rp**2*B+B**2*rp
            while n2<N:
                if is_sqrt(n2) and n2 not in nbs:
                    S += n2
                    nbs.add(n2)
                rp += 1
                n2 = A**3*rp**2*B+B**2*rp
    print S

main()
