#!/usr/bin/env python

M = [31,28,31,30,31,30,31,31,30,31,30,31]

def day(d,m,y):
    A = y-1900
    D = A*365+A/4 + sum(M[:m-1]) + d-1
    if y%4==0 and not (y%100==0 and y%400!=0):
        D += 1
    return D%7

print day(28,1,2000)
