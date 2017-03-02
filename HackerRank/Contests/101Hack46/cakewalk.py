#!/usr/bin/env python3

n = int(input())
C = sorted(map(int,input().split()),reverse=True)
print(sum(C[i]*(1<<i) for i in range(n)))
