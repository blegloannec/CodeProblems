#!/usr/bin/env python3

import sys
input = sys.stdin.readline

def case():
    C,N = map(int, input().split())
    V = [0]*N
    W = [0]*N
    for i in range(N):
        V[i],W[i] = map(int, input().split())

    # classic Knapsack DP
    # DP[n][w] = max value of weight w using items 0..n-1
    DP = [[0]*(C+1)]
    for n in range(1, N+1):
        DP.append(DP[n-1].copy())
        for w in range(W[n-1], C+1):
            DP[n][w] = max(DP[n][w], DP[n-1][w-W[n-1]]+V[n-1]) # ref. to n-1 as items used at most once

    # building solution backwards
    w = max(range(C+1), key=(lambda w: DP[N][w]))
    Sol = []
    for n in range(N, 0, -1):
        if DP[n-1][w]!=DP[n][w]:
            Sol.append(n-1)
            w -= W[n-1]
    sys.stdout.write(f'{len(Sol)}\n{" ".join(map(str, Sol))}\n')

def main():
    while True:
        try:
            case()
        except ValueError:
            break

main()
