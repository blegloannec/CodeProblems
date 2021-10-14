#!/usr/bin/env python3

import sys
input = sys.stdin.readline
from collections import Counter

def main():
    N,M = map(int, input().split())
    C = Counter(tuple(map(int, input().split())) for _ in range(M))
    L = int(input())
    W = list(map(int, input().split()))
    for i in range(L):
        if C[W[i],W[i+1]]>0:
            C[W[i],W[i+1]] -= 1
        else:
            print(i+1)
            return
    print('correct' if L==M else 'too short')

main()
