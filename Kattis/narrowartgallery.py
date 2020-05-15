#!/usr/bin/env python3

import sys

def main():
    while True:
        N,K = map(int,sys.stdin.readline().split())
        if N==0:
            break
        V = [tuple(map(int,sys.stdin.readline().split())) for _ in range(N)]
        DP00 = [float('-inf')]*(K+1)
        DP00[0] = 0
        DP10 = [float('-inf')]*(K+1)
        DP01 = [float('-inf')]*(K+1)
        for n in range(N):
            for k in range(min(K,n+1),-1,-1):
                DP00[k] = sum(V[n]) + max(DP00[k],DP10[k],DP01[k])
                if k>0:
                    DP10[k] = V[n][1] + max(DP00[k-1],DP10[k-1])
                    DP01[k] = V[n][0] + max(DP00[k-1],DP01[k-1])
        res = max(DP00[K],DP10[K],DP01[K])
        sys.stdout.write(f'{res}\n')

main()
