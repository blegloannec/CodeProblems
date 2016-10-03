#!/usr/bin/env python

# runs in 4.5s with pypy

M = 10**9

# prog dyn facon diviser pour regner
# dp(n,s,r) = nb de nb a n chiffres de somme des chiffres s
#             et de reste r modulo 23
memo = {}
def dp(n,s=23,r=0):
    if n==0:
        return 1 if (s,r)==(0,0) else 0
    if n==1:
        return 1 if s<10 and s==r else 0
    if s==0: # pour aller un peu plus vite (negligeable)
        return 1 if r==0 else 0
    if (n,s,r) in memo:
        return memo[n,s,r]
    n0 = n/2
    n1 = n-n0
    p10 = pow(10,n1,23)
    res = 0
    for s0 in xrange(s+1):
        s1 = s-s0
        for r0 in xrange(23):
            r1 = (r-p10*r0)%23
            res = (res+dp(n0,s0,r0)*dp(n1,s1,r1))%M
    memo[n,s,r] = res
    return res

print dp(11**12)
