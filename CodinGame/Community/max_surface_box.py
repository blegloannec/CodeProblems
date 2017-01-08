#!/usr/bin/env python3

import sys

# given N, we want to find 3 positive integers x,y,z
# that minimize/maximize the area 2(xy+xz+yz) under
# the constraint xyz = N
# Lagrange multipliers try
# L(x,y,z,l) = xy+xz+yz - l(xyz-N)
# dL/dx = y+z - lyz = 0
# dL/dy = x+z - lxz = 0
# dL/dz = x+y - lxy = 0
# dL/dl = -xyz + N = 0  (constraint)
# y+z / yz = x+z / xz = x+y / xy (= l)
# x(y+z) = y(x+z) = z(x+y) (= lxyz)
# well, well, well, maybe come back to that later?

# "naive" solution, without event caring about factoring N
N = int(sys.stdin.readline())
mini,maxi = float('inf'),0
for x in range(1,int(N**(1/3))+2):
    if N%x==0:
        M = N//x
        for y in range(x,int(M**(1/2))+1):
            if M%y==0:
                z = M//y
                a = 2*(x*y+x*z+y*z)
                mini = min(mini,a)
                maxi = max(maxi,a)
print(mini,maxi)
