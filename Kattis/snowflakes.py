#!/usr/bin/env python3

import sys

def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        l = res = 0
        last_seen = {}
        for i in range(N):
            s = int(sys.stdin.readline())
            if s in last_seen:
                l = max(l, last_seen[s]+1)
            res = max(res, i-l+1)
            last_seen[s] = i
        sys.stdout.write(f'{res}\n')

main()
