#!/usr/bin/env python3

# recursive+memoized simpler (expected) implementation
# (~ kinda-DP in the DAG)

from functools import lru_cache
from operator import add, sub, mul
Op = {'ADD': add, 'SUB': sub, 'MULT': mul, 'VALUE': (lambda x,_: x)}

def val(X):
    return None if X=='_' else cell(int(X[1:])) if X[0]=='$' else int(X)

@lru_cache(maxsize=None)
def cell(i):
    return Op[O[i]](val(A[i]),val(B[i]))

N = int(input())
O,A,B = zip(*(input().split() for _ in range(N)))
for i in range(N):
    print(cell(i))
