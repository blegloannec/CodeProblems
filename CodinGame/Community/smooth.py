#!/usr/bin/env python3

def win(n):
    for d in (2,3,5):
        while n%d==0:
            n //= d
    return n==1

N = int(input())
for _ in range(N):
    F = int(input())
    print(('DEFEAT','VICTORY')[win(F)])
