#!/usr/bin/env python3

N = int(input())
F = []; B = []
start = None
for n in range(N):
    L = input()
    nb = True
    if 'Fizz' in L:
        F.append(n)
        nb = False
    if 'Buzz' in L:
        B.append(n)
        nb = False
    if nb and start is None:
        start = int(L) - n

f = F[1]-F[0] if len(F)>1 else start+F[0]
b = B[1]-B[0] if len(B)>1 else start+B[0]
print(f, b)
