#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt, hypot

def suspended_triangle_width(a, b, c):
    # A = (0,0), B = (c,0), C = (x,y)
    #     x² + y² = b²
    # (c-x)² + y² = a²
    x = (c*c-a*a+b*b)/(2.*c)
    y = sqrt(b*b-x*x)
    # center of mass G
    gx, gy = (0.+c+x)/3., (0.+0.+y)/3.
    # vector CG (normalized)
    vx, vy = gx-x, gy-y
    vn = hypot(vx,vy)
    vx, vy = vx/vn, vy/vn
    # distance A & B to line (CG)
    nx, ny = -vy, vx
    da = abs((0.-x)*nx+(0.-y)*ny)
    db = abs((c-x)*nx+(0.-y)*ny)
    return da+db

def main():
    N = int(input())
    L = 0.
    for _ in range(N):
        A,B,C = map(int, input().split())
        L += suspended_triangle_width(A, B, C)
    print(L)

main()
