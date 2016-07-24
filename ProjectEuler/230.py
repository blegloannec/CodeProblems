#!/usr/bin/env python

from math import *
from decimal import *

# https://en.wikipedia.org/wiki/Fibonacci_word
# http://oeis.org/A005614
# F(a,b,n) est une variante des mots de Fibonacci engendre par a->b, b->ab
# de taille F(n) le n-ieme terme de la suite de Fibonacci
# comme ici |A|=|B|=100, pour n donne, le rang k que l'on recherche
# est le premier k pour lequel 100*F(k) >= n
# alors n/100 nous donne la position du bloc (A ou B) correspondant
# a la position reherchee
# et n%100 nous donne la position a l'interieur de ce bloc
# il ne reste plus qu'a etre capable de determiner si un bloc est
# de type A ou B a partir de sa position

def rang(n):
    u0,u1 = 1,1
    while u1<n:
        u1,u0 = u1+u0,u1
    return u1

## experimentations pour la formule explicite
phi = (1+Decimal(5).sqrt())/2
s = {0:[1],1:[0,1]}
def expe():
    u = [0]
    for i in xrange(10):
        u = [x for y in u for x in s[y]]
        v = [int((n+1)*phi)-int(n*phi)-1 for n in xrange(len(u),0,-1)]
        print u==v


# formule explicite
def bit(r,n):
    return int((r-n+1)*phi)-int((r-n)*phi)-1

#W = ['1415926535','8979323846']
W = ['1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679','8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196']

def D(W,n):
    w = len(W[0])
    r = rang((n+w-1)/w)
    b = bit(r,(n-1)/w)
    return int(W[b][(n-1)%w])

def main():
    #print D(W,35)
    print sum(D(W,(127+19*i)*7**i)*10**i for i in xrange(18))

#expe()
main()
