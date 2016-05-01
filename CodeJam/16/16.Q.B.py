#!/usr/bin/env python

import sys

def main():
    T = int(sys.stdin.readline())
    for t in range(1,T+1):
        s = sys.stdin.readline().strip()
        while len(s)>0 and s[-1]=='+':
            s = s[:-1]
        if len(s)==0:
            print 'Case #%d: 0' % (t)
            continue
        cpt = 1
        c = s[0]
        for i in range(1,len(s)):
            if s[i]!=c:
                c = s[i]
                cpt += 1
        print 'Case #%d: %d' % (t,cpt)

main()
