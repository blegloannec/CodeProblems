#!/usr/bin/env python3

M = int(input())
N = int(input())
W = sorted(map(int,input().split()), reverse=True)

i = l = w = 0
while i<N:
    i0,i = i,min(i+M,N)
    w += l*sum(W[i0:i])
    l += 1
w *= 0.65
print('%.03f' % w)
