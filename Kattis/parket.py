#!/usr/bin/env python3

from math import sqrt

# R = 2L+2W-4
# B = (L-2)*(W-2) = LW - R
# X = L+W = (R+4)/2
# Y = LW = B+R
# X = L+Y/L
# L^2 - XL + Y = 0

R,B = map(int,input().split())
X = R//2+2
Y = B+R
d = round(sqrt(X*X-4*Y))
print((X+d)//2, (X-d)//2)
