#!/usr/bin/env python3

import sys


# Input
Rule = []
L = sys.stdin.readline().strip()
while L!='':
    Rule.extend(c=='#' for c in L)
    L = sys.stdin.readline().strip()
assert len(Rule)==1<<9
assert Rule[0]!=Rule[-1]
FLIP = Rule[0]  # the rule flips the background state

S0 = set()
for i,L in enumerate(sys.stdin.readlines()):
    for j,c in enumerate(L.strip()):
        if c=='#':
            S0.add((i,j))
S0 = (S0, 0)

Hist = []  # for anim.

# Cellular Automaton step
#  s0 the default state
#  S0 the set of non-s0-valued cells
def step(S0, s0=0):
    s1 = 1^s0
    S = set()  # new state
    V = set()  # neighborhood of S0 without S0
    for i,j in S0:
        r = 0
        for vi in range(i-1,i+2):
            for vj in range(j-1,j+2):
                r <<= 1
                if (vi,vj) in S0:
                    r |= s1
                else:
                    r |= s0
                    V.add((vi,vj))
        if FLIP^s0^Rule[r]:
            S.add((i,j))
    for i,j in V:
        r = 0
        for vi in range(i-1,i+2):
            for vj in range(j-1,j+2):
                r <<= 1
                if (vi,vj) in S0:
                    r |= s1
                else:
                    r |= s0
        if FLIP^s0^Rule[r]:
            S.add((i,j))
    return (S, FLIP^s0)

def steps(S, n):
    Hist.append(S)
    for _ in range(n):
        S = step(*S)
        Hist.append(S)
    return S


#print(len(steps(S0, 2)[0]))  # Part 1
print(len(steps(S0,50)[0]))  # Part 2


# Anim.
import subprocess
from PIL import Image
TMPDIR = '/tmp/aoc21anim20'

imin = min(min(i for i,_ in S) for S,_ in Hist)
imax = max(max(i for i,_ in S) for S,_ in Hist)
jmin = min(min(j for _,j in S) for S,_ in Hist)
jmax = max(max(j for _,j in S) for S,_ in Hist)
W = jmax-jmin+1
H = imax-imin+1

def make_frame(S):
    Img = Image.new('1', (W,H))
    Pix = Img.load()
    for i,j in S:
        Pix[j-jmin, i-imin] = 1
    return Img

def make_anim(A=2):
    subprocess.run(('mkdir', TMPDIR))
    # range step = 1 -> every step, flipping colors
    #              2 -> every 2 steps, actual colors
    for t in range(0, len(Hist), 1):
        Img = make_frame(Hist[t][0])
        Img.resize((A*W,A*H)).save(f'{TMPDIR}/frame{t:03d}.gif')
    subprocess.run(f'gifsicle -O3 -l -d10 {TMPDIR}/frame*.gif > anim20.gif', shell=True)
    subprocess.run(('rm', '-rf', TMPDIR))

make_anim()
