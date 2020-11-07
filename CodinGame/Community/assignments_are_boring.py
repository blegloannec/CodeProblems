#!/usr/bin/env python3

Z = int(input())
N = int(input())
MOD = 1<<int(input())

Cnt = [0]*MOD
for _ in range(N):
    Z = (1664525*Z + 1013904223) % MOD
    Cnt[Z] += 1

rem = 0
Out = []
for cnt in reversed(Cnt):
    if cnt:
        Out.append(rem)
        rem += cnt
print(*reversed(Out))
