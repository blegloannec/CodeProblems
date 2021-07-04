#!/usr/bin/env python3

import sys

# successive simplifications
def sylvester0(x,y, k=63):
    if k<0:                   return 1
    if (x>>k)&1 and (y>>k)&1: return -sylvester0(x,y, k-1)
    else:                     return  sylvester0(x,y, k-1)

def sylvester1(x,y):
    res = 1
    for k in range(max(x,y).bit_length()-1, -1, -1):
        if (x>>k)&1 and (y>>k)&1:
            res = -res
    return res

def sylvester(x,y):
    # (-1)^(#1s in bin(x&y))
    res = 1
    z = x&y
    while z:
        z &= z-1
        res = -res
    return res

def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        _,x0,y0,w,h = map(int, sys.stdin.readline().split())
        for y in range(y0, y0+h):
            L = [sylvester(x,y) for x in range(x0, x0+w)]
            sys.stdout.write(' '.join(map(str, L)))
            sys.stdout.write('\n')
        sys.stdout.write('\n')

main()
