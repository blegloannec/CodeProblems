#!/usr/bin/env python3

from math import log10

def main():
    T = int(input())
    for n in range(T):
        N = int(input())
        for i in range(N+1):
            l = log10(2)*i + log10(11)*(N-i)
            if N-1 <= l < N:
                S = [2]*i + [11]*(N-i)
                print(*S)
                break

main()
