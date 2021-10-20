#!/usr/bin/env python3

from collections import defaultdict
import sys
input = sys.stdin.readline

def main():
    N = int(input())
    D = defaultdict(list)
    for _ in range(N):
        s,y = input().split()
        D[s].append(int(y))
    for s in D:
        D[s].sort()
    Q = int(input())
    for _ in range(Q):
        s,k = input().split()
        k = int(k)-1
        sys.stdout.write(f'{D[s][k]}\n')

main()
