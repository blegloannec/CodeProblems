from math import gcd, atan2, tau
from heapq import *
from itertools import chain, groupby, islice
import matplotlib.pyplot as plt

norm2 = lambda x,y: x*x+y*y

## Pythagorean generators (useless...)
#  /!\ Contrary to what is indicated in the statement, the n_i are NOT ints,
#      the problem is NOT related to Pythagorean triples...
# Euclid's formula to generate primitive pythagorean triples
# https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
def pythagorean(N):
    for m in range(2, N):
        n0s = 1 + (m&1)
        for n in range(n0s, m, 2):
            if gcd(m,n)==1:
                a,b,c = m*m-n*n, 2*m*n, m*m+n*n
                yield (a,b,c)

# custom version to generate all triples we want in incr. c order
def gen_pytha_vecs():
    Q = [(1, 1, 0, 1)]
    while Q:
        kc,m,n,k = heappop(Q)
        #assert 0<=n<m
        #assert k>0
        #assert kc%k==0
        if gcd(m,n)==1:
            a = m*m-n*n
            b = 2*m*n
            c = norm2(m,n)
            #assert k*c==kc
            yield (k*a, k*b) #, kc)
            heappush(Q, ((k+1)*c, m, n, k+1))
        if k==1:
            if n+1<m:
                heappush(Q, (norm2(m,n+1), m, n+1, 1))
            if n==0:
                heappush(Q, (norm2(m+1,0), m+1, 0, 1))


## Actual problem generator
# generates vectors in incr. order of norm
def gen_all_vecs():
    Q = [(1, 1, 0)]
    while Q:
        d2,x,y = heappop(Q)
        yield (x,y)
        if y==0:
            heappush(Q, (norm2(x+1,0), x+1, 0))
        if y+1<=x:
            heappush(Q, (norm2(x,y+1), x, y+1))


## "Spiral"
# groups vectors by norm
def gen_groups(gen=gen_all_vecs):
    for _,G in groupby(gen(), key=(lambda xy: norm2(*xy))):
        yield tuple(G)

def babylonian_spiral(n_steps):
    X = [0,0]
    Y = [0,1]
    rot = lambda x,y: ((x,y), (-x,y), (x,-y), (-x,-y), (y,x), (-y,x), (y,-x), (-y,-x))
    for V in islice(gen_groups(), 1, n_steps+1):
        amin = float('inf')
        for dx,dy in chain(*(rot(*p) for p in V)):
            a = (-(atan2(dy,dx) - atan2(Y[-1]-Y[-2], X[-1]-X[-2]))) % tau
            # NB: minimizing the angle at the origin between successive points
            #     also leads to an interesting spiral:
            #a = (-(atan2(Y[-1]+dy,X[-1]+dx) - atan2(Y[-1], X[-1]))) % tau
            if 0<a<amin:
                amin = a
                bx = dx; by = dy
        X.append(X[-1]+bx)
        Y.append(Y[-1]+by)
    return X,Y


if __name__=='__main__':
    plt.plot(*babylonian_spiral(20000), lw=0.4)
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
