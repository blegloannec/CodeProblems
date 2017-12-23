#!/usr/bin/env python3

import sys

I = [L.split() for L in sys.stdin.readlines()]

# Part 1 - Simulation
R = [0]*8

def num(x):
    return ord(x)-ord('a')

def val(x):
    return R[num(x)] if 'a'<=x[0]<='z' else int(x)

def simu(P):
    i = 0
    cmul = 0
    while 0<=i<len(P):
        C = P[i][0]
        if C=='set':
            R[num(P[i][1])] = val(P[i][2])
            i += 1
        elif C=='sub':
            R[num(P[i][1])] -= val(P[i][2])
            i += 1
        elif C=='mul':
            R[num(P[i][1])] *= val(P[i][2])
            i += 1
            cmul += 1
        else:  # jnz
            if val(P[i][1])!=0:
                i += val(P[i][2])
            else:
                i += 1
    return cmul

print(simu(I))

# Part 2 - Simulation is not possible anymore, we need to analyze the program.
# Let I = 84 (first line, probably the random part of the input).
# The first 8 lines set the values of b and c:
#  - if a = 0, then b = c = I
#  - if a != 0, then b = 100*I + 100000 and c = b + 17000
# Then the program does the following:
#   while b<=c do
#     f = True
#     for d from 2 to b-1 do
#       for e from 2 to b-1 do
#         if d*e = b then f = False
#     if not f then h += 1
#     b += 17
# So f is set to false iff the current b is not prime.
# Hence h counts the number of non prime (composite) numbers
# between initial b and c by step 17.

def prime(b):  # (sieving would be overkill here)
    if b%2==0:
        return False
    d = 3
    while d*d<=b:
        if b%d==0:
            return False
        d += 2
    return True

def h(I=84):
    b = 100*I+100000
    c = b+17000
    return sum(int(not prime(x)) for x in range(b,c+1,17))

print(h())
