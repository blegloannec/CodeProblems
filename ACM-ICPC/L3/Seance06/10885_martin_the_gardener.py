#!/usr/bin/env python3

from fractions import *
from math import sqrt

# Source principale de la methode :
# Anning & Erdos, Integral distances (1945)
# http://www.ams.org/journals/bull/1945-51-08/S0002-9904-1945-08407-9/S0002-9904-1945-08407-9.pdf

# Algo pour les 2 carres de Fermat
# http://www.les-mathematiques.net/phorum/read.php?5,636257
def f(a,b,c):
    if a==b:
        return (a,c)
    elif a>b+c:
        return f(a-b-c,b,2*b+c)
    return f(b+c-a,a,2*a-c)

# p^2 = a^2+b^2 pour p = 4k+1 premier 
def fermat(p):
    a,c = f((p-1)//4,1,1)
    return (2*a,c)

# https://fr.wikipedia.org/wiki/Triplet_pythagoricien
# si p = 4n+1 premier alors p = a^2+b^2 par les 2 carres de fermat
# et par identite de Lagrange, p^2 = (a^2+b^2)^2 = (a^-b^2)^2 + (2ab)^2

# triplet pythagoricien p^2 = a^2 + b^2 pour p = 4k+1 premier
def pytha(p):
    a,b = fermat(p)
    return (a*a-b*b,2*a*b)

# Crible pour les premiers de la forme 4k+1
def erat(n):
    l = list(range(2,n+1))
    s = int(sqrt(n))+1
    for i in range(2,s):
        for k in range(2*i,n+1,i):
            l[k-2] = -1
    return filter((lambda x: x>0 and x%4==1),l)

def ppcm(a,b):
    return a*b//gcd(a,b)

# Generation des points par la methode d'Erdos-Anning
def gen(L):
    P = erat(100)
    pts = [(Fraction(-1,2),Fraction(0,1)),(Fraction(1,2),Fraction(0,1))]
    for p in P:
        a,b = pytha(p)
        bp = Fraction(b*b,p*p)
        # (x,y) a distance b/p de (-1/2,0)
        # (x-1/2)^2 + y^2 = b^2/p^2
        # x^2 + y^2 = 1/4
        # Solution :
        x = Fraction(1,2)-bp
        y = Fraction(a*b,p*p)
        pts.append((x,y))
        # symetrie horizontale y <-> -y
        pts.append((x,-y))
        # symetrie a <-> b equivalente a symetrie verticale x <-> -x
        pts.append((-x,y))
        pts.append((-x,-y))
    pts = pts[:L]
    a = 1
    for x,y in pts:
        a = ppcm(a,ppcm(x.denominator,y.denominator))
    for i in range(L):
        x,y = pts[i]
        pts[i] = ((a*x).numerator,(a*y).numerator)
    #for i in range(L):
    #    for j in range(L):
    #        x1,y1 = pts[i]
    #        x2,y2 = pts[j]
    #        print sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
    for x,y in pts:
        print(x+a//2,y+a//2)
  
gen(13)
