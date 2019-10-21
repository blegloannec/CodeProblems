#!/usr/bin/env python3

import sys

def cost(N, M, A, B):
    res = (N-M)*A
    N //= 2
    bcost = B
    while N>=M:
        res = min(res, bcost + (N-M)*A)
        N //= 2
        bcost += B
    return res

def main():
    T = int(sys.stdin.readline())
    for t in range(1,T+1):
        N,M,L = map(int,sys.stdin.readline().split())
        Agencies = []
        for _ in range(L):
            Name,AB = sys.stdin.readline().split(':')
            A,B = tuple(map(int,AB.split(',')))
            Agencies.append((cost(N,M,A,B),Name))
        Agencies.sort()
        sys.stdout.write('Case %d\n' % t)
        for c,name in Agencies:
            sys.stdout.write('%s %d\n' % (name,c))

main()
