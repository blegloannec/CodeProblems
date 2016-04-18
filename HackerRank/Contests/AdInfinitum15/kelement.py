#!/usr/bin/env python

import sys

# P(n,k) = nb de listes de taille k dont la somme vaut n
# P(n,k) = sum(P(n-i,k-1), i=1..n) # par choix du dernier element
# ce que l'on peut reformuler :
# P(n,k) = P(n-1,k-1)+P(n-1,k)
# on retrouve la formule du binom et on remarque que
# P(n,k) = k-1 parmi n-1
## Justification directe :
# trouver une telle liste c'est decouper n ecrit en unaire
# en k morceaux de taille au moins 1
# c'est donc placer k-1 barres de separation parmi n-1 emplacements

M = 10**9+7

# binom std
#def binom(n,k):
#    res = 1
#    for i in xrange(k):
#        res = ((res*(n-i))/(i+1))
#    return res

# inversion modulo par euclide etendu
# (coeff de bezout)
def bezout(a,b):
    if b==0:
        return (1,0)
    u,v = bezout(b,a%b)
    return (v,u-(a/b)*v)

def inv(a,p):
    return bezout(a,p)[0]%p


# binom modulaire std
#def binom_mod(n,k,p):
#    res = 1
#    for i in xrange(k):
#        res = (res*(n-i)*inv(i+1,p))%p
#    return res


# binom modulaire bis
# avec precalcul des factorielles modulo
# (mais pas de leurs inverses car trop lent)
FACT = [1]*(2*10**6+1)
#INV_FACT = [1]*(2*10**6+1)

def precomp():
    for i in xrange(2,len(FACT)):
        FACT[i] = (i*FACT[i-1])%M
        #INV_FACT[i] = inv(FACT[i],M)

def binom_mod(n,k):
    return (FACT[n]*inv(FACT[k],M)*inv(FACT[n-k],M))%M


def main():
    precomp()
    T = int(sys.stdin.readline())
    for t in xrange(T):
        N,K = map(int,sys.stdin.readline().split())
        if K==1:
            print 1
        else:
            print binom_mod(N-1,K-1)

main()
