#!/usr/bin/env python3

def mex(S):
    x = 0
    while x in S:
        x += 1
    return x

memo = {0: 0}
def grundy(n):
    if n not in memo:
        S = set()
        for i in range(n):
            S.add(grundy(i)^grundy(n-1-i))
            if i<n-1:
                S.add(grundy(i)^grundy(n-2-i))
        memo[n] = mex(S)
    return memo[n]

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        C = input().split('X')
        g = 0
        for B in C:
            g ^= grundy(len(B))
        print('LOSE' if g==0 else 'WIN')
