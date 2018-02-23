#!/usr/bin/env python3

from collections import defaultdict

def solve(m,C,D):
    for i in range(len(C)):
        for j in D[m-C[i]]:
            if j!=i:
                return (i+1,j+1)
    assert(False)

def main():
    t = int(input())
    for _ in range(t):
        m = int(input())
        n = int(input())
        C = list(map(int,input().split()))
        D = defaultdict(list)
        for i in range(n):
            D[C[i]].append(i)
        print(*solve(m,C,D))

main()
