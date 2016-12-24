#!/usr/bin/env python

import sys

R = [7,0,0,0]

toggle = {'inc':'dec','dec':'inc','tgl':'inc','jnz':'cpy','cpy':'jnz'}

def is_reg(s):
    return (len(s)==1 and ord('a')<=ord(s)<=ord('d'))

def reg_i(s):
    return ord(s)-ord('a')

def simu(P):
    P = [I[:] for I in P] # local copy
    i = 0
    while 0<=i<len(P):
        I = P[i]
        if I[0]=='cpy' and len(I)==3:
            R[reg_i(I[2])] = R[reg_i(I[1])] if is_reg(I[1]) else int(I[1])
            i += 1
        elif I[0]=='inc' and len(I)==2:
            R[reg_i(I[1])] += 1
            i += 1
        elif I[0]=='dec' and len(I)==2:
            R[reg_i(I[1])] -= 1
            i += 1
        elif I[0]=='jnz' and len(I)==3:
            if (R[reg_i(I[1])] if is_reg(I[1]) else int(I[1]))!=0:
                # new stuff: jnz can have accept a register as shift
                # (it was never the case on day 12)
                i += R[reg_i(I[2])] if is_reg(I[2]) else int(I[2])
            else:
                i += 1
        elif I[0]=='tgl' and len(I)==2:
            j = i+(R[reg_i(I[1])] if is_reg(I[1]) else int(I[1]))
            if 0<=j<len(P):
                P[j][0] = toggle[P[j][0]]
            i += 1
        else: # invalid instruction skipped
            i += 1

# Part One
P = [L.split() for L in sys.stdin.readlines()]
simu(P)
print R[0]

# Part Two (naive simulation in ~ 1 min 40 with pypy, closed formula below)
#R = [12,0,0,0]
#simu(P)
#print R[0]

# If we analyse the input code, we see that it can be split in two parts.
# The first one goes until "tgl c; cpy -16 c; jnz 1 c" and
# computes a0*(a0-1), a0*(a0-1)*(a0-2), etc, in a
# and 2*(a0-2), 2*(a0-3), 2*(a0-4), etc, in c (and b = c/2)
# It loops until c = 2, at that point it toggles the jnz into cpy, so
# that we move for the first time to the second part of the code where
# the following * instructions have been toggled:
# *jnz -> cpy 1 c (toggled at c = 2)
# cpy 72 c
# *jnz -> cpy 77 d (toggled at c = 4)
# inc a
# *inc -> dec d (toggled at c = 6)
# jnz d -2
# *inc -> dec c (toggled at c = 8)
# jnz c -5
# and we see that this simply adds 72*77 to a
# so that the answer is always a0! + 5544
# NB: this analysis only works for a0 >= 6 for the 4 toggles
# to occur (this requires 2*(a0-2)>=8); we also guess that only the
# constants 72 and 77 are changed in the different input files.

def formula(a):
    return reduce(lambda x,y: x*y, xrange(2,a+1)) + 72*77

print formula(12)
