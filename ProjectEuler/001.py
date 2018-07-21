#!/usr/bin/env python

def problem1():
    s = 0
    for i in range(1000):
        if i%3==0 or i%5==0:
            s += i
    print s

problem1()
