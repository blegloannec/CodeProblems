#!/usr/bin/env python3

import sys

def main():
    P,D = map(int, sys.stdin.readline().split())
    A = [0]*D
    B = [0]*D
    for _ in range(P):
        d,a,b = map(int, sys.stdin.readline().split())
        d -= 1
        A[d] += a
        B[d] += b
    V = WA = WB = 0
    for d in range(D):
        vot = A[d]+B[d]
        maj = vot//2+1
        if A[d]>B[d]:
            win = 'A'
            wa = A[d]-maj
            wb = B[d]
        else:
            win = 'B'
            wa = A[d]
            wb = B[d]-maj
        sys.stdout.write(f'{win} {wa} {wb}\n')
        V += vot
        WA += wa
        WB += wb
    E = abs(WA-WB)/V
    sys.stdout.write(f'{E}\n')

main()
