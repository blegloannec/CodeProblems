#!/usr/bin/env python3

T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    print(2 if M==1 or N%2==0 else 1)
