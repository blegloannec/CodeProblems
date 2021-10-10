#!/usr/bin/env python3

from math import gcd

def lcm(a,b):
    return a*b//gcd(a,b)

def main():
    N = int(input())
    res = 1<<30
    for _ in range(N):
        y,c,d = map(int, input().split())
        res = min(res, y+lcm(c,d))
    print(res)

main()
