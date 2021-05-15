#!/usr/bin/env pypy

NMAX = 10**6+1

def precomp():
    # O(N√N) DP, runs in <10s with pypy2
    # Cα[n] = max length k of a divisors chain α ≤ a1 | a2 | ... | ak
    #         such that ∑ ai = n
    C2 = [1]*NMAX
    C2[0] = C2[1] = 0
    C3 = [1]*NMAX
    C3[0] = C3[1] = C3[2] = 0
    for n in xrange(3, NMAX):
        d = 2
        while d*d<=n:
            if n%d==0:
                # n = d*(1 + chain of sum n/d)
                C2[n] = max(C2[n], C2[n//d-1]+1)
                C2[n] = max(C2[n], C2[d-1]+1)
                if d>2:
                    C3[n] = max(C3[n], C2[n//d-1]+1)
                if n//d>2:
                    C3[n] = max(C3[n], C2[d-1]+1)
            d += 1
    return C3

def main():
    C = precomp()
    T = int(raw_input())
    for t in xrange(1, T+1):
        n = int(raw_input())
        print('Case #{}: {}'.format(t, C[n]))

main()
