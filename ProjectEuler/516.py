#!/usr/bin/env python

from math import log
import random
random.seed()
from bisect import *

# Soit Q l'ensemble des nb premiers q>5 tels que
# q-1 est un nb de Hamming.
# Comme 2-1 = 1, 3-1 = 2 et 5-1 = 2^2,
# les solutions recherchees sont les nb de la forme
# 2^a x 3^b x 5^c x (un produit de nombres *distincts* de Q)

# Miller-Rabin
def digits(n,b=10):
    c = []
    while n>0:
        c.append(n%b)
        n /= b
    return c

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

# Generation de l'ensemble Q
def genQ(N):
    Q = []
    for a in xrange(int(log(N,2))+1):
        for b in xrange(int(log(N,3))+1):
            for c in xrange(int(log(N,5))+1):
                x = 2**a * 3**b * 5**c
                if x>5 and x<N and miller_rabin(x+1):
                    Q.append(x+1)
    Q.sort()
    return Q

def genLQ(N,Q,x=1,i=0):
    if i==len(Q) or Q[i]*x>N:
        yield x
    else:
        for n in genLQ(N,Q,x,i+1):
            yield n
        if x*Q[i]<=N:
            for n in genLQ(N,Q,x*Q[i],i+1):
                yield n

def gen235(N):
    L235 = []
    for a in xrange(int(log(N,2))+1):
        for b in xrange(int(log(N,3))+1):
            for c in xrange(int(log(N,5))+1):
                x = 2**a * 3**b * 5**c
                if x<=N:
                    L235.append(x)
    L235.sort()
    return L235

def main():
    N = 10**12
    M = 2**32
    Q = genQ(N)
    L235 = gen235(N)
    S235 = L235[:]
    for i in xrange(1,len(S235)):
        S235[i] += S235[i-1]
    res = 0
    for n in genLQ(N,Q):
        res = (res + n*S235[bisect_right(L235,N/n)-1])%M
    print res

main()
