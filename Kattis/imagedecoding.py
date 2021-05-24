#!/usr/bin/env python3

import sys
input = sys.stdin.readline

A = '.#'

def main():
    first = True
    while True:
        N = int(input())
        if N==0:
            break
        if first:
            first = False
        else:
            sys.stdout.write('\n')
        W = None
        error = False
        for _ in range(N):
            L = input().split()
            c = A.index(L[0])
            L = list(map(int, L[1:]))
            O = []
            w = 0
            for l in L:
                O.append(A[c]*l)
                w += l
                c ^= 1
            if W is None:
                W = w
            elif w!=W:
                error = True
            O.append('\n')
            sys.stdout.write(''.join(O))
        if error:
            sys.stdout.write('Error decoding image\n')

main()
