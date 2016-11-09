#!/usr/bin/env python

from math import sqrt
from collections import defaultdict

def line_int(i):
    i -= 1
    j = i*(i+1)/2+1
    return (j,j+i)

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

# crible pour marquer les nb premiers L <= n <= R
def prime_int(L,R):
    P = sieve_list(int(sqrt(R))+1)
    D = [True for _ in xrange(R-L+1)]
    for p in P:
        for n in xrange(max(2,(L+p-1)/p)*p,R+1,p):
            D[n-L] = False
    return D

def line_count(i,P,x0,C):
    x,y = line_int(i)
    for p in xrange(x,y+1):
        if P[p-x0]:
            if p==x:
                V = [p-i+1,p-i+2,p+1,p+i,p+i+1]
            elif p==y-1:
                V = [p-i,p-i+1,p-1,p+1,p+i-1,p+i,p+i+1]
            elif p==y:
                V = [p-i,p-1,p+i-1,p+i,p+i+1]
            else:
                V = [p-i,p-i+1,p-i+2,p-1,p+1,p+i-1,p+i,p+i+1]
            for v in V:
                if P[v-x0]:
                    C[p].append(v)

def line_sum(i):
    x0,_ = line_int(i-2)
    _,y0 = line_int(i+2)
    P = prime_int(x0,y0)
    C = defaultdict(list)
    line_count(i-1,P,x0,C)
    line_count(i,P,x0,C)
    line_count(i+1,P,x0,C)
    x,y = line_int(i)
    S = 0
    for p in xrange(x,y+1):
        if P[p-x0] and (len(C[p])>=2 or (len(C[p])==1 and len(C[C[p][0]])>=2)): 
            S += p
    return S

print line_sum(5678027)+line_sum(7208785)
