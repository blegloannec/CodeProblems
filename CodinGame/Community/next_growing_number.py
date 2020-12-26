#!/usr/bin/env python3

N = str(int(input())+1)
for i in range(1, len(N)):
    if N[i] < N[i-1]:
        N = N[:i] + N[i-1]*(len(N)-i)
        break
print(N)
