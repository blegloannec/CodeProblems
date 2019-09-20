#!/usr/bin/env python3

import sys, os, random
random.seed(42)

def gen1(N, S1, S2=None):
    if S2 is None:
        S2 = S1
    P = set()
    while len(P)<N:
        P.add((random.randint(0,S1-1),random.randint(0,S2-1)))
    return sorted(P)

def gen2(S, p):
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

if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1] in ('clear','clean'):
        os.system('rm -f case_* cover_in')
        sys.exit()
    for n in [5,50,100,500,1000,1500,1750]:
        p = 0.5
        s = int((n/p)**0.5)
        write_case('case_%04d_1'%n, gen1(n,s))
        write_case('case_%04d_2'%n, gen2(s,p))
    random.seed(227)
    write_case('cover_in', gen1(50,19,10))
