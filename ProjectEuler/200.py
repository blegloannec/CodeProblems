#!/usr/bin/env python

from math import sqrt
from heapq import *
import random
random.seed()

def sieve_list(N):
    P = [True for _ in xrange(N)]
    L = []
    P[0] = False
    P[1] = False
    for i in xrange(2,N):
        if P[i]:
            L.append(i)
            for k in xrange(2*i,N,i):
                P[k] = False
    return L

# not so clever way of generating squbes in order
def squbes():
    P = sieve_list(10**6)
    H = [(0,0,0)]
    S = set([(0,0)])
    while H:
        sq,ip,iq = heappop(H)
        S.remove((ip,iq))
        if ip!=iq:
            yield sq
        if ip<len(P)-1 and (ip+1,iq) not in S:
            heappush(H,(P[ip+1]**2*P[iq]**3,ip+1,iq))
            S.add((ip+1,iq))
        if iq<len(P)-1 and (ip,iq+1) not in S:
            heappush(H,(P[ip]**2*P[iq+1]**3,ip,iq+1))
            S.add((ip,iq+1))

def contains200(x):
    return (str(x).find('200')>=0)

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

def prime_proof(x):
    sx = x
    p10 = 1
    while sx>0:
        dx = sx%10
        for d in xrange(10):
            if d==dx:
                continue
            y = x + (d-dx)*p10
            if y>0 and miller_rabin(y):
                return False
        sx /= 10
        p10 *= 10
    return True

def main():
    cpt = 0
    for x in squbes():
        if contains200(x) and prime_proof(x):
            cpt += 1
        if cpt==200:
            print x
            break

main()
