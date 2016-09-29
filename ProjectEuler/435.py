#!/usr/bin/env python

from fractions import gcd

# L'analyse menee aux pb 137 et 140 nous dit que
# la fonction generatrice de Fibonacci pour les termes
# initiaux F1 et F2 est g(F1,F2,x) = ((F2-F1)x^2 + F1x) / (1-x-x^2)

# Methode 1 (fail) : Fn(x) = g(1,1,x) - g(fibo(n),fibo(n+1),x)
# ca marcherait bien modulo un nb premier, (voire un produit de facteurs
# premiers sans multiplicite), mais on ne peut pas exploiter cela
# modulo 15! car le denominateur ne sera pas toujours premier avec...

# Methode 2 : 15! = 2**11 * 3**6 * 5**3 * 7**2 * 11 * 13
# les facteurs sont petits et x <= 100 donc il est possible d'exploiter
# la periodicite des Fi*x^i modulo chaque facteur

def lcm(a,b):
    return a*b/gcd(a,b)

# la fonction (x,y) -> (y,(x+y)%p) est inversible
# donc on aura une vraie periodicite des termes et
# pas seulement une ultime-periodicite
def fibo_mod(p):
    F = [0,1,1]
    while (F[-2],F[-1])!=(0,1):
        F.append((F[-2]+F[-1])%p)
    F.pop()
    F.pop()
    return F

# revoie pre-periode + periode des x^i mod p
# et indice du debut de la periode
def pow_mod(x,p):
    y = 1
    T = [-1 for _ in xrange(p)]
    X = []
    t = 0
    while T[y]<0:
        T[y] = t
        X.append(y)
        t += 1
        y = (y*x)%p
    return X,T[y]

def bezout(a,b):
    if b==0:
        return (a,1,0)
    g,u,v = bezout(b,a%b)
    return (g,v,u-(a/b)*v)

def rev_chinois(a,p,b,q):
    _,u,v = bezout(p,q)
    return (b*u*p+a*v*q)%(p*q)

P = 1307674368000
Facteurs = [2**11,3**6,5**3,7**2,11,13]
Fmod = [fibo_mod(f) for f in Facteurs]

def poly(n,x):
    res,prod = 0,1
    for i in xrange(len(Facteurs)):
        f,fmod = Facteurs[i],Fmod[i]
        T,p0 = pow_mod(x,f)
        pper = len(T)-p0
        ind = (lambda x: x if x<len(T) else p0+(x-p0)%pper)
        # periode commune (des Fi*x^i mod f)
        g = lcm(len(fmod),len(T)-p0)
        # calcul de la somme des termes
        X = [0]
        for i in xrange(1,p0+g):
            X.append((X[-1]+fmod[i%len(fmod)]*T[ind(i)])%f)
        # preperiode
        X0 = X[p0-1] if p0>0 else 0
        # periode
        Xg = (X[-1]-X[p0-1])%f
        assert(n>=p0)
        resf = (X0 + ((n-p0)/g)*Xg + (X[p0+(n-p0)%g]-X0))%f
        res = rev_chinois(res,prod,resf,f)
        prod *= f
    return res

def main():
    N = 10**15
    R = 0
    for x in xrange(1,101):
        R = (R+poly(N,x))%P
    print R

main()
