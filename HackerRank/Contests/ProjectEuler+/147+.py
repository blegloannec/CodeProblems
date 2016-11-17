#!/usr/bin/env python

import sys

def axis_para(n,m):
    return n*(n+1)/2 * m*(m+1)/2

# terrible...
def cross(n,m):
    cpt = 0
    for x in xrange(2*n-1):
        for y in xrange(1,2*m):
            if x%2==y%2:
                X,Y = float(x)/2+1,float(y)/2
                for i in xrange(min(y,2*n-x)):
                    for j in xrange(min(2*n-x,2*m-y)):
                        X0,Y0 = X+0.5*i+0.5*j,Y-0.5*i+0.5*j
                        if 0<=X0<=n and 0<=Y0<=m:
                            cpt += 1
    return cpt

# On conjecture qu'il existe une formule polynomiale en n et m.
# Par interpolation de Lagrange (avec Sage), on decouvre que
# cross(x,x) = 2/3*x^4 - 1/6*x^2 - 1/2*x

# Supposons qu'il existe une formule polynomiale a 2 variables en n et m de degre d
# et ecrivons P(n,m) = sum( a(i,j)*n^i*m^j, i+j<=d ) a k termes
# que l'on reecrit P(n,m) = sum( ai * n^xi * m^yi, i=1..k )
# Choisissons k points (ni,mi) tels que la matrice M =
# [n1^x1*m1^y1, ..., n1^xk*m1^yk]
# ...
# [nk^x1*m1^y1, ..., nk^xk*mk^yk]
# soit inversible (de rang k)
# alors en posant A = [a1,...,ak] le vecteur colonne des coeffs, on doit avoir
# M*A = [P(n1,m1),...,P(nk,mk)]
# ce qui permet de calculer A en inversant M
# avec Sage, on calcule :
# cross(n,m) = 4/3*m*n^3 - 2/3*n^4 - 1/3*m*n + 1/6*n^2 - 1/2*n pour m>=n

def crossbis(n,m):
    if m<n:
        m,n = n,m
    return (8*m*n**3 - 4*n**4 - 2*m*n + n**2 - 3*n)/6

def crosssum(n,m):
    s = 0
    for a in xrange(1,n+1):
        for b in xrange(1,m+1):
            s += crossbis(a,b)
    return s

def genM(d):
    XY,NM,P = [],[],[]
    for x in xrange(d+1):
        for y in xrange(d+1):
            XY.append((x,y))
            NM.append((x+1,x+y+1))
            P.append(crosssum(x+1,x+y+1)) # choix des valeurs avec m>=n
    M = []
    for (n,m) in NM:
        M.append([n**x*m**y for (x,y) in XY])
    return (M,P,XY)

# on fait la meme chose avec crosssum et on calcule avec Sage :
# crosssum(n,m) = 1/6*m^2*n^4 - 2/15*m*n^5 + 1/30*n^6 + 1/3*m^2*n^3 - 1/6*m*n^4 + 1/30*n^5
# + 1/12*m^2*n^2 + 1/6*m*n^3 - 1/12*n^4 - 1/12*m^2*n - 1/12*m*n^2 -
# 17/60*m*n + 1/20*n^2 - 1/30*n pour m>=n

def crosssumbis(n,m):
    if m<n:
        m,n = n,m
    return (10*m**2*n**4 - 8*m*n**5 + 2*n**6 + 20*m**2*n**3 - 10*m*n**4 + 2*n**5 + 5*m**2*n**2 + 10*m*n**3 - 5*n**4 - 5*m**2*n - 5*m*n**2 - 17*m*n + 3*n**2 - 2*n)/60


# idem pour les axis_para
def axissum(n,m):
    s = 0
    for a in xrange(1,n+1):
        for b in xrange(1,m+1):
            s += axis_para(a,b)
    return s

def genM_axispara(d):
    XY,NM,P = [],[],[]
    for x in xrange(d+1):
        for y in xrange(d+1):
            XY.append((x,y))
            NM.append((x+1,y+1))
            P.append(axissum(x+1,y+1))
    M = []
    for (n,m) in NM:
        M.append([n**x*m**y for (x,y) in XY])
    return (M,P,XY)

# et tant qu'a faire on fait ca aussi pour la somme des axis para et on trouve
# axissum(n,m) = 1/36*m^3*n^3 + 1/12*m^3*n^2 + 1/12*m^2*n^3 + 1/18*m^3*n + 1/4*m^2*n^2 +
# 1/18*m*n^3 + 1/6*m^2*n + 1/6*m*n^2 + 1/9*m*n

def axissumbis(n,m):
    return (m**3*n**3 + 3*m**3*n**2 + 3*m**2*n**3 + 2*m**3*n + 9*m**2*n**2 + 2*m*n**3 + 6*m**2*n + 6*m*n**2 + 4*m*n)/36
    
def main():
    P = 10**9+7
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        M,N = map(int,sys.stdin.readline().split())
        print axissumbis(M,N)%P,crosssumbis(M,N)%P

main()
