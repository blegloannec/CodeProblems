#!/usr/bin/env python3

import sys
input = sys.stdin.readline

MOD = 10**9+7

def main():
    N = int(input())
    H = input()[::2]
    C1 = C2 = C3 = 0
    for h in H:
        if   h=='1': C1 += 1
        elif h=='2': C2 = (C1 + 2*C2) % MOD
        else:        C3 = (C3 + C2) % MOD
    print(C3)

main()
