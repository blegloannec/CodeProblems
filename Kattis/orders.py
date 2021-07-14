#!/usr/bin/env python3

import sys
input = sys.stdin.readline

def main():
    N = int(input())
    C = list(map(int, input().split()))
    M = int(input())
    S = list(map(int, input().split()))
    SMAX = max(S)

    # classic Subset-Sum DP
    # DP[n][s] = #ways to reach s using C[:n]
    DP = [[0]*(SMAX+1)]
    DP[0][0] = 1
    for n in range(1, N+1):
        c = C[n-1]
        DP.append(DP[n-1].copy())
        for s in range(c, SMAX+1):   # incr. s and ref. to n (not DP[n-1][s-c])
            DP[n][s] += DP[n][s-c]   # as items can be used more than once

    # output
    for s in S:
        if DP[N][s]==0:
            sys.stdout.write('Impossible')
        elif DP[N][s]>1:
            sys.stdout.write('Ambiguous')
        else:
            # building solution backwards
            Sol = []
            n = N
            while n>0:
                if DP[n-1][s]==1:
                    n -= 1
                else:
                    s -= C[n-1]
                    Sol.append(n)
            Sol.reverse()
            sys.stdout.write(' '.join(map(str, Sol)))
        sys.stdout.write('\n')

main()
