#!/usr/bin/env python3

from math import sqrt, ceil

f = lambda x: 10.*sqrt(x)

def main():
    x,y0,y1 = map(int, input().split())
    k = 0
    k0 = None
    while ceil(x)<=y1:
        if k0 is None and y0<=ceil(x):
            k0 = k
            if y1==100:
                break
        x = f(x)
        k += 1
    k = 'inf' if y1==100 else k-1
    print('impossible' if k0 is None else f'{k0} {k}')

main()
