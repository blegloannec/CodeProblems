#!/usr/bin/env python

N = 100

# progdyn to count increasing numbers
# with <=n digits
I = [[-1  for _ in xrange(10)] for _ in xrange(N+1)]
for a in xrange(10):
    I[0][a] = 1
def inc(n,a0=9):
    if I[n][a0]>=0:
        return I[n][a0]
    res = 0
    for a in xrange(a0+1):
        res += inc(n-1,a)
    I[n][a0] = res
    return res

# progdyn to count decreasing numbers
# with exactly n digits
D = [[-1 for _ in xrange(10)] for _ in xrange(N+1)]
D[0][0] = 0
for a in xrange(1,10):
    D[0][a] = 1
def dec(n,a0=0):
    if D[n][a0]>=0:
        return D[n][a0]
    res = 0
    for a in xrange(a0,10):
        res += dec(n-1,a)
    D[n][a0] = res
    return res

# constant numbers (both inc and dec)
# with <=n digits
def con(n):
    return 9*n+1

def main():
    i = inc(N)
    d = sum(dec(n) for n in xrange(N+1))
    print i+d-con(N)

main()
