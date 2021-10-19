#!/usr/bin/env python3

while True:
    N = int(input())
    if N==0:
        break
    if N==1:
        print('{ }')
        continue
    N -= 1
    S = []
    p = 1
    while N:
        if N&1:
            S.append(p)
        N >>= 1
        p *= 3
    print('{', ', '.join(map(str,S)), '}')
