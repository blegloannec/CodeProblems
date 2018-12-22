#!/usr/bin/env python3

import sys

I = [L.strip().split() for L in sys.stdin.readlines()]
Rip = int(I[0][1])
Prog = [(O,int(A),int(B),int(C)) for O,A,B,C in I[1:]]

# /!\ cf input21_analysis for the code dissection that provides the insights
#     leading to the following solution

# Part 1
Rcnt = 6
def is_reg(i):
    return 0<=i<Rcnt

def step(R,ip):
    O,A,B,C = Prog[ip]
    R[Rip] = ip
    assert(is_reg(C))
    if O=='addr':
        assert(is_reg(A) and is_reg(B))
        R[C] = R[A]+R[B]
    elif O=='addi':
        assert(is_reg(A))
        R[C] = R[A]+B
    elif O=='mulr':
        assert(is_reg(A) and is_reg(B))
        R[C] = R[A]*R[B]
    elif O=='muli':
        assert(is_reg(A))
        R[C] = R[A]*B
    elif O=='banr':
        assert(is_reg(A) and is_reg(B))
        R[C] = R[A]&R[B]
    elif O=='bani':
        assert(is_reg(A))
        R[C] = R[A]&B
    elif O=='borr':
        assert(is_reg(A) and is_reg(B))
        R[C] = R[A]|R[B]
    elif O=='bori':
        assert(is_reg(A))
        R[C] = R[A]|B
    elif O=='setr':
        assert(is_reg(A))
        R[C] = R[A]
    elif O=='seti':
        R[C] = A
    elif O=='gtir':
        assert(is_reg(B))
        R[C] = int(A>R[B])
    elif O=='gtri':
        assert(is_reg(A))
        R[C] = int(R[A]>B)
    elif O=='gtrr':
        assert(is_reg(A) and is_reg(B))
        R[C] = int(R[A]>R[B])
    elif O=='eqir':
        assert(is_reg(B))
        R[C] = int(A==R[B])
    elif O=='eqri':
        assert(is_reg(A))
        R[C] = int(R[A]==B)
    elif O=='eqrr':
        assert(is_reg(A) and is_reg(B))
        R[C] = int(R[A]==R[B])

def simu(R):
    ip = 0
    while 0<=ip<len(Prog):
        #print('%02d\t%s %d %d %d\t%s' % (ip,Prog[ip][0],Prog[ip][1],Prog[ip][2],Prog[ip][3],str(R)))
        if ip==28:
            # R0 is never modified and there is only one exit point:
            # 28  eqrr 1 0 5  ~~> R5 = R1==R0
            # 29  addr 5 3 3  ~~> if R1==R0 then jump 31 -- HALT
            # hence the fastest way to halt is to choose R0 = R1 the first
            # time we arrive at ip == 28
            return R[1]
        step(R,ip)
        ip = R[Rip]+1

print(simu([0]*Rcnt))


# Part 2
# the following function (~lines 6-27) computes in a faster way
# the successive values of R1 when we arrive at line 28
# (where it is compared to R0)
def f(R1):
    R2 = R1 | (1<<16)
    R1 = 10605201
    while R2:
        R1 = (((R1+(R2&255))&16777215)*65899)&16777215
        R2 >>= 8
    return R1

# the values for R1 are ultimately periodic, the time-maximizing R0 is then
# the last R1 value before entering the loop
R1 = 0  # line 5
Seen = set()
while R1 not in Seen:
    Seen.add(R1)
    R1,last = f(R1),R1
print(last)
