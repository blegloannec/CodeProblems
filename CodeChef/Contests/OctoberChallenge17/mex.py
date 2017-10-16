#!/usr/bin/env python3

M = 2*10**5+1

def main():
    T = int(input())
    for _ in range(T):
        N,K = map(int,input().split())
        S = list(map(int,input().split()))
        B = [False]*M
        for s in S:
            B[s] = True
        i = 0
        while i<M and K>=0:
            if not B[i]:
                K -= 1
            i += 1
        print(i+K)

main()
