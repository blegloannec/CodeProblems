#!/usr/bin/env python3

from collections import deque
import sys
input = sys.stdin.readline

def case():
    P = input().strip()
    N = int(input())
    X = input().strip()[1:-1]
    X = deque(X.split(',')) if X else []
    rev = False
    for c in P:
        if c=='R':
            rev = not rev
        else:
            if not X:
                return 'error'
            if rev:
                X.pop()
            else:
                X.popleft()
    return f'[{",".join(reversed(X))}]' if rev else f'[{",".join(X)}]'

def main():
    T = int(input())
    for _ in range(T):
        sys.stdout.write(case())
        sys.stdout.write('\n')

main()
