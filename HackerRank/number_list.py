#!/usr/bin/env python3

def main():
    T = int(input())
    for _ in range(T):
        N,K = map(int,input().split())
        A = list(map(int,input().split()))
        res = N*(N+1)//2
        j = -1
        for i in range(N):
            if A[i]>K:
                j = i
            else:
                res -= i-j
        print(res)

main()
