#!/usr/bin/env python3

def main():
    T = int(input())
    for _ in range(T):
        t,N,m,k = map(int, input().split())
        V = [i for i in range(1,N+1) if i%k!=m]
        DP = [0]*(N+1)
        DP[0] = 1
        for n in range(N):
            for v in V:
                if n+v<=N:
                    DP[n+v] += DP[n]
                else:
                    break
        print(t, DP[N])

main()
