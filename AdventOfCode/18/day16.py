#!/usr/bin/env python3

import sys

I = [L.strip() for L in sys.stdin.readlines()]

Samples = []
for i in range(0,len(I),4):
    if I[i]=='':
        Prog = [tuple(map(int,L.split())) for L in I[i+2:]]
        break
    R0 = list(map(int,I[i].split(': ')[1][1:-1].split(', ')))
    Instr = tuple(map(int,I[i+1].split()))
    R1 = list(map(int,I[i+2].split(':  ')[1][1:-1].split(', ')))
    Samples.append((R0,Instr,R1))


# Part 1
def is_reg(i):
    return 0<=i<4

Names = ['addr','addi','mulr','muli','banr','bani','borr','bori','setr','seti','gtir','gtri','gtrr','eqir','eqri','eqrr']
Code2Name = [None]*16

def step(R,Instr):
    O,A,B,C = Instr
    if isinstance(O,int):
        O = Code2Name[O]
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

def simu(R,Prog):
    for Instr in Prog:
        step(R,Instr)

def candidates(R0,Instr,R1):
    for O in Names:
        _,A,B,C = Instr
        R = R0[:]
        try:
            step(R,(O,A,B,C))
            if R==R1:
                yield O
        except:
            pass

part1 = 0
Cand = [set(Names) for _ in range(16)]
for R0,In,R1 in Samples:
    S = set(candidates(R0,In,R1))
    Cand[In[0]] &= S
    if len(S)>=3:
        part1 += 1

print(part1)


# Part 2
Q = [i for i in range(16) if len(Cand[i])==1]
while Q:
    i = Q.pop()
    op = Cand[i].pop()
    Code2Name[i] = op
    for j in range(16):
        if len(Cand[j])>1:
            Cand[j].discard(op)
            if len(Cand[j])==1:
                Q.append(j)

R = [0]*4
simu(R,Prog)
print(R[0])
