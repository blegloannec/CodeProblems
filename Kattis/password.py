#!/usr/bin/env python3

N = int(input())
P = sorted((float(input().split()[1]) for _ in range(N)), reverse=True)
E = sum((i+1)*P[i] for i in range(N))
print(E)
