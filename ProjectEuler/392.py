#!/usr/bin/env python

# terrible gradient descent :/ ... runs in ~70s with pypy

from math import sqrt

# Par symetrie, on ne raisonne que sur le quart de
# cercle superieur droit avec n/2 points. Il suffit egalement de
# ne s'occuper que des lignes verticales car a chacune sera
# associee la ligne horisontale correspondante passant par le
# point d'intersection avec le cercle.
# On place donc les lignes verticales aux abcisses x1,...,xk, k = n/2
# on pose (x0,y0) = (0,1) et (x{k+1},y{k+1}) = (1,0)
# x^2+y^2 = 1 donc y = sqrt(1-x^2)
# A(x1,...,xk) = sum( (x{i+1}-xi)*yi, i=0..k )
# dA/dxi = y{i-1} - d/dxi[(x{i+1}-xi)*sqrt(1-xi^2)]
#        = y{i-1} - sqrt(1-xi^2) - (x{i+1}-xi)*xi/sqrt(1-xi^2)
#        = y{i-1} - yi - (x{i+1}-xi)*xi/yi

# Approche : descente de gradient avec recherche dichotomique
# du point d'annulation de la derivee de la fonction le long de
# la direction de descente.
# On suppose ici a priori que l'approche theorique consistant a resoudre
# le systeme non lineaire grad(X) = 0 est trop compliquee et que la
# differentielle du gradient serait un peu moche donc on laisse la methode
# de Newton de cote.

def valX(X,i):
    return 1. if i>=len(X) else X[i]

def valY(X,i):
    return 1. if i<0 else sqrt(1-X[i]*X[i])

# aire
def A(X):
    a = X[0]
    for i in xrange(len(X)-1):
        a += (X[i+1]-X[i])*valY(X,i)
    a += (1.-X[len(X)-1])*valY(X,len(X)-1)
    return a

# gradient de A
def grad(X):
    return [valY(X,i-1)-valY(X,i)-(valX(X,i+1)-X[i])*X[i]/valY(X,i) for i in xrange(len(X))]

def norm2(X):
    return sum(x*x for x in X)

# derivee de t -> A(X-t*G)
def deriv(X0,G0,t):
    G = grad([X0[i]-t*G0[i] for i in xrange(len(X0))])
    res = 0.
    for i in xrange(len(X0)):
        res += -G0[i]*G[i]
    return res

# recherche dicho du 0 de la derivee
def dicho(X,G,b0):
    a,b = 0.,b0
    da,db = deriv(X,G,a),deriv(X,G,b)
    assert(da*db<0)
    while b-a>1e-3:
        m = (a+b)/2.
        dm = deriv(X,G,m)
        if a==m or b==m:
            return m
        if da*dm>0:
            a,da = m,dm
        else:
            b,db = m,dm
    return m

def main():
    N = 200
    X = [(i+1.)/(N+1.) for i in xrange(N)]
    cpt = 0
    # descente de gradient
    while True:
        G = grad(X)
        if norm2(G)<1e-16:
            break
        # borne sup arbitraire 0.15 pour N=200, 1. pour N=5 
        t0 = dicho(X,G,0.15)
        X = [X[i]-t0*G[i] for i in xrange(len(X))]
        cpt += 1
        if cpt==10000:
            # converges to 3.14867344349
            print 4*A(X)
            cpt = 0
    print 4*A(X)

main()
