#!/usr/bin/env python3

# pfff...

def num(c):
    return ord(c)-ord('A')

def let(i):
    return chr(i+ord('A'))

def plate2int(X):
    n0 = 26*num(X[7])+num(X[8])
    n1 = int(X[3:6])-1
    n2 = 26*num(X[0])+num(X[1])
    n = n2*999*26**2 + n0*999 + n1
    return n

def int2plate(n):
    s1 = '%03d' % (n%999+1)
    n //= 999
    s0 = let((n//26)%26) + let(n%26)
    n //= 26**2
    s2 = let(n//26) + let(n%26)
    return '-'.join([s2,s1,s0])

X = input()
n = int(input())
print(int2plate(plate2int(X)+n))
