#!/usr/bin/env python

def axis_para(n,m):
    return n*(n+1)/2 * m*(m+1)/2

# terrible (almost 7s with pypy)...
def cross(n,m):
    cpt = 0
    for x in xrange(2*n-1):
        for y in xrange(1,2*m):
            if x%2==y%2:
                X,Y = float(x)/2+1,float(y)/2
                for i in xrange(min(y,2*n-x)):
                    for j in xrange(min(2*n-x,2*m-y)):
                        X0,Y0 = X+0.5*i+0.5*j,Y-0.5*i+0.5*j
                        if 0<=X0<=n and 0<=Y0<=m:
                            cpt += 1
    return cpt

def main():
    cpt = 0
    for m in xrange(1,44):
        for n in xrange(m,48):
            c = axis_para(n,m)+cross(n,m)
            cpt += c if (n==m or n>=44) else 2*c
    print cpt

main()
