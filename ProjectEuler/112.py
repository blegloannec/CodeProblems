#!/usr/bin/env python

def digits(n,b=10):
    c = []
    while n>0:
        c.append(n%b)
        n /= b
    return c

def bouncy(n):
    inc,dec = False,False
    dig = digits(n)
    for i in xrange(len(dig)-1):
        if dig[i]>dig[i+1]:
            inc = True
        elif dig[i]<dig[i+1]:
            dec = True
    return inc and dec

def main():
    cpt = 0
    n = 100
    while 100*cpt<99*(n-1):
        if bouncy(n):
            cpt += 1
        n += 1
    print n-1

main()
