#!/usr/bin/env python

import sys

win = {0:False, 1:False}
def progdyn(n):
    if n not in win:
        win[n] = not progdyn(n-2) or (n>2 and not progdyn(n-3)) or (n>4 and not progdyn(n-5))
    return win[n]

def main():
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        n = int(sys.stdin.readline())
        if progdyn(n):
            print 'First'
        else:
            print 'Second'

main()
