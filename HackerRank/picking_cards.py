#!/usr/bin/env python3

from collections import Counter

P = 10**9+7

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        C = Counter(map(int,input().split()))
        avail = 0
        res = 1
        for i in range(N):
            avail += C[i]
            res = (res*avail)%P
            avail -= 1
        print(res)

main()
