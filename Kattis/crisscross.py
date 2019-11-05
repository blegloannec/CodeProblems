#!/usr/bin/env python3

import sys
from fractions import Fraction

def svg_plot(S):
    m = min(min(s[0],s[1]) for s in S) - 1
    M = max(max(s[2],s[3]) for s in S) + 1
    A = 500.
    X = lambda x: A*(x-m)/(M-m)
    O = ['<svg width="%f" height="%f">' % (A,A)]
    for s in S:
        O.append('<line x1="%f" y1="%f" x2="%f" y2="%f" stroke="blue" stroke-width="0.5" />' % tuple(map(X,s)))
    O.append('</svg>')
    F = open('out.svg', 'w')
    F.write('\n'.join(O))
    F.close()

def intersection(A,B):
    x1,y1,x2,y2 = A
    x3,y3,x4,y4 = B
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
            if max(t1,t3)<min(t2,t4):
                return -1
            elif max(t1,t3)==min(t2,t4):
                if (x1,y1)==(x3,y3) or (x1,y1)==(x4,y4):
                    return (Fraction(x1),Fraction(y1))
                else:
                    return (Fraction(x2),Fraction(y2))
        return None
    # Cramer
    t,tp = e*d-b*f,a*f-e*c
    if det<0:
        det = -det
        t = -t
        tp = -tp
    if 0<=t<=det and 0<=tp<=det:
        t,tp = Fraction(t,det),Fraction(tp,det)
        return (x1+t*a,y1+t*c)
    return None

def main():
    N = int(sys.stdin.readline())
    P = set()
    S = [tuple(map(int,sys.stdin.readline().split())) for _ in range(N)]
    #svg_plot(S)
    for a in range(N):
        for b in range(a+1,N):
            I = intersection(S[a],S[b])
            if I is not None:
                if I==-1:
                    print(-1)
                    return
                # way way faster than hashing the Fraction objects
                P.add((I[0].numerator,I[0].denominator,I[1].numerator,I[1].denominator))
    print(len(P))

main()
