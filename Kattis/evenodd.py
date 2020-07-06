#!/usr/bin/env python3

MOD = 10**9+7

def f(x):
    i = 0
    while x>1:
        if x&1==0:
            x >>= 1
        else:
            x += 1
        i += 1
    return i

# the sum can then be computed recursively in O(log n)
def S(n):
    if n<=1:
        return 0
    if n==2:
        return 1
    if n&1==0:
        # even nbs 2..n   are /2      -> n/2 + S(n/2)
        # odd  nbs 3..n-1 are +1 & /2 -> 2*(n/2-1) + S(n/2)
        n >>= 1
        return 2*S(n) + 3*n - 2
    else:
        return f(n) + S(n-1)

def main():
    L,R = map(int, input().split())
    res = (S(R) - S(L-1)) % MOD
    print(res)

main()
