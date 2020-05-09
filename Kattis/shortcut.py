#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# DS(b,d)  <=>  ∀n, bⁿ ≡ 1 [d]  <=>  b ≡ 1 [d]
# the largest d ≤ k such that d | b-1

import sys

def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        B,K = map(int,sys.stdin.readline().split())
        B -= 1
        D = d = 1
        while d<=K and d*d<=B:
            if B%d==0:
                if B//d<=K:
                    D = B//d
                    break
                else:
                    D = d
            d += 1
        sys.stdout.write(f'{D}\n')

main()
