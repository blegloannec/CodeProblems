#!/usr/bin/env python

# might be a stupid solution (yet fast way enough) as
# we do not use the formula for the sum of squares...
# but it actually does not seem to help here...

def mirror(n):
    m = 0
    while n>0:
        m = 10*m + n%10
        n /= 10
    return m

def is_palindrome(n):
    return mirror(n)==n

def main():
    M = 10**8
    N = 10**4
    # some numbers (actually only 2) can be obtained as several sums
    U = set()
    for i in xrange(1,N+1):
        s = i*i
        for j in xrange(i+1,N+1):
            s += j*j
            if s>=M:
                break
            if is_palindrome(s):
                U.add(s)
    print sum(U)

main()
