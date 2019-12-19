#!/usr/bin/env python3

from functools import lru_cache

class DP:  # O(N log N)
    def __init__(self, A):
        self.A0 = A[:]
        self.A = A
        self.N = len(self.A)
        for i in range(1,self.N):
            self.A[i] += self.A[i-1]
    
    def sum(self, l, r):
        return A[r] - (A[l-1] if l>0 else 0)
    
    def mid(self, l, r):
        i,j = l,r
        while i<j:
            m = (i+j)//2
            if self.sum(l,m)<self.sum(m+1,r):
                i = m+1
            else:
                j = m
        return i if self.sum(l,i)==self.sum(i+1,r) else None
    
    @lru_cache(maxsize=None)
    def dp(self, l, r):
        res = 0
        if l<r:
            if self.sum(l,r)==0:  # full 0 interval
                return r-l
            # There might be several valid mids due to a "median" block of 0s,
            # e.g. [1,0,0,0,1].
            # However, the one we choose does not matter: as the sum of the
            # current interval is not 0, the block of 0s will never be isolated
            # in the future, we cannot take advantage of it.
            m = self.mid(l,r)
            if m is not None:
                res = 1 + max(self.dp(l,m), self.dp(m+1,r))
        return res
    
    def result(self):
        return self.dp(0, self.N-1)


def main():
    global A
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int,input().split()))
        print(DP(A).result())

main()
