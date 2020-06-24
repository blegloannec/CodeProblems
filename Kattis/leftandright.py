#!/usr/bin/env python3

import sys
input = sys.stdin.readline

def main():
    N = int(input())-1
    S = input()
    P = [1]
    i = 0
    while i<N:
        if S[i]=='R':
            i += 1
            P.append(i+1)
        else:
            while i<N and S[i]=='L':
                i += 1
            P.extend(range(i+1, P.pop()-1, -1))
    for p in P:
        sys.stdout.write(f'{p}\n')

main()
