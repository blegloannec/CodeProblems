#!/usr/bin/env python

from math import sqrt

# A = (0,0)
# D = 25*(sqrt(2)-1)
# Pi = (D+10*i,yi) avec yi variable
# B = (50*sqrt(2),50*sqrt(2))
# T = d(A,P0)/10 + d(P0,P1)/9 + ... + d(P4,P5)/5 + d(P5,B)/10
# dT/dyi = 1/c(i) * (y(i)-y(i-1)) / d(P(i-1),P(i)) + 1/c(i+1) * (y(i)-y(i+1)) / d(P(i),P(i+1))
# puis descente de gradient

C = [10,9,8,7,6,5,10]
D = 25*(sqrt(2)-1)
X = [0,D,D+10,D+20,D+30,D+40,D+50,50*sqrt(2)]
Y = X[:]

def T():
    return sum(sqrt((X[i]-X[i+1])**2+(Y[i]-Y[i+1])**2)/C[i] for i in xrange(7))

def dc(i):
    return sqrt((X[i]-X[i+1])**2+(Y[i]-Y[i+1])**2)*C[i]

def grad():
    return [(Y[i]-Y[i-1])/dc(i-1)+(Y[i]-Y[i+1])/dc(i) for i in xrange(1,7)]

def norm2(X):
    return sum(x*x for x in X)

def main():
    global Y
    # descente de gradient
    while True:
        G = grad()
        if norm2(G)<1e-16:
            break
        t0 = 30. # arbitraire ici
        for i in xrange(1,7):
            Y[i] -= t0*G[i-1]
    print T()

main()
