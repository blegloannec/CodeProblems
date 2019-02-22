#!/usr/bin/env python3

from math import *

f = int(input())
F = map(float,input().split())

x0,y0 = map(float,input().split())
m = float(input())
a = float(input())*pi/180.
s0 = float(input())
dx0,dy0 = s0*cos(a),s0*sin(a)
gx,gy = map(float,input().split())

# mx" = mg
# x' = gt + dx0
# x = 1/2gt^2 + dx0t + x0
# y = 0 <=> 1/2*gy*t^2 + dy0*t + y0 = 0
t = (-dy0 - sqrt(dy0**2 - 2.*gy*y0)) / gy
x = 0.5*gx*t**2 + dx0*t + x0
x = round(x,2)
print(sum(int(d>x) for d in F)+1)
