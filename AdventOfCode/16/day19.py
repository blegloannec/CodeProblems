#!/usr/bin/env python

Input = 3018458

# Part One
def josephus(n,k=2):
    p = 0
    for i in xrange(2,n+1):
        p = (p+k)%i
    return p

# +1 as 1-indexed instead of 0-indexed
print josephus(Input)+1


# Part Two
def josephus2(n):
    p = 0
    for i in xrange(2,n+1):
        p += 1       # rotation 
        if (p>=i/2): # si on est apres l'elimine
            p += 1   # alors on decale
        p %= i
    return p

print josephus2(Input)+1
