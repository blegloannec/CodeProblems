#!/usr/bin/env python3

A = sorted(map(int,input()[1:-1].split(',')))
S = []
i = 0
while i<len(A):
    i0 = i
    i += 1
    while i<len(A) and A[i]==A[i-1]+1:
        i += 1
    if i-i0<=2:
        S.append('%d' % A[i0])
        if i-i0==2:
            S.append('%d' % A[i0+1])
    else:
        S.append('%d-%d' % (A[i0],A[i-1]))
print(','.join(S))
