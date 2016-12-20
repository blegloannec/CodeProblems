#!/usr/bin/env python

Input = '00101000101111010'

def dragon(A,n):
    A = list(A)
    while len(A)<n:
        # recent discovery: reversed() to reverse an iterator
        # (requires length and random access)
        A += ['0']+['0' if a=='1' else '1' for a in reversed(A)]
    return A[:n]

def checksum(A):
    while len(A)%2==0:
        A = ['1' if A[i]==A[i+1] else '0' for i in xrange(0,len(A)-1,2)]
    return ''.join(A)

# Part One
print checksum(dragon(Input,272))

# Part Two
print checksum(dragon(Input,35651584))
