#!/usr/bin/env python

import sys

R = [0,0,0,0]

def is_reg(s):
    return (len(s)==1 and ord('a')<=ord(s)<=ord('d'))

def reg_i(s):
    return ord(s)-ord('a')

def simu(P):
    i = 0
    while 0<=i<len(P):
        I = P[i]
        if I[0]=='cpy':
            R[reg_i(I[2])] = R[reg_i(I[1])] if is_reg(I[1]) else int(I[1])
            i += 1
        elif I[0]=='inc':
            R[reg_i(I[1])] += 1
            i += 1
        elif I[0]=='dec':
            R[reg_i(I[1])] -= 1
            i += 1
        else: # jnz
            if (R[reg_i(I[1])] if is_reg(I[1]) else int(I[1]))!=0:
                i += int(I[2])
            else:
                i += 1

# Part One
P = [L.split() for L in sys.stdin.readlines()]
simu(P)
print R[0]

# Part Two
R = [0,0,1,0]
simu(P)
print R[0]
