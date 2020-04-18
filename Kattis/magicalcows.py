#!/usr/bin/env python3

def main():
    C,N,M = map(int,input().split())
    Cnt = [[0]*(C+1)]
    for _ in range(N):
        c = int(input())
        Cnt[0][c] += 1
    D = [int(input()) for _ in range(M)]
    for d in range(1,max(D)+1):
        Cnt.append([0]*(C+1))
        for i in range(1,C+1):
            if 2*i<=C:
                Cnt[d][2*i] += Cnt[d-1][i]
            else:
                Cnt[d][i] += 2*Cnt[d-1][i]
    for d in D:
        print(sum(Cnt[d]))

main()
