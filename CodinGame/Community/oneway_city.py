#!/usr/bin/env python3

m = int(input())
n = int(input())

def binom(n,p):
    res = 1
    for i in range(p-1,-1,-1):
        res = (n-i)*res//(p-i)
    return res

print(str(binom(m+n-2,n-1))[:1000])
