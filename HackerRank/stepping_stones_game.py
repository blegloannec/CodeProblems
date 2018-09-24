#!/usr/bin/env python3

from math import sqrt

# t = n(n+1)/2
# n^2 + n - 2t = 0
# Given t, D = 1+8t must be a square
# then n = (-1+sqrt(D))/2
def is_triang(t):
    D = 1+8*t
    d = int(sqrt(1+8*t))
    return (-1+d)//2 if d*d==D else -1

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        n = is_triang(N)
        print('Go On Bob %d'%n if n>=0 else 'Better Luck Next Time')

main()
