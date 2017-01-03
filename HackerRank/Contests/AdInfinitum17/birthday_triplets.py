#!/usr/bin/env python

import sys
from math import sqrt

# solution pas forcement attendue et n'utilisant pas f4 !
# considerons le polynome P = (X-a)(X-b)(X-c)
# on a P = X^3 - (a+b+c)X^2 + (ab+ac+bc)X - abc
# connaissant f1 = a+b+c, f2 et f3 on peut facilement calculer
# les coefficients de P (considerer f1^2 et f1^3)
# on va donc chercher f1 parmi les sqrt(f2) <= f1 <= borne de l'enonce
# pour chaque f1 :
#  - on calcule les coeffs (qui doivent etre entiers) de P
#  - on cherche a par methode de Newton (on itere 20 fois partant de 0,
#    on arrondit a l'entier le plus proche, on teste si c'est une racine de P)
#  - on factorise P = (X-a)Q avec Q de degre 2
#  - on calcule les racines du trinome Q : si on en a 2 reelles, entieres
#    et distinctes, alors on a trouve b et c
#  - si on a reussi toutes les etapes precedentes avec succes, on peut
#    calculer le resultat (3 sommes geometriques)

# NB: alternativement on pourrait utiliser la methode de Cardan pour les
# les equations polynomiales de degre 3, mais c'est moins basique...

P = 10**9+7
N = 15000

def newton(c3,c2,c1,c0,x=0.,n=20):
    P = lambda x: ((c3*x+c2)*x+c1)*x+c0
    Pp = lambda x: (3*c3*x+2*c2)*x+c1
    while n>0:
        x -= P(x)/Pp(x)
        n -= 1
    x = int(round(x))
    return x if P(x)==0 else None

def horner_factor(c3,c2,c1,c0,r):
    d2 = c3
    d1 = c2+r*d2
    d0 = c1+r*d1
    assert(c0+r*d0==0)
    return (d2,d1,d0)

def trinome(a,b,c):
    D = b*b-4*a*c
    if D>0:
        d = int(sqrt(D))
        if d*d==D and (-b-d)%(2*a)==0 and (-b+d)%(2*a)==0:
            return ((-b-d)/(2*a),(-b+d)/(2*a))
    return None

def bezout(a,b):
    if b==0:
        return (a,1,0)
    g,u,v = bezout(b,a%b)
    return (g,v,u-(a/b)*v)

def inv_mod(a,n=P):
    _,u,_ = bezout(a,n)
    return u

I = [0,1]
for a in xrange(2,N+1):
    I.append(inv_mod(a))

def geo(a,l,r):
    if a==1:
        return (r-l+1)%P
    return ((pow(a,r+1,P)-pow(a,l,P))*I[a-1])%P

def main():
    q = int(sys.stdin.readline())
    for _ in xrange(q):
        f2,f3,f4,l,r = map(int,sys.stdin.readline().split())
        for f1 in xrange(int(sqrt(f2)),N+1):
            ff1 = f1*f1-f2
            if ff1&1==0:
                ff0 = f1*f1*f1-f3-3*(f1*f2-f3)
                if ff0%6==0:
                    c2,c1,c0 = -f1,ff1>>1,-ff0/6
                    a = newton(1,c2,c1,c0)
                    if a!=None and 0<3*a<f1:
                        d2,d1,d0 = horner_factor(1,c2,c1,c0,a)
                        bc = trinome(d2,d1,d0)
                        if bc!=None:
                            b,c = bc
                            print (geo(a,l,r)+geo(b,l,r)+geo(c,l,r))%P
                            break

main()
