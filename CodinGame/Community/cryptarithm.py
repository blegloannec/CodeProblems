#!/usr/bin/env python3

import itertools

def solve(W,T):
    L = set()
    for w in W+[T]:
        for c in w:
            L.add(c)
    L = list(L)
    for X in itertools.combinations(range(10),len(L)):
        for Y in itertools.permutations(X):
            D = {L[i]:Y[i] for i in range(len(L))}
            S = 0
            for w in W:
                s = 0
                for c in w:
                    s = 10*s+D[c]
                S += s
            ST = 0
            for c in T:
                ST = 10*ST+D[c]
            # "the initial letter of a word can never be assigned to 0"
            if S==ST and all(D[w[0]]!=0 for w in W+[T]):
                return D

def main():
    N = int(input())
    W = []
    for _ in range(N):
        W.append(input())
    T = input()
    D = solve(W,T)
    for c in sorted(D):
        print(c,D[c])

main()
