#!/usr/bin/env python

def mirror(n):
    m = 0
    while n>0:
        m = 10*m + n%10
        n /= 10
    return m

def is_palindrome(n):
    return mirror(n)==n

def lychrel(n):
    k = 1
    while k<=50:
        n += mirror(n)        
        if is_palindrome(n):
            return False
        k += 1
    return True

def main():
    cpt = 0
    for n in xrange(1,10000):
        if lychrel(n):
            cpt += 1
    print cpt

main()
