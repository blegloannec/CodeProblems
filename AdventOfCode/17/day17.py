#!/usr/bin/env pypy

# analog to Josephus problem (see also AoC 2016 day 19)

I = 355  # Input

# Part 1
def spinlock1(n,k):
    p = (-(k+1))%n
    i = n-1
    while p!=0:
        p = (p-(k+1))%i
        i -= 1
    return i

print spinlock1(2017,I)


# Part 2
def spinlock2(n,k):
    p = 0  # insertion position
    for i in xrange(1,n+1):
        if p==0:  # i is inserted right after 0
            m = i
        p = (p+k+1)%(i+1)
    return m

print spinlock2(50000000,I)
