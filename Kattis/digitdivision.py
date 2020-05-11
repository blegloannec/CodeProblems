#!/usr/bin/env python3

# key insight:
# consider the number N = "AB" = A*10^|B| + B
# and assume the prefix A is divisible by M
# then N is divisible by M iff B is divisible by M

import sys

def main():
    N,M = map(int, sys.stdin.readline().split())
    S = sys.stdin.readline()
    sep = r = 0
    for i in range(N):
        d = ord(S[i])-ord('0')
        r = (10*r + d) % M
        if r==0:
            sep += 1
    res = pow(2, sep-1, 10**9+7) if r==0 else 0
    sys.stdout.write(f'{res}\n')

main()
