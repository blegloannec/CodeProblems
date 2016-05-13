#!/usr/bin/env python

import sys

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

# la periode du calendrier est de 400 ans et le nb de
# dimanches 1er du mois sur la periode est 688

# compte depuis le 01/01/1900
def count_until(D,M,Y):
    Y -= 1900
    cpt = (Y/400)*688
    Y = 1900+Y%400
    w = 0
    d,m,y = 1,1,1900
    while (d,m,y)!=(D,M,Y):
        if d==1 and w==6:
            cpt += 1
        d,m,y = next_day(d,m,y)
        w = (w+1)%7
    return cpt

def main():
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        Y1,M1,D1 = map(int,sys.stdin.readline().split())
        Y2,M2,D2 = map(int,sys.stdin.readline().split())
        D2,M2,Y2 = next_day(D2,M2,Y2)
        print count_until(D2,M2,Y2)-count_until(D1,M1,Y1)

main()
