#!/usr/bin/env python

import sys

def main():
    T = int(sys.stdin.readline())
    for t in range(T):
        N,K = map(int,sys.stdin.readline().split())
        A = map(int,sys.stdin.readline().split())
        nb = 0
        for a in A:
            if a<=0:
                nb += 1
        print 'YES' if nb<K else 'NO'

main()
