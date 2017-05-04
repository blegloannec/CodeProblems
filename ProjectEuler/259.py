#!/usr/bin/env python

from fractions import *

# similaire au pb du "compte est bon"
# voir aussi pb 93 ou 155
# runs in 42s with pypy

R = [[None]*10 for _ in xrange(10)]

def reach(a=1,b=9):
    assert(0<=a<=b)
    if R[a][b]!=None:
        return R[a][b]
    R[a][b] = set()
    x = 0
    for i in xrange(a,b+1):
        x = 10*x+i
    R[a][b].add(Fraction(x))
    for i in xrange(a,b):
        X,Y = reach(a,i),reach(i+1,b)
        for x in X:
            for y in Y:
                R[a][b].add(x+y)
                R[a][b].add(x-y)
                R[a][b].add(x*y)
                if y!=0:
                    R[a][b].add(x/y)
    return R[a][b]

def main():
    cpt = 0
    for x in reach():
        if x>0 and x.denominator==1:
            cpt += x.numerator
    print(cpt)

main()
