#!/usr/bin/env python3

# inspired by https://open.kattis.com/problems/knightsfen

from collections import deque
import random
random.seed(55)

# 123        012
# 456        345
# 78.        678
# 1672.438   05618327

def bfs():
    V = ((-1,-2),(-2,-1),(1,-2),(-2,1),(1,2),(2,1),(-1,2),(2,-1))
    C0 = (1,2,3,4,5,6,7,8,0)
    Dist = {C0: 0}
    Q = deque([C0])
    while Q:
        C = Q.popleft()
        p0 = C.index(0)
        i,j = divmod(p0,3)
        for vi,vj in V:
            if 0<=i+vi<3 and 0<=j+vj<3:
                D = list(C)
                p1 = 3*(i+vi) + j+vj
                D[p0],D[p1] = D[p1],D[p0]
                D = tuple(D)
                if D not in Dist:
                    Dist[D] = Dist[C] + 1
                    Q.append(D)
    return Dist

Dist = bfs()

def dist(C):
    if C[4]!='5':
        return -1
    P = (0,5,6,1,8,3,2,7)
    S = [C[i] for i in P]
    i0 = S.index('.')
    S.pop(i0)
    i1 = S.index('1')
    if ''.join(S[i1:]+S[:i1])!='1672438':
        return -1
    if i1==0:
        return abs(i0-4)
    left  =   i0 + (6-i1)*8 + 4
    right = 7-i0 + (i1-1)*8 + 5
    return min(left,right)

Modes = ('', 'force_possible', 'force_center_5', 'force_center_.')
def rand_grid(mode=''):
    if mode=='force_possible':
        B = random.choice(list(Dist.keys()))
        B = ['.' if c==0 else str(c) for c in B]
    else:
        B = list('.12345678')
        random.shuffle(B)
        if mode=='force_center_5':
            i5 = B.index('5')
            B[i5], B[4] = B[4], B[i5]
        elif mode=='force_center_.':
            i0 = B.index('.')
            B[i0], B[4] = B[4], B[i0]
    return '\n'.join(''.join(B[i:i+3]) for i in range(0,9,3))

def gen():
    cases = (0,1,3,2,1,2,1,2,1,2,2,1)
    for i in range(len(cases)):
        mode = Modes[cases[i]]
        for title in ('Test','Validator'):
            d = 0
            while 0<=d<3:
                G = rand_grid(mode)
                C = tuple(0 if c=='.' else int(c) for c in G.replace('\n',''))
                d = -1 if C not in Dist else Dist[C]
            print('{} {}'.format(title, i+2))
            print(G)
            print(d)
            print()

gen()
