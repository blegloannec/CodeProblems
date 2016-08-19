#!/usr/bin/env python

import random
random.seed()

# https://en.wikipedia.org/wiki/Cyclic_number
# Les nombres cycliques sont exactement les portions periodiques
# des decimales des 1/p pour chaque p premier pour lequel la
# periode du developpement de 1/p est p-1.
# Le premier exemple est issu de 1/7, le second de 1/17.
# La taille du nombre est alors p-1, et le nombre est
# le quotient de Fermat (10^(p-1) - 1)/p (entier lorsque
# p premier avec 10).

# Le nb premier p en question ici verifie
# 0.00000000137 <= 1/p < 0.00000000138
# donc 729927007 >= p >= 724637682
# On a donc ~5 millions de nombres a tester.

# Comme on veut eviter d'avoir a calculer ~ 10^9 chiffres
# pour chacun des candidats afin d'obtenir les 5 derniers chiffres,
# on peut plus simplement calculer le quotient de Fermat modulo 10^5.

# Pour les nombres restants on peut calculer la periode (naivement
# ou par Floyd) puis la somme par developpement complet.

def digits(n,b=10):
    c = []
    while n>0:
        c.append(n%b)
        n /= b
    return c

# Miller-Rabin
def witness(a,n,b):
    d = 1
    for i in xrange(len(b)-1,-1,-1):
        x = d
        d = (d*d)%n
        if d==1 and x!=1 and x!=n-1:
            return True
        if b[i]==1:
            d = (d*a)%n
    return d!=1

def miller_rabin(n,s=15):
    b = digits(n-1,2)
    for j in xrange(s):
        if witness(random.randint(1,n-1),n,b):
            return False
    return True

def bezout(a,b):
    if b==0:
        return (a,1,0)
    g,u,v = bezout(b,a%b)
    return (g,v,u-(a/b)*v)

def inv_mod(a,n):
    g,u,_ = bezout(a,n)
    assert(g==1)
    return u # ajouter %n pour solution >0

def qfermod(p,M=10**5):
    return ((pow(10,p-1,M)-1)*inv_mod(p,M))%M

def persum(p):
    r = 1
    per = 0
    S = 0
    while per==0 or r!=1:
        q = 10*r
        S += q/p
        r = q%p
        per += 1
    return per,S

def main():
    for i in xrange(724637683,729927008,2):
        if miller_rabin(i) and qfermod(i)==56789:
            per,S = persum(i)
            if per==i-1:
                print S
                break

main()
