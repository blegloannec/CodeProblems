#!/usr/bin/env python3

# interactive problem!

# It is not hard to notice that, knowing all but one
# elements of A[l] .. A[r], one can deduce the missing
# one by requesting [l,r] (whatever the given k).
# Then simply notice that we can request [1,r] for all r ≤ n
# as ∑ 1/r² < π²/6 < 5/3 (to successively deduce each A[r]).

import sys
from functools import lru_cache
input = sys.stdin.readline

MOD = 10**9+7
def invmod(n):
    return pow(n, MOD-2, MOD)

# dp(k,r) = sum of prod. of k elements of A[0] .. A[r]
@lru_cache(maxsize=None)
def dp(k, r):
    if k==0:
        return 1
    if k>r+1:
        return 0
    return (dp(k, r-1) + dp(k-1, r-1)*A[r]) % MOD

def send_recv(l,r):
    sys.stdout.write(f'1 {l+1} {r+1}\n')
    sys.stdout.flush()
    return map(int, input().split())

def main():
    global A
    N = int(input())
    A = [0]*N
    for r in range(N):
        k,S = send_recv(0,r)
        # S = dp(k,r-1) + dp(k-1,r-1)*A[r]
        A[r] = ((S - dp(k,r-1)) * invmod(dp(k-1,r-1))) % MOD
    sys.stdout.write(f'2 {" ".join(map(str, A))}\n')
    sys.stdout.flush()

main()
