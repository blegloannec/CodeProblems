#!/usr/bin/env python

# naive O(n^2) algo (for n ~ 2500 the number of points)

N = 51

def main():
    cpt = 0
    for A in xrange(1,N*N):
        xa,ya = A%N,A/N
        da = xa*xa+ya*ya
        for B in xrange(A+1,N*N):
            xb,yb = B%N,B/N
            D = [da,xb*xb+yb*yb,(xa-xb)*(xa-xb)+(ya-yb)*(ya-yb)]
            h = max(D)
            if 2*h==sum(D):
                cpt += 1
    print cpt

main()
