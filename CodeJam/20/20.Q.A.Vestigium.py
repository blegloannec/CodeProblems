#!/usr/bin/env python3

def main():
    T = int(input())
    for t in range(1,T+1):
        N = int(input())
        M = [list(map(int,input().split())) for _ in range(N)]
        k = sum(M[i][i] for i in range(N))
        r = sum(int(len(set(L[j] for j in range(N)))<N) for L in M)
        c = sum(int(len(set(M[i][j] for i in range(N)))<N) for j in range(N))
        print('Case #{}: {} {} {}'.format(t,k,r,c))

main()
