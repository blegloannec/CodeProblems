#!/usr/bin/env python3

from math import pi, tan

def main():
    N = int(input())
    for _ in range(N):
        n,l,d,g = map(int,input().split())
        r = d*g
        print(n*l*l/(4.*tan(pi/n)) + n*l*r + pi*r*r)

main()
