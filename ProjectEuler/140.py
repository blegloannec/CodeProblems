#!/usr/bin/env python

# meme analyse que pour le pb 137
# on a cette fois x*A(n,x) + A(n+1,x) = A(n+2,x)/x - 3x - 1
# D'ou A(n+2,x) = x^2*A(n,x) + x*A(n+1,x) + 3x^2 + x
# on trouve alors la constante K(x) = (3x^2+x)/(1-x-x^2)
# et pour x<1/phi, A(n,x) -> K(x)

# on fixe K>=1 entier et on cherche x tel que K = (3x^2+x)/(1-x-x^2)
# (K+3)x^2 + (K+1)x - K = 0
# D = 5K^2 + 14K + 1
# x sera rationnel ssi D est un carre
# on cherche donc les solutions entieres K,K' a
# 5K^2 + 14K + 1 = K'^2
# equation diophantienne quadratique (classique)
# on trouve les coeff de generation des solutions via
# https://www.alpertron.com.ar/JQUAD.HTM
# (mais ca ne donne pas les solutions fondamentales)

from math import sqrt

def is_sqr(n):
    r = int(sqrt(n))
    return r*r==n

# code de test pour trouver les solutions fondamentales
def test():
    for K in xrange(1,10**8):
        if is_sqr(5*K*K+14*K+1):
            print K,int(sqrt(5*K*K+14*K+1))

#test()

def main():
    # solutions fondamentales trouvees par test()
    Fond = [(2,7),(5,14),(21,50),(42,97),(152,343),(296,665)]
    sol = []
    for (K0,Kp0) in Fond:
        K,Kp = K0,Kp0
        sol0 = [K]
        while len(sol0)<30:
            K,Kp = -9*K-4*Kp-14,-20*K-9*Kp-28
            if K>0:
                sol0.append(K)
        sol += sol0
    sol.sort()
    print sum(sol[:30])

main()
