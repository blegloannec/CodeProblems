#!/usr/bin/env python3

T = int(input())
for _ in range(T):
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    M = N-A.count(1)
    print('YES' if M<=K else 'NO')
