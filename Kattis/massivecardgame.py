#!/usr/bin/env python3

import sys
from bisect import *
input = sys.stdin.readline

def main():
    N = int(input())
    C = sorted(map(int, input().split()))
    Q = int(input())
    for _ in range(Q):
        l,r = map(int, input().split())
        i = bisect_left(C, l)
        j = bisect_right(C, r)
        sys.stdout.write(f'{j-i}\n')

main()
