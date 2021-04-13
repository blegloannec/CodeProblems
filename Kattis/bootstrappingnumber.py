#!/usr/bin/env python3

from math import log

# Newton's method for x -> x log x
def inv_nlogn(y):
    if y==0.: return 1.
    x = y/log(y)
    for _ in range(10):
        x -= (x*log(x)-y)/(1+log(x))
    return x

# binary search for x -> x^x over [1,10]
def inv_npn(y):
    l = 1.; r =10.
    while r-l>1e-7:
        x = (r+l)/2
        if x**x>y: r = x
        else:      l = x
    return (r+l)/2.

y = float(input())
print(inv_nlogn(log(y)))
#print(inv_npn(y))
