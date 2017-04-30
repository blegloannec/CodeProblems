#!/usr/bin/env python3

from math import *

# https://en.wikipedia.org/wiki/Simple_linear_regression
# y = ax+b
def linear_regression(P):
    N = len(P)
    xmoy,ymoy = 0,0
    for (x,y) in P:
        xmoy += x
        ymoy += y
    xmoy /= N
    ymoy /= N
    a,d = 0,0
    for (x,y) in P:
        a += (x-xmoy)*(y-ymoy)
        d += (x-xmoy)**2
    a /= d
    b = ymoy - a*xmoy
    return (a,b)

def variance(P,f,a,b):
    v = 0
    for (x,y) in P:
        v += (y - f(a*x+b))**2
    v /= len(P)
    return v

def log0(x):
    return 0 if x<=0 else log(x)

newton_it = 20

def inv_nlogn(y):
    x = y/log(y)
    for _ in range(newton_it):
        x -= (x*log(x)-y)/(1+log(x))
    return x

def inv_n2logn(y):
    x = sqrt(y)/log(y)
    for _ in range(newton_it):
        x -= (x*x*log(x)-y)/(x+2*x*log(x))
    return x

def main():
    N = int(input())
    P = []
    for _ in range(N):
        P.append(tuple(map(int,input().split())))
    ymoy = sum(y for (_,y) in P)/N
    O = ['O(n)','O(n^2)','O(n^3)','O(2^n)','O(n log n)','O(n^2 log n)','O(log n)']
    F = [(lambda x: x),(lambda x: x*x),(lambda x: x*x*x),exp,(lambda x: x*log0(x)),(lambda x: x*x*log0(x)),(lambda x: ymoy*log0(x))]
    Finv = [(lambda x: x),sqrt,(lambda x: x**(1/3)),log,inv_nlogn,inv_n2logn,(lambda x: exp(x/ymoy))]
    vmin = float('inf')
    for i in range(len(O)):
        Q = list(map((lambda X: (X[0],Finv[i](X[1]))),P))
        a,b = linear_regression(Q)
        v = variance(P,F[i],a,b)
        if v<vmin:
            vmin = v
            if i==0 and a<0.5:
                res = 'O(1)'
                break
            else:
                res = O[i]
    print(res)

main()
