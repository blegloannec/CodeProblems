#!/usr/bin/env python3

N = int(input())
C = sorted(input().split(),reverse=True)
minus = C[-1]=='-'
if minus: C.pop()
dot = '.' if C[-1]=='.' else ''
if dot: C.pop()

res = '-'+C[-1]+dot+''.join(reversed(C[:-1])) if minus else ''.join(C[:-1])+dot+C[-1]

if dot and res[-1]=='0':
    res = '0' if minus else res[:-2]
print(res)
