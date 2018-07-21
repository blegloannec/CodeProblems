#!/usr/bin/env python

def syracuse(n):
    return n/2 if n%2==0 else 3*n+1

def problem14():
    n = 1000001
    t = [-1 for i in range(n)]
    t[1] = 1
    def aux(s):
        if s>=n:
            return 1+aux(syracuse(s))
        elif t[s]<0:
            t[s] = 1+aux(syracuse(s))
        return t[s]
    cmax = 0
    for s in range(2,n):
        c = aux(s)
        if c>cmax:
            cmax = c
            smax = s
    print smax

problem14()
