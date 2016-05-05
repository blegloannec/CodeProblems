#!/usr/bin/env python

import sys

def est_lettre(c):
    return (ord('a')<=c and c<=ord('z')) or (ord('A')<=c and c<=ord('Z'))

def main():
    N = int(sys.stdin.readline())
    mess = map(int,sys.stdin.readline().split())
    maxind = 0
    for a in xrange(26):
        for b in xrange(26):
            for c in xrange(26):
                key = [a+97,b+97,c+97]
                ind = 0
                k = 0
                for i in xrange(len(mess)):
                    if est_lettre(mess[i]^key[k]):
                        ind += 1
                    k = (k+1)%3
                if ind>maxind:
                    maxind = ind
                    maxkey = key
    print ''.join(map(chr,maxkey))

main()
