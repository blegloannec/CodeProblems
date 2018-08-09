#!/usr/bin/env python3

from fractions import gcd
from functools import reduce

def lcm(a,b):
    return a*b//gcd(a,b)

def nb_div(x):
    d = 1
    res = 0
    while d*d<=x:
        if x%d==0:
            res += 1 if d*d==x else 2
        d += 1
    return res

def main():
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    # x is "between" A and B  iff  lcm(A) | x | gcd(B)
    # hence lcm(A) | gcd(B) and x = d*lcm(A) for any d | gcd(B)/lcm(A)
    L = reduce(lcm,A)
    R = reduce(gcd,B)
    res = nb_div(R//L) if R%L==0 else 0
    print(res)

main()
