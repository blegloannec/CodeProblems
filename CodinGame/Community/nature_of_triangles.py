#!/usr/bin/env python3

from math import atan2, pi, degrees

class Vec:
    def __init__(self, x, y):
        self.x = x; self.y = y
    def __sub__(self, B):
        return Vec(self.x-B.x, self.y-B.y)
    def __mul__(self, B):
        return self.x*B.x + self.y*B.y
    def angle(self):
        return atan2(self.y, self.x)
    def norm2(self):
        return self.x**2 + self.y**2

def normangle(a):
    a %= 2.*pi
    if a > pi: a -= 2.*pi
    return a

def main():
    N = int(input())
    for i in range(N):
        a,xa,ya, b,xb,yb, c,xc,yc = input().split()
        A = Vec(int(xa), int(ya))
        B = Vec(int(xb), int(yb))
        C = Vec(int(xc), int(yc))
        AB = B-A
        BC = C-B
        CA = A-C
        side_nat = 'a scalene'
        if   CA.norm2() == AB.norm2(): side_nat = f'an isosceles in {a}'
        elif AB.norm2() == BC.norm2(): side_nat = f'an isosceles in {b}'
        elif BC.norm2() == CA.norm2(): side_nat = f'an isosceles in {c}'
        angle_nat = 'an acute'
        if   CA*AB == 0: angle_nat = f'a right in {a}'
        elif AB*BC == 0: angle_nat = f'a right in {b}'
        elif BC*CA == 0: angle_nat = f'a right in {c}'
        else:
            CAB = abs(normangle(AB.angle()-CA.angle()+pi))
            ABC = abs(normangle(BC.angle()-AB.angle()+pi))
            BCA = abs(normangle(CA.angle()-BC.angle()+pi))
            if   CAB > pi/2.: angle_nat = f'an obtuse in {a} ({round(degrees(CAB))}°)'
            elif ABC > pi/2.: angle_nat = f'an obtuse in {b} ({round(degrees(ABC))}°)'
            elif BCA > pi/2.: angle_nat = f'an obtuse in {c} ({round(degrees(BCA))}°)'
        print(f'{a}{b}{c} is {side_nat} and {angle_nat} triangle.')

main()
