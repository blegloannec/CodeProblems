#!/usr/bin/env python3

import sys
input = sys.stdin.readline

def ask(A):
    sys.stdout.write(f'ASK {len(A)} {" ".join(map(str, A))}\n')
    sys.stdout.flush()
    return list(map(int, input().split()))

def main():
    N = int(input())
    K = N.bit_length()
    B = [0]*(N+1)
    for k in range(K):
        A = [n for n in range(1, N+1) if (n>>k)&1]
        for b in ask(A):
            B[b] |= 1<<k
    sys.stdout.write(f'ANSWER {" ".join(map(str, B[1:]))}\n')
    sys.stdout.flush()

main()
