#!/usr/bin/env python3

from collections import defaultdict

def count(a,b,c,d):
    X = defaultdict(int)
    for x in range(1,c+1):
        X[x*x-a*x] += 1
    Y = defaultdict(int)
    for y in range(1,d+1):
        Y[b*y-y*y] += 1
    cpt = 0
    for x in X:
        cpt += X[x]*Y[x]
    return cpt

def main():
    q = int(input())
    for _ in range(q):
        a,b,c,d = map(int,input().split())
        print(count(a,b,c,d))

main()
