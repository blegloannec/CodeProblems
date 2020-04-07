#!/usr/bin/env python3

from math import gcd

def first_tree(x1,y1, rx1,ry1, rx2,ry2):
    g = gcd(x1,y1)
    if g==1:
        return None
    inside = lambda x,y: rx1<=x<=rx2 and ry1<=y<=ry2
    x,y = x1//g, y1//g        # first tree
    if not inside(x,y):
        return (x,y)
    lx,ly = (g-1)*x, (g-1)*y  # last tree
    if inside(lx,ly):
        return None
    k = min(rx2//x, ry2//y) + 1
    return (k*x,k*y)

def main():
    x1,y1 = map(int,input().split())
    rx1,ry1, rx2,ry2 = map(int,input().split())
    res = first_tree(x1,y1, rx1,ry1, rx2,ry2)
    if res is None:
        print('Yes')
    else:
        print('No')
        print(*res)

main()
