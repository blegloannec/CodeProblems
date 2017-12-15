#!/usr/bin/env pypy

A,B = 16807,48271
M = (1<<31)-1
mask = (1<<16)-1

#a0,b0 = 65,8921  # Example
a0,b0 = 289,629  # Input

# Part 1
a,b = a0,b0
cpt = 0
for _ in xrange(40000000):
    a = (A*a)%M
    b = (B*b)%M
    if a&mask==b&mask:
        cpt += 1
print(cpt)

# Part 2
a,b = a0,b0
cpt = 0
for _ in xrange(5000000):
    a = (A*a)%M
    while a&3!=0:
        a = (A*a)%M
    b = (B*b)%M
    while b&7!=0:
        b = (B*b)%M
    if a&mask==b&mask:
        cpt += 1
print(cpt)
