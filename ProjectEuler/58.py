#!/usr/bin/env python

from math import sqrt

def premier(n):
    if n<0 or n%2==0:
        return False
    for i in range(3,int(sqrt(n))+1,2):
        if n%i==0:
            return False
    return True

def problem58():
    n = 7
    nb = 8
    while 10*nb>2*n-1:
        n += 2
        if premier(n*n-(n-1)):
            nb += 1
        if premier(n*n-2*(n-1)):
            nb += 1
        if premier(n*n-3*(n-1)):
            nb += 1
    print n

problem58()
