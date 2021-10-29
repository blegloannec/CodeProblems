#!/usr/bin/env python3

import sys
input = sys.stdin.readline

def main():
    N = int(input())
    I = [tuple(map(int, input().split())) for _ in range(N)]
    I.sort(key=(lambda lr: lr[1]))
    res = t = 0
    for l,u in I:
        if t<l:
            res += 1
            t = u
    print(res)

main()
