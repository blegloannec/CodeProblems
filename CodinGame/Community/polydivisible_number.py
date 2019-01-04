#!/usr/bin/env python3

D = list(map(int,input().split()))
for B in range(max(D)+1,37):
    n = 0
    for d in D:
        n = B*n+d
    n = str(n)
    if all(int(n[:i])%i==0 for i in range(2,len(n)+1)):
        print(B)
