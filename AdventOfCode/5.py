#!/usr/bin/env python

import sys
import re

re1 = re.compile('(.*[aeiou]){3}')
re2 = re.compile(r'(.)\1')
#re2 = re.compile('|'.join([2*chr(i) for i in range(97,123)]))
re3 = re.compile('ab|cd|pq|xy')

re4 = re.compile(r'(..).*\1')
re5 = re.compile(r'(.).\1')

def c1(s):
    return (re1.search(s)!=None)

def c2(s):
    return (re2.search(s)!=None)

def c3(s):
    return (re3.search(s)==None)

def c4(s):
    return (re4.search(s)!=None)

def c5(s):
    return (re5.search(s)!=None)

def main():
    f = open(sys.argv[1],'r')
    cases = f.readlines()
    f.close()
    cpt = 0
    cpt2 = 0
    for l in cases:
        s = l.strip()
        #print s,c1(s),c2(s),c3(s)
        if c1(s) and c2(s) and c3(s):
            cpt += 1
        if c4(s) and c5(s):
            cpt2 += 1
    print cpt,cpt2

main()
