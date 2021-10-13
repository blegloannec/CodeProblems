#!/usr/bin/env python3

import sys
input = sys.stdin.readline

def main():
    N,M = map(int, input().split())
    T = [-1]*N
    for i in range(1, M+1):
        a,b = map(int, input().split())
        if a>b:
            a,b = b,a
        # /!\ both conditions can be true for N=2
        if a+1==b:
            T[a-1] = i
        if a==1 and b==N:
            T[-1] = i
    sys.stdout.write('impossible' if -1 in T else '\n'.join(map(str, T)))
    sys.stdout.write('\n')

main()
