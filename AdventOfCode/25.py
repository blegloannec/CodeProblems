#!/usr/bin/env python

def num(r,c):
    return c+(r+c)*(r+c+1)/2

def calcul(n):
    u = 20151125
    for i in range(n):
        u = (u*252533)%33554393
    return u

for i in range(5):
    for j in range(5):
        print calcul(num(i,j)),
    print

print calcul(num(2978-1,3083-1))
