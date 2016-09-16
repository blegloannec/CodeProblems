#!/usr/bin/env python

# on utilise les multiplicateurs de Lagrange
# https://fr.wikipedia.org/wiki/Multiplicateur_de_Lagrange
# phi(x1,...,xn) = x1*x2^2*...*xn^n
# psi(x1,...,xn) = x1+...+xn - m
# L(X,l) = phi(X) + l*psi(X)
# dL/dxi = x1*...*x_{i-1}* i*xi^(i-1) *x_{i+1}*...*xn + l
# dL/dl = psi(x)

# On doit resoudre le systeme, pour tout i,  dL/dxi = 0 et dL/dl = 0
# on a xi*dL/dxi = i*phi(X) + l*xi = 0
# donc xi = -i*phi(X)/l
# psi(X)+m = -phi(X)/l * n*(n+1)/2 = m
# donc phi(X) = -2*m*l/(n*(n+1))
# et xi = 2*i*m/(n*(n+1))

# l'enonce ne s'interesse qu'au cas m = n
# donc xi = 2*i/(n+1)

def P(n):
    res = 1.
    for i in xrange(1,n+1):
        res *= (2.*i/(n+1))**i
    return res

print sum(int(P(i)) for i in xrange(2,16))
