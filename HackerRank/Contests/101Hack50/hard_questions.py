#!/usr/bin/env python3

n = int(input())
V = input()
C = input()
s = 0
for i in range(n):
    s += int(V[i]!='.' and V[i]!=C[i])
print(s)
