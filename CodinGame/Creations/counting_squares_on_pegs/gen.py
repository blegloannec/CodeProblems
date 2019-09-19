#!/usr/bin/env python3

import random
random.seed(42)

def gen1(N,S):
    P = set()
    while len(P)<N:
        P.add((random.randint(0,S-1),random.randint(0,S-1)))
    return sorted(P)

def gen2(S,p):
    P = []
    for i in range(S):
        for j in range(S):
            if random.random()<p:
                P.append((i,j))
    return P

def write_case(fname,P):
    f = open(fname,'w')
    f.write('%d\n' % len(P))
    for p in P:
        f.write('%d %d\n' % p)
    f.close()

for n in [5,50,100,500,1000,1500,1750]:
    p = 0.5
    s = int((n/p)**0.5)
    write_case('case_%04d_1'%n, gen1(n,s))
    write_case('case_%04d_2'%n, gen2(s,p))
