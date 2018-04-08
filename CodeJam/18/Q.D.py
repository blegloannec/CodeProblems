#!/usr/bin/env python3

from math import *

EPS = 1e-12
S2 = sqrt(2)


# Rotation around the x-axis for areas from 1 to sqrt(2)
A = (-0.5,0.5,-0.5)
B = (0.5,0.5,-0.5)
C = (0.5,0.5,0.5)
D = (-0.5,0.5,0.5)
E = (-0.5,-0.5,-0.5)
F = (0.5,-0.5,-0.5)
G = (0.5,-0.5,0.5)
H = (-0.5,-0.5,0.5)

O1 = (0.5,0.,0.)
O2 = (0.,0.5,0.)
O3 = (0.,0.,0.5)

def Rx(a):
    return [[1.,0.,0.],
            [0.,cos(a),sin(a)],
            [0.,-sin(a),cos(a)]]

def prod(R,P):
    return tuple(sum(R[i][k]*P[k] for k in range(3)) for i in range(3))

lim = pi/4.

def dicho(area0):
    l,r = 0.,lim
    while True:
        a = (l+r)/2.
        R = Rx(a)
        AA = prod(R,A)
        HH = prod(R,H)
        area = HH[2]-AA[2]
        if r-l<EPS:
            return a
        if area0<area:
            r = a
        else:
            l = a


# Rotation around the z-axis starting from the ending position of the previous
# rotation (pi/4 rotated cube), only for areas > sqrt(2)
R1 = Rx(lim)
A1 = prod(R1,A)
B1 = prod(R1,B)
C1 = prod(R1,C)
D1 = prod(R1,D)
E1 = prod(R1,E)
F1 = prod(R1,F)
G1 = prod(R1,G)
H1 = prod(R1,H)

O11 = prod(R1,O1)
O21 = prod(R1,O2)
O31 = prod(R1,O3)

def Rz(a):
    return [[cos(a),-sin(a),0.],
            [sin(a),cos(a),0.],
            [0.,0.,1.]]

lim1 = atan(1./S2)

def dicho1(area0):
    l,r = 0.,lim1
    while True:
        a = (l+r)/2.
        R = Rz(a)
        AA = prod(R,A1)
        BB = prod(R,B1)
        DD = prod(R,D1)
        area = (BB[0]-AA[0])*S2 + S2*(AA[0]-DD[0])
        if r-l<EPS:
            return a
        if area0<area:
            r = a
        else:
            l = a


# MAIN
def main():
    T = int(input())
    for t in range(1,T+1):
        print('Case #%d:' % t)
        area0 = float(input())
        if area0<=S2:
            a = dicho(area0)
            R = Rx(a)
            print(*prod(R,O1))
            print(*prod(R,O2))
            print(*prod(R,O3))
        else:
            a = dicho1(area0)
            R = Rz(a)
            print(*prod(R,O11))
            print(*prod(R,O21))
            print(*prod(R,O31))

main()
