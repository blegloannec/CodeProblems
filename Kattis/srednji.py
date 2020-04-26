#!/usr/bin/env python3

import sys

def main():
    N,B = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    bi = A.index(B)
    Suff = {0: 1}
    d = 0
    for i in range(bi+1, N):
        d += 1 if A[i]>B else -1
        Suff[d] = Suff.get(d, 0) + 1
    res = Suff[0]
    d = 0
    for i in range(bi-1, -1, -1):
        d += 1 if A[i]>B else -1
        res += Suff.get(-d, 0)
    print(res)

main()
