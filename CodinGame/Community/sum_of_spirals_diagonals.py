#!/usr/bin/env python3

def D(n, d=1):
    if n==0: return 0
    if n==1: return d
    return d + d+n-1 + d+2*n-2 + d+3*n-3 + D(n-2, d+4*n-4)

print(D(int(input())))
