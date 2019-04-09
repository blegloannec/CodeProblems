#!/usr/bin/env pypy2

# Not so "hard", at least way easier than it might look.

P = 10**9+9

# O(N^3) DP approach
# dp(i,j) = (n,e,o) where
#   n = total number of BST over (sorted) A[i:j]  (i included, j excluded)
#   e = total sum of even-depth nodes in all these trees
#   o =               odd-
def dp(i,j):
    n = int(i==j)
    e = o = 0
    if memo[i][j] is None:
        for k in xrange(i,j):
            ln,l0,l1 = dp(i,k)
            rn,r0,r1 = dp(k+1,j)
            e = (e + (ln*rn)*A[k] + rn*l1 + ln*r1) % P
            o = (o + rn*l0 + ln*r0) % P
            n = (n + ln*rn) % P
        memo[i][j] = (n,e,o)
    return memo[i][j]

if __name__=='__main__':
    T = int(raw_input())
    for _ in xrange(T):
        N = int(raw_input())
        a,b = map(int,raw_input().split())
        A = sorted(map(int,raw_input().split()))
        memo = [[None]*(N+1) for _ in xrange(N+1)]
        _,e,o = dp(0,N)
        res = (a*e-b*o) % P
        print(res)
