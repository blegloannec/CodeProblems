#!/usr/bin/env python3

from collections import defaultdict

# Cocke-Younger-Kasami (CYK) https://en.wikipedia.org/wiki/CYK_algorithm
# Standard implementation, single-word index-based O(|W|^3) DP
def CYK(i,j):
    if memo[i][j] is None:
        memo[i][j] = set()
        if i==j:
            memo[i][j] |= InvRules[W[i]]
        else:
            for k in range(i,j):
                for A in CYK(i,k):
                    for B in CYK(k+1,j):
                        memo[i][j] |= InvRules[A+B]
    return memo[i][j]


'''
# Alternative implementation, hashing words for memoization to be 
# reused/shared between inputs (slightly slower on most testcases
# but slightly faster on the largest/last one)
memo = {}
def CYK(W):
    if W not in memo:
        Res = set()
        if len(W)==1:
            Res |= InvRules[W]
        else:
            for k in range(1,len(W)):
                for A in CYK(W[:k]):
                    for B in CYK(W[k:]):
                        Res |= InvRules[A+B]
        memo[W] = Res
    return memo[W]
'''


if __name__=='__main__':
    N = int(input())
    START = input()
    # https://en.wikipedia.org/wiki/Chomsky_normal_form
    # CNF without epsilon rules
    Rules = [tuple(input().split(' -> ')) for _ in range(N)]
    InvRules = defaultdict(set)
    for L,R in Rules:
        InvRules[R].add(L)
    T = int(input())
    for _ in range(T):
        W = input()
        L = len(W)
        memo = [[None]*L for _ in range(L)]
        print(str(START in CYK(0,L-1)).lower())
