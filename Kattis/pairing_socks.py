#!/usr/bin/env python3

import sys

def main():
    N = int(sys.stdin.readline())
    A = list(map(int,reversed(sys.stdin.readline().split())))
    B = []
    while A and len(A)>=len(B):
        if B and A[-1]==B[-1]:
            A.pop()
            B.pop()
        else:
            B.append(A.pop())
    print('impossible' if B else 2*N)

main()
