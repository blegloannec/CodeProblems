#!/usr/bin/env python3

H,W = map(int, input().split())
C = [0] + [H]*W + [0]

T = int(input())
for c in map(int, input().split()):
    C[c] -= 1
    peri = 0
    for i in range(1, W+2):
        peri += abs(C[i]-C[i-1])
        if C[i]>0:
            peri += 2
    print(peri)
