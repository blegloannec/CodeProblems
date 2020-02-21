#!/usr/bin/env python3

# K is acceptable iff considering A(k) = {Ai >> k, 1<=i<=n}, we can reorder
# them (circularly) in such a way that no two consecutive values xor to 0,
# i.e. are equal.
# Hence iff no value in A(k) appears more than N/2 times.

from collections import Counter

def main():
    N = int(input())
    A = list(map(int,input().split()))
    K = max(a.bit_length() for a in A)-1
    while K>=0:
        C = Counter(a>>K for a in A)
        m = max(C.values())
        if m<=N//2:
            break
        K -= 1
    print(K)

main()
