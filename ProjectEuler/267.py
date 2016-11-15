#!/usr/bin/env python

import sys
sys.setrecursionlimit(1100)

# lorsqu'on gagne, le capital est multiplie par (1+2f)
# lorsqu'on perd, le capital est multiplie par (1-2f)
# l'ordre des gains/pertes n'a aucune importance
# soit g le nb de gains et posons B = 10^9
# on veut (1+2f)^g * (1-f)^(1000-g) >= B
# ie g*log(1+2f) + (1000-g)*log(1-f) >= log(B)
# ie g >= (log(B)-1000*log(1-f)) / (log(1+2f)-log(1-f))
# le nb de gains a atteindre pour etre milliardaire
# on cherche donc le f qui minimise g

# on pourrait deriver et chercher le 0 par dichotomie, mais on l'a deja
# assez fait comme ca dans PE... cette fois on donne la fonction a Sage :
# F = lambda x: (log(10**9)-1000*log(1-x)) / (log(1+2*x)-log(1-x))
# find_local_minimum(F(x),0.1,0.9,tol=1e-30)
# (431.25594829396044, 0.1468839206433015)
# reste a calculer la proba d'avoir g >= 432

def binom(n,p):
    return 1 if p==0 else n*binom(n-1,p-1)/p

print float(sum(binom(1000,k) for k in xrange(432,1001)))/2**1000
