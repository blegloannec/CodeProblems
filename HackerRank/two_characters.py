#!/usr/bin/env python3

# L = length of the string, A = size of the alphabet 
# the naive solution is O(A^2*L) (trying every pair, e.g. editorial)
# the following approach is O(A*L)
# it's unclear whether something better is possible...

from collections import *

L = int(input())
S = input()
res = 0
if L>1:
    C = Counter(S)
    for a in C:
        i0 = -1
        D = defaultdict(int)
        B = set(C.keys())
        for i in range(L+1):
            if i==L or S[i]==a:
                if 0<=i0 and i<L:
                    B &= {b for b in D if D[b]==1}
                else:
                    B -= {b for b in D if D[b]>1}
                i0 = i
                D.clear()
            else:
                D[S[i]] += 1
        if B:
            res = max(res, C[a]+max(C[b] for b in B))
print(res)
