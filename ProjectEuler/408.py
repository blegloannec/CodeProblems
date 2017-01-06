#!/usr/bin/env python

from math import sqrt

# 19s with pypy, most of the time spent to compute the
# inadmissible points and build their DAG

N = 10**7
P = 10**9+7
S = int(sqrt(N))

def is_sqr(n):
    r = int(sqrt(n))
    return r*r==n

def bezout(a,b):
    if b==0:
        return (a,1,0)
    g,u,v = bezout(b,a%b)
    return (g,v,u-(a/b)*v)

def inv_mod(a,n=P):
    _,u,_ = bezout(a,n)
    return u%n

F,IF = [1],[1]
for i in xrange(1,2*N+1):
    F.append((F[-1]*i)%P)
    IF.append(inv_mod(F[-1]))
            
def binom(n,p):
    return (F[n]*(IF[p]*IF[n-p])%P)%P

# cf pb 15+
def paths((x0,y0),(x1,y1)):
    dx,dy = x1-x0,y1-y0
    if dx==0 or dy==0:
        return 1
    return binom(dx+dy,dx)

# inadmissibles points + (0,0) & (N,N)
I = [(0,0)]
for x in xrange(1,S+1):
    for y in xrange(x,S+1):
        if is_sqr(x*x+y*y):
            I.append((x*x,y*y))
            if x!=y:
                I.append((y*y,x*x))
I.append((N,N))

# I points DAG
# (x0,y0) --> (x1,y1) iff (x1,y1) reachable from (x0,y0)
G = [[] for _ in xrange(len(I))]
for u in xrange(len(I)):
    for v in xrange(len(I)):
        if u!=v and I[u][0]<=I[v][0] and I[u][1]<=I[v][1]:
            G[u].append(v)

# counting admissible paths by inclusion-exclusion
cpt = [None for _ in xrange(len(I))]
cpt[-1] = -1
def count(u=0):
    if cpt[u]!=None:
        return cpt[u]
    res = 0
    for v in G[u]:
        res = (res - paths(I[u],I[v])*count(v))%P
    cpt[u] = res
    return res

print count()
