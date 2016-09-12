#!/usr/bin/env python

# DP for the number of step numbers of size n
# using last as last digit and seen as used digits
# (seen is coded as a 10-bit binary number)
memo = {}
def step(n,last,seen):
    if n==1:
        return 1 if last>0 and seen==1<<last else 0
    if (n,last,seen) in memo:
        return memo[n,last,seen]
    res = 0
    if last>0 and (seen>>(last-1))&1:
        res += step(n-1,last-1,seen)+step(n-1,last-1,seen^(1<<last))
    if last<9 and (seen>>(last+1))&1:
        res += step(n-1,last+1,seen)+step(n-1,last+1,seen^(1<<last))
    memo[n,last,seen] = res
    return res

def main():
    full = (1<<10)-1
    cpt = 0
    for n in xrange(10,41):
        for a in xrange(10):
            cpt += step(n,a,full)
    print cpt

main()
