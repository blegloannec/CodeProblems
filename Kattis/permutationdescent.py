#!/usr/bin/env python3

from functools import lru_cache

P = 1001113

@lru_cache(maxsize=None)
def PDC(n, k):
    assert 0<=k<n
    if k==0 or k==n-1:
        return 1
    # to build a perm. from PDC(n,k):
    # either insert n in a     desc. pos. of a perm. from PDC(n-1,k)
    #                     (k pos. + the end = k+1)
    # or                   non-desc.                      PDC(n-1,k-1)
    #                     ((n-2)-(k-1) pos. + the beginning = n-k)
    return ((k+1)*PDC(n-1,k) + (n-k)*PDC(n-1,k-1)) % P

def main():
    T = int(input())
    for _ in range(T):
        C,n,k = map(int, input().split())
        print(C, PDC(n,k))

main()
