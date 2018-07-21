#!/usr/bin/env python

from math import *

def premier(n):
    if n<0 or n%2==0:
        return False
    for i in range(3,int(sqrt(n))+1,2):
        if n%i==0:
            return False
    return True

def problem3():
    n = 600851475143
    s = int(sqrt(n))+1
    if s%2==0:
        s -= 1
    for i in range(s,2,-1):
        if n%i==0 and premier(i):
            print i
            return

problem3()
