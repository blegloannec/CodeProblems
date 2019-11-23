#!/usr/bin/env python3

N = int(input())
V = list(map(int,input().split()))
try:
    l = next(i for i in range(N-1) if V[i]>V[i+1])
    while l>0 and V[l-1]==V[l]:
        l -= 1
    r = next(i for i in range(N-1,0,-1) if V[i-1]>V[i])
    while r<N-1 and V[r]==V[r+1]:
        r += 1
    V = V[:l]+V[l:r+1][::-1]+V[r+1:]
except StopIteration:
    l = r = 0
if all(V[i]<=V[i+1] for i in range(N-1)):
    print(l+1,r+1)
else:
    print('impossible')
