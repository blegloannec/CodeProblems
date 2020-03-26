#!/usr/bin/env python3

import sys

def sieve(N=32001):
    P = [True]*N
    L = []
    for i in range(2,N):
        if P[i]:
            L.append(i)
            for k in range(i*i,N,i):
                P[k] = False
    return P,L

def main():
    P,L = sieve()
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        R = []
        for p in L:
            if 2*p<=n:
                if P[n-p]:
                    R.append(p)
            else:
                break
        sys.stdout.write(f'{n} has {len(R)} representation(s)\n')
        for p in R:
            sys.stdout.write(f'{p}+{n-p}\n')
        sys.stdout.write('\n')

main()
