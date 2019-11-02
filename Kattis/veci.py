#!/usr/bin/env python3

N = list(input())
try:
    i = next(i for i in range(len(N)-1,0,-1) if N[i-1]<N[i])
    j = min(range(i,len(N)), key=(lambda j: N[j] if N[j]>N[i-1] else 'a'))
    N[i-1],N[j] = N[j],N[i-1]
    N = N[:i] + sorted(N[i:])
    print(''.join(N))
except StopIteration:
    print(0)
