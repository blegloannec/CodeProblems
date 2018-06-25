#!/usr/bin/env python3

from collections import Counter

n,k = map(int,input().split())
A = list(map(int,input().split()))
A0 = Counter(A[i]-i*k for i in range(n))
res = n - max(A0[a0] for a0 in A0)
print(res)
