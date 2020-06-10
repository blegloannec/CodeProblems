#!/usr/bin/env python3

from functools import lru_cache

def is_hill(N):
    up = True
    for i in range(1,len(N)):
        if up and N[i-1]>N[i]:
            up = False
        elif not up and N[i-1]<N[i]:
            return False
    return True

# hill(n, a) = nb of hill numbers of size n starting with a
# observe in particular that:
# hill(n+1, 0) = nb of hill numbers of size <= n
# hill(n+1, 1) = nb of hill numbers of size == n
@lru_cache(maxsize=None)
def hill(n, a=0, up=True):
    if n==1:
        return 1
    res = 0
    if up:
        for b in range(a, 10):
            res += hill(n-1, b, True)
        a -= 1
    for b in range(a+1):
        res += hill(n-1, b, False)
    return res

# for N the digits (in left to right order) of an hill number n,
# computes the number of hill numbers below n
def hill_below(N):
    up = True
    res = 0
    for i in range(len(N)):
        if up and i>0 and N[i]<N[i-1]:
            up = False
        # we compute the nb of hill numbers of size len(N) such that:
        #  - they start with N[:i]
        #  - their next digit is below N[i]
        a0 = 10
        if up:
            a0 = N[i-1] if i>0 else 0
        for a in range(N[i]):
            res += hill(len(N)-i, a, a>=a0)
    return res

def main():
    N = tuple(map(int, input()))
    print(hill_below(N) if is_hill(N) else -1)

main()
