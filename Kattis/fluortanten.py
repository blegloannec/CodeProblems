#!/usr/bin/env python3

import sys
input = sys.stdin.readline

def main():
    N = int(input())
    A = [int(a) for a  in input().split() if a!='0']
    S = s = sum((i+1)*a for i,a in enumerate(A))
    for a in reversed(A):
        s += a
        S = max(S, s)
    print(S)

main()
