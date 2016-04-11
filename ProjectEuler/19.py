#!/usr/bin/env python

M = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def leap(y):
    return y%4==0 and not (y%100==0 and y%400!=0)

def next_day(d,m,y):
    if (d,m)==(28,2) and leap(y):
        return (29,2,y)
    if (d,m)==(31,12):
        return (1,1,y+1)
    if d<M[m]:
        return (d+1,m,y)
    return (1,m+1,y)

def main():
    cpt = 0
    w = 0
    d,m,y = 1,1,1900
    while (d,m,y)!=(1,1,2001):
        if y>1900 and d==1 and w==6:
            cpt += 1
        d,m,y = next_day(d,m,y)
        w = (w+1)%7
    print cpt

main()
