#!/usr/bin/env python

import sys,re

I0 = re.compile('rect ([0-9]+)x([0-9]+)')
I1 = re.compile('rotate row y=([0-9]+) by (-?[0-9]+)')
I2 = re.compile('rotate column x=([0-9]+) by (-?[0-9]+)')

W,H = 50,6
S = [[False for _ in xrange(W)] for _ in xrange(H)]
P = [L.strip() for L in sys.stdin.readlines()]

# naive simulation
def simu(P):
    lit = 0
    for I in P:
        O = I0.match(I)
        if O!=None:
            for i in xrange(int(O.group(2))):
                for j in xrange(int(O.group(1))):
                    if not S[i][j]:
                        S[i][j] = True
                        lit += 1
        else:
            O = I1.match(I)
            if O!=None:
                i,d = int(O.group(1)),int(O.group(2))
                S[i] = [S[i][(j-d)%W] for j in xrange(W)]
            else:
                O = I2.match(I)
                j,d = int(O.group(1)),int(O.group(2))
                C0 = [S[(i-d)%H][j] for i in xrange(H)]
                for i in xrange(H):
                    S[i][j] = C0[i]
    return lit

print simu(P)
for L in S:
    print ''.join(map((lambda x: '#' if x else ' '),L))
