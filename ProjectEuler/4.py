#!/usr/bin/env python

def miroir(n):
    m = 0
    while n!=0:
        m = 10*m + n%10
        n /= 10
    return m

def palindrome(n):
    return miroir(n)==n

def problem4():
    m = 0
    for i in range(100,1000):
        for j in range(100,i+1):
            p = i*j
            if p>m and palindrome(p):
                m = p
    print m

problem4()
