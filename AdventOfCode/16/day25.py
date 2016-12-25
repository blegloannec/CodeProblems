#!/usr/bin/env python

import sys

# no toggle in the input code for that problem
#toggle = {'inc':'dec','dec':'inc','tgl':'inc','jnz':'cpy','cpy':'jnz'}

def is_reg(s):
    return (len(s)==1 and ord('a')<=ord(s)<=ord('d'))

def reg_i(s):
    return ord(s)-ord('a')

def simu(R,P):
    #P = [I[:] for I in P] # local copy, useless as no toggles
    i = 0
    O = [] # output
    S = set() # seen states
    while 0<=i<len(P):
        # as there is no toggle, a state of the program is perfectly
        # determined by the current instruction and registers
        s = (i,tuple(R))
        if s in S: # loop detected
            break
        S.add(s)
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
                i += R[reg_i(I[2])] if is_reg(I[2]) else int(I[2])
            else:
                i += 1
        # no toggle in the input code for that problem
        #elif I[0]=='tgl' and len(I)==2:
        #    j = i+(R[reg_i(I[1])] if is_reg(I[1]) else int(I[1]))
        #    if 0<=j<len(P):
        #        P[j][0] = toggle[P[j][0]]
        #    i += 1
        elif I[0]=='out' and len(I)==2:
            O.append(R[reg_i(I[1])] if is_reg(I[1]) else int(I[1]))
            i += 1
        else: # invalid instruction skipped
            i += 1
    return O

# Part One
def experimental():
    P = [L.split() for L in sys.stdin.readlines()]
    a = 1
    while True:
        O = simu([a,0,0,0],P)
        # we assume that the output will be repeated periodically
        # (which is the case) and not just ultimately-periodically
        if len(O)%2==0 and all(O[i]==i%2 for i in xrange(len(O))):
            return a
        a += 1

print experimental()

# If we analyse the input code, we see that it adds 14*182
# (constants in the code, probably specific to each input file)
# and then loops computing and outputting the bits of that number.
# To generate a proper signal, we must find the first x = a + 14*182,
# with a>0 the required input, of the form 101010...10 in binary.

def solution(n):
    x = 2
    while x<=n:
        x = 4*x+2
    return x-n

print solution(14*182)
