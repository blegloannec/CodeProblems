#!/usr/bin/env python3

import sys
input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        D,N = map(int, input().split())
        A = [int(x)%D for x in input().split()]
        Cnt = [0]*D
        Cnt[0] = 1
        res = s = 0
        for a in A:
            s = (s+a) % D
            res += Cnt[s]
            Cnt[s] += 1
        print(res)

main()
