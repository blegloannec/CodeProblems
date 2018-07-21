#!/usr/bin/env python

def digits(n,b=10):
    c = []
    while n>0:
        c.append(n%b)
        n /= b
    return c

def test(n):
    D = sorted(digits(n))
    for i in xrange(2,7):
        if sorted(digits(i*n))!=D:
            return False
    return True
    
def main():
    n = 1
    while not test(n):
        n += 1
    print n

main()
