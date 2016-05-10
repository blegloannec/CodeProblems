#!/usr/bin/env python

import sys

D = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}

def main():
    s = list(sys.stdin.readline().strip())
    for i in xrange(len(s)):
        s[i] = D[s[i]]
    print ''.join(s[::-1])

main()
