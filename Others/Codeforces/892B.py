#!/usr/bin/env python3

n = int(input())
L = list(map(int,input().split()))
cpt = 0
a = n-1
for i in range(n-1,-1,-1):
    if a>=i:
        cpt += 1
    a = min(a,i-L[i]-1)
print(cpt)
