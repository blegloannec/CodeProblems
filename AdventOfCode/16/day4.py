#!/usr/bin/env python

import sys, re
from collections import defaultdict

def decrypt(s,n):
    d = []
    for c in s:
        if c=='-':
            d.append(' ')
        else:
            d.append(chr((((ord(c)-ord('a'))+n)%26)+ord('a')))
    return ''.join(d)

def main():
    S = 0
    R = re.compile('(.*)-([0-9]*)\[([a-z]*)\]')
    for L in sys.stdin.readlines():
        M =  R.match(L)
        C = [0 for _ in xrange(26)]
        for s in M.group(1):
            if s!='-':
                C[ord(s)-ord('a')] += 1
        C = sorted([(-C[i],chr(i+ord('a'))) for i in xrange(26)])
        CS = ''.join(map((lambda (_,y): y),C[:5]))
        if CS==M.group(3):
            s = int(M.group(2))
            S += s
            d = decrypt(M.group(1),s)
            if d.find('north')>=0:
                print d,s
    print S

main()
