#!/usr/bin/env python3

from math import *

bounce = lambda a: atan(2.*tan(a))

def main():
    K,W,L = map(int, input().split())
    bl, br = 0., pi/2.
    while br-bl>1e-9:
        a = b = (bl+br)/2.
        l = (W/2.)*tan(a)
        a = bounce(a)
        for _ in range(K-1):
            l += W*tan(a)
            a = bounce(a)
        l += (W/2.)*tan(a)
        if l<L: bl = b
        else:   br = b
    print(degrees(b))

main()
