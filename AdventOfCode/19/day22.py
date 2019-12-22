#!/usr/bin/env python3

import sys

I = [L.rstrip('\n').split() for L in sys.stdin.readlines()]


# Part 1 (naive simulation to set the ideas down)
N = 10007

def deal_inc(C,k):
    D = [None]*N
    for i,c in enumerate(C):
        D[(k*i)%N] = c
    return D

def simu():
    C = list(range(N))
    for L in I:
        if L[0]=='cut':
            k = int(L[1])
            if k<0:
                k += N
            C = C[k:]+C[:k]
        elif L[1]=='into':
            C.reverse()
        else:
            k = int(L[3])
            C = deal_inc(C,k)
    return C

print(simu().index(2019))


# Part 2 (proper maths)
def rev_shuffle(N=119315717514047, E=101741582076661, p=2020):
    # for N a prime number
    inv = lambda x: pow(x,N-2,N)
    a,b = 1,0  # for position ap+b
    for L in reversed(I):
        if L[0]=='cut':
            k = int(L[1])
            # p = p+k mod N
            b = (b+k) % N
        elif L[1]=='into':
            # p = -p-1 mod N
            a = (-a) % N
            b = (-b-1) % N
        else:
            k = int(L[3])
            l = inv(k)
            # p = p*l mod N
            a = (a*l) % N
            b = (b*l) % N
    # after one pass of the shuffle, the card in position x was
    # initially in position ax+b
    # hence after two passes, it was in a(ax+b)+b = a^2x + ab + b
    # after three passes, it was in a^3x + a^2b + ab + b
    # after E passes, it was in a^E*x + sum(a^k, k=0..E-1)*b
    aE = pow(a,E,N)
    return (aE*p + ((aE-1)*inv(a-1))*b) % N

print(rev_shuffle())
