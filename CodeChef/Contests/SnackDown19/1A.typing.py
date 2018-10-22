#!/usr/bin/env python3

def cost(W):
    W = W.replace('f','d').replace('k','j')
    return 2 + sum(2+2*int(W[i-1]==W[i]) for i in range(1,len(W)))

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        memo = {}
        res = 0
        for _ in range(N):
            W = input()
            if W in memo:
                res += memo[W]//2
            else:
                memo[W] = cost(W)
                res += memo[W]
        print(res)

main()
