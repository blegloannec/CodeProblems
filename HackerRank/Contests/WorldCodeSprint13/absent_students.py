#!/usr/bin/env python3

n = int(input())
R = set(map(int,input().split()))
A = sorted(set(range(1,n+1))-R)
print(*A)
