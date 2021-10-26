#!/usr/bin/env python3

import sys
input = sys.stdin.readline

def main():
    N = int(input())
    I = [tuple(map(int, input().split())) for _ in range(N)]
    I.sort(key=(lambda lr: lr[1]))
    Out = []
    for l,r in I:
        if len(Out)==0 or Out[-1][1]<=l:
            Out.append((l,r))
    print(len(Out))

main()
