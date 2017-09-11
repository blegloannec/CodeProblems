#!/usr/bin/env python3

from collections import Counter

T = int(input())
for _ in range(T):
    N = Counter(int(c) for c in input())
    A = []
    for x in range(65,91):
        a,b = x%10,x//10
        if a==b:
            if N[a]>=2:
                A.append(chr(x))
        else:
            if N[a]>=1 and N[b]>=1:
                A.append(chr(x))
    print(''.join(A))
