#!/usr/bin/env python

def sig(n):
    d = []
    while n>0:
        d.append(n%10)
        n /= 10
    d.sort(reverse=True)
    s = 0
    for x in d:
        s = 10*s+x
    return s

def main():
    D = {}
    for n in xrange(1,100000):
        c = n*n*n
        s = sig(c)
        if s in D:
            D[s].append(n)
        else:
            D[s] = [n]
    nmin = 1<<63
    for s in D:
        if len(D[s])==5:
            nmin = min(nmin,min(D[s]))
    print nmin*nmin*nmin

main()
