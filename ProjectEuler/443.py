#!/usr/bin/env python

from fractions import gcd
from collections import defaultdict
import random
random.seed()

# Code de test
def test():
    g = 13
    for n in xrange(5,100):
        g0,g = g,g + gcd(n,g)
        if g-g0>1:
            print n,g
        #print n,g

#test()
  
# La plupart du temps, g(n+1) = g(n) + 1.
# Sauf en certains points, pour lesquels on a
# alors toujours g(n) = 3*n (sauf le premier g(6) = 16) :
# 9,17,18,20,21,41,42,83,84,167,168,170,171,176,177,352,353,...
# La suite g(n) est strictement croissante et ces points font des bonds.
# Les bonds ont bien sur lieu lorsque le pgcd > 1.
# En admettant que ce pattern soit correct, si n est un point de la
# suite pour lequel g(n) = 3n, les termes suivants sont
# g(n+k) = 3n+k jusqu'au prochain bond qui a lieu au premier
# n+k pour lequel gcd(n+k+1,3n+k) > 1.
# Or 3n+k = (n+k+1) + 2n-1, donc gcd(n+k+1,3n+k) = gcd(2n-1,n+k+1).
# Si l'on factorise 2n-1, on peut facilement trouver le plus petit k
# pour lequel n+k+1 est multiple d'un facteur premier de 2n-1 (et donc
# n'est pas premier avec), ce qui donne l'emplacement du prochain saut.

# Suffit alors de calculer les sauts < 10^15 et ajouter le nombre de termes
# jusqu'a 10^15 (puisque ce seront des +1 dans la suite g(n)).

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

# Pollard's Rho
def pollard_rho(n):
    c = random.randint(1,n-1)
    f = (lambda x: (x*x+c)%n)
    x = random.randint(0,n-1)
    y = x
    x = f(x)
    y = f(f(y))
    while x!=y:
        p = gcd(n,abs(x-y))
        if 1<p<n:
            return p
        x = f(x)
        y = f(f(y))
    return None

def factorisation(n,D):
    while n>1:
        if miller_rabin(n):
            D[n] += 1
            return D
        f = pollard_rho(n)
        if f!=None:
            factorisation(f,D)
            n /= f
    return D

def full_factorisation(n):
    D = defaultdict(int)
    while n%2==0:
        D[2] += 1
        n /= 2
    return factorisation(n,D)


# PROCHAIN SAUT
def next_jump(n):
    D = full_factorisation(2*n-1)
    m = min((-(n+1))%p for p in D)
    return n+m+1

def main():
    N = 10**15
    n = 9
    while n<N:
        n0,n = n,next_jump(n)
    print 3*n0 + N-n0

main()
