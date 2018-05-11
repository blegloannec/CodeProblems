#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# runs in 0.5s with python3

from collections import defaultdict
from math import *

# https://en.wikipedia.org/wiki/Golden_ratio_base

# ring of numbers of the form a + bφ, a and b integers
# (as φ^2 = φ + 1, this is stable by multiplication)
class Zphi: 
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def __add__(self, B):
        return Zphi(self.a+B.a,self.b+B.b)

    def __neg__(self, B):
        return Zphi(-self.a,-self.b)

    def __sub__(self, B):
        return self+(-B)

    def __mul__(self, B):
        return Zphi(self.a*B.a+self.b*B.b,self.a*B.b+self.b*B.a+self.b*B.b)

    def __pow__(self, n):
        assert(n>=0)
        if n==0:
            return Zphi(1,0)
        if n&1==0:
            return (self*self)**(n>>1)
        return self*(self*self)**(n>>1)

    def conj(self): # (that one or its opposite as well, whatever)
        return Zphi(self.a+self.b,-self.b)
    
    def __repr__(self):
        return '%d + %dφ' % (self.a,self.b)


def gen(L):
    U0,U1,U10 = {Zphi(0,0)},set(),set()
    for x in L:
        U10 = U1.copy()
        for u in U0:
            U1.add(u+x)
        U0 |= U10
    return U0,U1

def to_dict(U):
    D = defaultdict(list)
    for u in U:
        D[u.b].append(u.a)
    return D

def meet_middle(S,D1,D2):
    for b in D1:
        if -b in D2:
            for a1 in D1[b]:
                for a2 in D2[-b]:
                    S.add(a1+a2)

def sum_pals(N):
    K = int(log(N,(1+sqrt(5))/2))+1
    phi = Zphi(0,1)
    phim = Zphi(-1,1)
    # symmetric digits pairs
    P = [phi**i + phim**(i+1) for i in range(1,K)]
    k = K//2
    # generating all palindromic numbers from each half of the pairs
    # (we reverse the second half to avoid gluing two 1s in the next step)
    U0,U1 = map(to_dict,gen(P[:k]))
    V0,V1 = map(to_dict,gen(P[:k-1:-1]))
    # meet in the middle
    # (we use a set, even though representations are unique, to avoid
    #  dealing with the b = 0 case separately in meet_middle())
    S = {1}
    meet_middle(S,U0,V0)
    meet_middle(S,U1,V0)
    meet_middle(S,U0,V1)
    return sum(s for s in S if s<=N)

print(sum_pals(10**10))
