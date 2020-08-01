#!/usr/bin/env python3

import sys
input = sys.stdin.readline

# iterative tree infix traversal
def join(W, T, a0):
    S = [a0]
    while S:
        a = S.pop()
        sys.stdout.write(W[a])
        S.extend(reversed(T[a]))

def main():
    N = int(input())
    S = [input().strip() for _ in range(N)]
    T = [[] for _ in range(N)]
    a = 0  # /!\ for N = 1
    for _ in range(N-1):
        a,b = map(int, input().split())
        a -= 1
        b -= 1
        T[a].append(b)
    join(S, T, a)
    sys.stdout.write('\n')

main()
