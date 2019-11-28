#!/usr/bin/env python2

# terrible brute-force... recycled from CG/cryptarithm.py

import itertools

def solve_count(W):
    L = set()
    for w in W:
        L |= set(w)
    L = list(L)
    W = [[L.index(c) for c in w] for w in W]
    T = W.pop()
    cnt = 0
    for X in itertools.combinations(range(10),len(L)):
        for Y in itertools.permutations(X):
            if Y[T[0]]!=0:
                S = 0
                for w in W:
                    s = 0
                    for c in w:
                        s = 10*s+Y[c]
                    S += s
                ST = 0
                for c in T:
                    ST = 10*ST+Y[c]
                if S==ST and all(Y[w[0]]!=0 for w in W):
                    cnt += 1
    return cnt

def main():
    N = int(raw_input())
    W = [raw_input() for _ in range(N)]
    print(solve_count(W))

main()
