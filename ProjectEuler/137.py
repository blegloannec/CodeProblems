#!/usr/bin/env python

# soit A(n,x) = sum( x^i*F_i, i=1..n ) les sommes partielles
# on remarque par le calcul (en forcant le destin pour utiliser
# la relation de Fibonacci) que x*A(n,x) + A(n+1,x) = A(n+2,x)/x - 1
# D'ou A(n+2,x) = x^2*A(n,x) + x*A(n+1,x) + x
# on commence par eliminer la constante
# on pose K(x) = x/(1-x-x^2) et B(n,x) = A(n,x) - K(x)
# on a B(n+2,x) = x^2*B(n,x) + x*B(n+1,x)
# on a une suite recurrente lineaire (sans partie constante)
# equation caracteristique B^2 - x*B - x^2 = 0
# D = 5*x^2
# solutions B = (x +/- x*sqrt(5))/2, soit x*phi et x*phi'
# donc B(n,x) = L*(x*phi)^n + M*(x*phi')^n avec L et M des
# trucs infames (L = (x*x+x-phip*(x*x-x))/(x*x*(phi*phi-phi*phip)))
# et a la limite n -> +inf :
# lim B(n,x) = lim L*(x*phi)^n = +inf si x*phi>1 et 0 si x*phi<1
# autrement dit, on s'interesse uniquement aux x < 1/phi
# et dans ce cas A(n,x) -> K(x)

# NB (a posteriori) : l'analyse precedente est correcte, mais il aurait suffit
# d'aller chercher la fontion generatrice de Fibonacci sur wikipedia...

# on fixe K>=1 entier et on cherche x tel que K = x/(1-x-x^2)
# Kx^2 + (K+1)x -K = 0
# D = 5K^2 + 2K + 1
# x sera rationnel ssi D est un carre
# on cherche donc les solutions entieres K,K' a
# 5K^2 + 2K + 1 = K'^2
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
        if is_sqr(5*K*K+2*K+1):
            print K,int(sqrt(5*K*K+2*K+1))

#test()

def main():
    Fond = [(2,5),(15,34),(104,233)]
    sol = []
    for (K0,Kp0) in Fond:
        K,Kp = K0,Kp0
        sol0 = [K]
        while len(sol0)<15:
            K,Kp = -9*K-4*Kp-2,-20*K-9*Kp-4
            if K>0:
                sol0.append(K)
        sol += sol0
    sol.sort()
    print sol[14]

main()
