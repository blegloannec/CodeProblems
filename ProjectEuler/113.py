#!/usr/bin/env python

N = 100

# At first, used a prog-dyn to count increasing and decreasing
# numbers. Then realised it was actually easy to count directly:
# 1. To build an increasing number of size <=n, simply pick a
# multiset of {0..9} of size n, hence there are binom(n+10-1,n) of them.
# 2. For decreasing numbers, it is trickier as you can pick leading (to cover
# numbers of size <n) as well as trailing 0s. Just distinguish those two
# kinds of zero to get binom(n+11-1,n) numbers and remove the full 0s
# that you get in several ways picking only leading and trailing zeros,
# so binom(n+11-1,n) - (N+1).
# 3. Add both quantities and remove 9N+1 constant numbers that are
# counted twice.

def binom(n,p):
    return 1 if p==0 else n*binom(n-1,p-1)/p

print binom(N+9,N) + binom(N+10,N)-(N+1) - (9*N+1)
