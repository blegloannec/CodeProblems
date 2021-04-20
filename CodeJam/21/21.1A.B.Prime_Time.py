#!/usr/bin/env pypy

# let P the given set of primes
#     S the sum of all primes with multiplicities
# (A,B) a target partition, sum A = prod B
# 0 < prod B = sum A < 499.10^15 < 2^59
# hence |B| < 59
# hence sum B <= 58 * 499 = 28942
# but S = sum A + sum B
# hence S-28942 <= sum A = prod B < S, a pretty small range
# try all these as prod B, factor each of them using P

def sum_of_factors(p):
    s = 0
    for pi,ni in PN:
        n = 0
        while p%pi==0:
            p /= pi
            n += 1
        if n<=ni:
            s += pi*n
            if p==1:
                break
        else:
            return 0  # invalid candidate p
    return s if p==1 else 0

def main():
    global PN
    T = int(raw_input())
    for t in xrange(1, T+1):
        M = int(raw_input())
        PN = [tuple(map(int, raw_input().split())) for _ in xrange(M)]
        S = sum(p*n for p,n in PN)
        res = 0
        for s in xrange(S-1, max(0, S-28943), -1):
            if s+sum_of_factors(s)==S:
                res = s
                break
        print('Case #{}: {}'.format(t, res))

main()
