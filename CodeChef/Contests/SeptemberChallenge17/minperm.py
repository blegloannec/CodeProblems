#!/usr/bin/env python3

T = int(input())
for _ in range(T):
    n = int(input())
    P = []
    if n%2==0:
        for i in range(1,n+1,2):
            P += [i+1,i]
    else:
        for i in range(1,n-3,2):
            P += [i+1,i]
        P += [n-1,n,n-2]
    print(' '.join(map(str,P)))
