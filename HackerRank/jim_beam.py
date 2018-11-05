#!/usr/bin/env python3

from fractions import Fraction

# segments intersection, modified from PE 165
def intersection(x1,y1,x2,y2,x3,y3,x4,y4):
    a,b,e = x2-x1,-(x4-x3),x3-x1
    c,d,f = y2-y1,-(y4-y3),y3-y1
    det = a*d-b*c
    if det==0:          # cas //
        if a*f-c*e==0:  # cas alignes
            norm2 = a*a+c*c
            t3 = Fraction(a*e+c*f,norm2)
            t4 = Fraction(a*(x4-x1)+c*(y4-y1),norm2)
            if t3>t4:
                t3,t4 = t4,t3
            return not (t4<0 or 1<t3)
        return False
    # Cramer
    t,tp = Fraction(e*d-b*f,det),Fraction(a*f-e*c,det)
    return (0<=t<=1 and 0<=tp<=1)

def main():
    T = int(input())
    for _ in range(T):
        x1,y1,x2,y2,xm,ym = map(int,input().split())
        print('YES' if not intersection(0,0,xm,ym,x1,y1,x2,y2) else 'NO')

main()
