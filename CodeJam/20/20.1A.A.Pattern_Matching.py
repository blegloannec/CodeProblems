#!/usr/bin/env python3

NONE = '*'

def match_pattern(P):
    N = len(P)
    # checking prefixes compatibility
    pref_max_idx = max(range(N), key=(lambda i: len(P[i][0])))
    for i in range(N):
        for a,b in zip(P[i][0], P[pref_max_idx][0]):
            if a!=b:
                return NONE
    # checking suffixes compatibility
    suff_max_idx = max(range(N), key=(lambda i: len(P[i][-1])))
    for i in range(N):
        for a,b in zip(reversed(P[i][-1]), reversed(P[suff_max_idx][-1])):
            if a!=b:
                return NONE
    # for the middle part, the input/output constraints
    # (N * max length <= 5000 <= 10^4)
    # allow to simply concatenate them
    mid = ''.join(''.join(p[1:-1]) for p in P)
    res = P[pref_max_idx][0] + mid + P[suff_max_idx][-1]
    return res

def main():
    T = int(input())
    for t in range(1,T+1):
        N = int(input())
        P = [input().split('*') for _ in range(N)]
        res = match_pattern(P)
        print('Case #{}: {}'.format(t,res))

main()
