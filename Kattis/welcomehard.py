#!/usr/bin/env python3

# also passes the welcomeeasy problem

import sys
input = sys.stdin.readline

WCJ = 'welcome to code jam'
MOD = 10000

def main():
    T = int(input())
    for t in range(1, T+1):
        S = input().strip()
        C = [0]*(len(WCJ)+1)
        C[0] = 1
        for c in S:
            for i in range(len(WCJ)-1, -1, -1):
                if c==WCJ[i]:
                    C[i+1] += C[i]
                    C[i+1] %= MOD
        print(f'Case #{t}: {C[-1]:04d}')

main()
