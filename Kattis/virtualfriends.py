#!/usr/bin/env python3

import sys

def find(Repr, x):
    if Repr[x] is None:
        return x
    Repr[x] = find(Repr, Repr[x])
    return Repr[x]

def union(Repr, Size, x, y):
    x0 = find(Repr, x)
    y0 = find(Repr, y)
    if x0!=y0:
        Repr[y0] = x0
        Size[x0] += Size[y0]
    return Size[x0]

def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        Num  = {}
        Repr = []
        Size = []
        for _ in range(N):
            A,B = sys.stdin.readline().split()
            for X in (A,B):
                if X not in Num:
                    Num[X] = len(Repr)
                    Repr.append(None)
                    Size.append(1)
            sys.stdout.write('%d\n' % union(Repr, Size, Num[A], Num[B]))

main()
