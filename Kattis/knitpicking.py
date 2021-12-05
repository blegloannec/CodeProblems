#!/usr/bin/env python3

import sys
input = sys.stdin.readline

def main():
    N = int(input())
    socks = {}
    total = 0
    for _ in range(N):
        typ, fit, cnt = input().split()
        cnt = int(cnt)
        total += cnt
        if fit=='any':
            cnt = 1
        if typ not in socks or cnt>socks[typ]:
            socks[typ] = cnt
    res = sum(socks.values())
    print('impossible' if res==total else res+1)

main()
