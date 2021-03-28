#!/usr/bin/env python3

import random
random.seed()

# analog to quicksort with 2 pivots, O(N log3 N)
def medsort(A, l0=None, r0=None):
    if len(A)<2:
        return A
    l = random.choice(A)
    A.remove(l)
    r = random.choice(A)
    A.remove(r)
    if l0 is not None:
        assert r0 is None
        print(l0,l,r, flush=True)
        m = int(input())
        assert m>0 and m!=l0
        if m==r:
            l,r = r,l
    elif r0 is not None:
        assert l0 is None
        print(l,r,r0, flush=True)
        m = int(input())
        assert m>0 and m!=r0
        if m==l:
            l,r = r,l
    L = []; M = []; R = []
    for i in A:
        print(l,i,r, flush=True)
        m = int(input())
        assert m>0
        if   m==l: L.append(i)
        elif m==r: R.append(i)
        else:      M.append(i)
    L = medsort(L, None, l)
    M = medsort(M, l, None)
    R = medsort(R, r, None)
    A = L + [l] + M + [r] + R
    return A

def case():
    A = list(range(1, N+1))
    A = medsort(A)
    print(*A, flush=True)
    assert input()=='1'

def main():
    global N
    T,N,Q = map(int, input().split())
    for _ in range(T):
        case()

main()
