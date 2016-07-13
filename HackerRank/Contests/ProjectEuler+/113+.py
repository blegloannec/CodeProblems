#!/usr/bin/env python

import sys

N = 10**5
P = 10**9+7

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
        res = (res + inc(n-1,a))%P
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
        res = (res + dec(n-1,a))%P
    D[n][a0] = res
    return res

def main():
    # to avoid recursion limitation
    for n in xrange(N):
        inc(n)
        dec(n)
    d = [0 for _ in xrange(N+1)]
    for i in xrange(1,N+1):
        d[i] = (d[i-1]+dec(i))%P
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        k = int(sys.stdin.readline())
        print (inc(k)+d[k]-9*k-1)%P

main()
