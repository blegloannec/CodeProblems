#!/usr/bin/env python

import sys
from math import sqrt

# probleme "easy" car un lien est donne dans l'enonce vers :
# http://math.stackexchange.com/questions/124408/finding-a-primitive-root-of-a-prime-number

# les racines primitives sont les generateurs de (Z/nZ)* (d'ordre phi(n))
# s'il en existe, alors (Z/nZ)* est monogene fini donc cyclique et donc
# isomorphe a Z/phi(n)Z et donc il y en a phi(phi(n))
# il en existe toujours pour n = p premier (car alors Z/nZ = Fp et l'on sait
# que Fp* est cyclique)

# pour les trouver, on decompose phi(n) (= p-1 ici) en facteurs premiers
# phi(n) = prod(pi^ai)
# et on les cherche parmi r = 2,...,n-1 en testant : il faut et il
# suffit d'avoir r^(phi(n)/pi) != 1 mod n pour tout i pour s'assurer que
# l'ordre de r est phi(n)

def decomp(n):
    F = []
    m = 0
    while n%2==0:
        n /= 2
        m += 1
    if m>0:
        F.append((2,m))
    i = 3
    s = int(sqrt(n))+1
    while n>1 and i<s:
        m = 0
        while n%i==0:
            n /= i
            m += 1
        if m>0:
            F.append((i,m))
        i += 2
    if n>1:
        F.append((n,1))
    return F

def eulerphi(decomp):
    res = 1
    for (p,m) in decomp:
        res *= (p-1)*p**(m-1)
    return res

def primitive(r,p,Dphi):
    return all(pow(r,(p-1)/f,p)!=1 for (f,_) in Dphi)

def main():
    p = int(sys.stdin.readline())
    phi = p-1
    Dphi = decomp(phi)
    phiphi = eulerphi(Dphi)
    r = 2
    while not primitive(r,p,Dphi):
        r += 1
    print r,phiphi

main()
