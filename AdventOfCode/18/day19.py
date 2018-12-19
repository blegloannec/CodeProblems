#!/usr/bin/env python3

import sys

I = [L.strip().split() for L in sys.stdin.readlines()]
Rip = int(I[0][1])
Prog = [(O,int(A),int(B),int(C)) for O,A,B,C in I[1:]]


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
        step(R,ip)
        ip = R[Rip]+1

R = [0]*Rcnt
simu(R)
print(R[0])


# Part 2 (cf input19_analysis for a dissection of the input program)
def R5(R0,R4=0,R5=0):
    assert(0<=R0<=1)
    R5 = 11*19*(R5+2)**2 + 22*(R4+2)+16
    if R0==1:
        R5 += (27*28+29)*30*14*32
    return R5

def sum_divisors(n):
    return sum(d for d in range(1,n+1) if n%d==0)

#print(sum_divisors(R5(0)))  # part 1
print(sum_divisors(R5(1)))   # part 2
