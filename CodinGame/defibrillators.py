#!/usr/bin/env python3

from math import cos,sqrt,pi

# https://en.wikipedia.org/wiki/Haversine_formula
# http://www.movable-type.co.uk/scripts/latlong.html
def dist(lo1,la1,lo2,la2):
    x = (lo2-lo1)*cos((la1+la2)/2)
    y = la2-la1
    return 6371*sqrt(x*x+y*y)

def ang(s):
    return pi*float(s.replace(',','.'))/180

lon = ang(input())
lat = ang(input())
n = int(input())
D = []
for _ in range(n):
    _,name,_,_,lo,la = input().split(';')
    D.append((name,ang(lo),ang(la)))

print(min(D,key=(lambda d: dist(lon,lat,d[1],d[2])))[0])
