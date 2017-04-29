#!/usr/bin/env python3

N = int(input())
C = int(input())
B = []
S = 0
for _ in range(N):
    B.append(int(input()))
    S += B[-1]
B.sort()

if C>S:                  # pas assez de budget
    print('IMPOSSIBLE')
else:
    M = C//N             # moyenne
    for i in range(N-1):
        P = min(B[i],M)  # ce que i paye
        print(P)
        C -= P           # cout restant m-a-j
        M = C//(N-i-1)   # moyenne m-a-j
    print(C)             # le dernier paye ce qui reste
