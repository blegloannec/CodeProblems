#!/usr/bin/env python3

import sys

def intersection(A,B):
    x1,y1,x2,y2 = A
    x3,y3,x4,y4 = B
    if (x1,y1)==(x2,y2):
        if (x3,y3)==(x4,y4):
            return (x1,y1) if (x1,y1)==(x3,y3) else None
        # swap
        x1,y1,x2,y2 = B
        x3,y3,x4,y4 = A
    a,b,e = x2-x1,-(x4-x3),x3-x1
    c,d,f = y2-y1,-(y4-y3),y3-y1
    det = a*d-b*c
    if det==0:          # parallel
        if a*f-c*e==0:  # aligned
            t1 = 0
            t2 = a*a+c*c
            t3 = e*a+f*c
            t4 = (x4-x1)*a+(y4-y1)*c
            if t3>t4:
                t3,t4 = t4,t3
            tl, tr = max(t1,t3)/t2, min(t2,t4)/t2
            if tl<tr:
                return (x1+tl*a, y1+tl*c, x1+tr*a, y1+tr*c)
            elif tl==tr:
                return (x1+tl*a, y1+tl*c)
        return None
    # Cramer
    t,tp = e*d-b*f,a*f-e*c
    if det<0:
        det = -det
        t = -t
        tp = -tp
    if 0<=t<=det and 0<=tp<=det:
        t, tp = t/det, tp/det
        return (x1+t*a, y1+t*c)
    return None

def main():
    N = int(sys.stdin.readline())
    for _ in range(N):
        x1,y1,x2,y2,x3,y3,x4,y4 = map(int,sys.stdin.readline().split())
        I = intersection((x1,y1,x2,y2),(x3,y3,x4,y4))
        if I is None:
            print('none')
        elif len(I)==2:
            print('%.2f %.2f' % I)
        else:
            x1,y1,x2,y2 = I
            if (x1,y1)>(x2,y2):
                I = x2,y2,x1,y1
            print('%.2f %.2f %.2f %.2f' % I)

main()
