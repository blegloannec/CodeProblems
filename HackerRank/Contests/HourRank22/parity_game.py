#!/usr/bin/env python3

n = int(input())
A = list(map(int,input().split()))
S = sum(A)
if S%2==0:
    print(0)
else:
    if n>1 and any(a%2==1 for a in A):
        print(1)
    else:
        print(-1)
