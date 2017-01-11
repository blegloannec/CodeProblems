#!/usr/bin/env python

def M(m,k,s,n):
    return n-s if n>m else M(m,k,s,M(m,k,s,n+k))

M91 = lambda n: M(100,11,10,n)

# cf pb 340 for the descending "interval" approach/reasoning
# We can prove that M(m,k,s,n) equals:
#  - by definition n-s for n>m
#  - assuming k>s and with d = k-s > 0, then for n<=m
#    we have values [m-s+1,m-s+d] on any interval
#    [m+1-(l+1)d,m-ld] for l>=0
#  - if k<=s, the function is not defined for n<=m
#    yet the statement of the problem only considers s<k
# here m = 10^6 is fixed and we only consider 1<=s<k<=10^6
# so that the fixed points are only in the "periodic interval part"
# n is a fixed point iff n = m+1-(k+1)d+j = m-s+1+j for k>=0 and 0<=j<d
# modulo d: m+1+j = m-s+1+j, ie s = 0 mod d
# so that the fixed points are straightforwardly enumerated by the naive()
# function below

def naive(m=1000):
    S = 0
    for d in xrange(1,m):
        for s in xrange(d,m-d+1,d):
            for i in xrange(d):
                S += m-s+1+i
    return S

# same computation made efficient
def efficient(m=10**6):
    S = 0
    for d in xrange(1,m):
        k = (m-d)/d
        S += k*d*m-d*d*k*(k+1)/2+k*d*(d+1)/2
    return S

print efficient()
