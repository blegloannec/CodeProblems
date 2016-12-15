#!/usr/bin/env python

# we use the Chinese remainder theorem
# though considering the input size, a naive simulation should work
# (at least 2 more discs would have been better)

def bezout(a,b):
    if b==0:
        return (a,1,0)
    g,u,v = bezout(b,a%b)
    return (g,v,u-(a/b)*v)

def rev_chinois(a,p,b,q):
    g,u,v = bezout(p,q)
    assert(g==1)
    return (b*u*p+a*v*q)%(p*q)

def solve(I):
    a,p = 0,1
    for i in xrange(len(I)):
        q,b = I[i]
        a = rev_chinois(a,p,-(i+1+b),q)
        p *= q
    return a

# Example
#Input = [(5,4),(2,1)]

# Part One
Input = [(13,11),(5,0),(17,11),(3,0),(7,2),(19,17)]
print solve(Input)

# Part Two
Input.append((11,0))
print solve(Input)
