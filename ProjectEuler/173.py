#!/usr/bin/env python

def main():
    M = 10**6
    cpt = 0
    a = 3
    while a*a-(a-2)*(a-2)<=M:
        for b in xrange(a-2,0,-2):
            n = a*a-b*b
            if n>M:
                break
            cpt += 1
        a += 1
    print cpt

main()
