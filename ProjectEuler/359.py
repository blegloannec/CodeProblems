#!/usr/bin/env python

from math import sqrt

# Code de test
def is_sqr(n):
    s = int(sqrt(n))
    return s*s==n

R = []

def insert(n):
    for i in xrange(len(R)):
        if is_sqr(n+R[i][-1]):
            R[i].append(n)
            return
    R.append([n])

# Calculs
def row_fst(n):
    if n==0:
        return 1
    return 2*(n/2)*(n/2+1)+(n%2)*(n+1)

def sqr_sum(a,b):
    if a==0:
        return b*(b+1)*(2*b+1)/6
    return sqr_sum(0,b)-sqr_sum(0,a-1)

def even_sqr_sum(a,b):
    return 4*sqr_sum((a+1)/2,b/2)

def odd_sqr_sum(a,b):
    i1,i2 = a/2,(b-1)/2
    return 4*sqr_sum(i1,i2)+2*(i2-i1+1)*(i1+i2)+(i2-i1+1)

def half_sqr_sum(a,b):
    if a%2==0:
        return even_sqr_sum(a,b)
    return odd_sqr_sum(a,b)

def row_sum(r,c):
    sqr_fst = r+1+r%2 if r>0 else 2
    if c%2==0:
        return half_sqr_sum(sqr_fst,sqr_fst+c)
    return row_fst(r)+half_sqr_sum(sqr_fst+1,sqr_fst+c)

def case(r,c):
    return row_sum(r,c-1)-row_sum(r,c-2)

# Code de test
def test():
    for i in xrange(1,200):
        insert(i)
    for i in xrange(len(R)):
        print R[i]
        #print R[i][0], row_fst(i)#-R[i-1][0]
        L = []
        for j in xrange(len(R[i])):
            #L.append(R[i][j]+R[i][j-1])
            L.append(case(i,j))
        print L
        #print i,(i+1+i%2)**2,L

# MAIN
# 71328803586048 = 2^27 . 3^12
def main():
    X = 71328803586048
    M = 10**8
    S = 0
    for a in xrange(28):
        for b in xrange(13):
            x = 2**a*3**b
            S = (S+case(x-1,X/x-1))%M
    print S

main()
