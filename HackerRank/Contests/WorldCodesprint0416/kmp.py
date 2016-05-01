#!/usr/bin/env python

import sys

def word(W):
    return ''.join(map((lambda x: chr(x+ord('a'))), W))

def main():
    F = map(int,sys.stdin.readline().split())
    a,b,f = None,None,None
    for i in xrange(26):
        if F[i]>0:
            if a!=None and b==None:
                b = i
            if a==None:
                a = i
            if f==None or F[i]<F[f]:
                f = i
    W = []
    if f!=a:
        W.append(f)
        F[f] -= 1
    elif b!=None:
        W.append(a)
        F[a] -= 1
        while F[a]>0:
            W.append(a)
            W.append(b)
            F[a] -= 1
            F[b] -= 1
    for i in xrange(26):
        for j in xrange(F[i]):
            W.append(i)
    print word(W)


main()
