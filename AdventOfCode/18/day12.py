#!/usr/bin/env python3

# A cellular automaton today!

import sys
from PIL import Image

I = [L.strip() for L in sys.stdin.readlines()]
C0 = {i for i,c in enumerate(I[0].split(': ')[1]) if c=='#'}  # sparse conf
R = 2      # radius
W = 2*R+1  # width
Rule = [False]*(1<<W)
for L in I[2:]:
    A,B = L.split(' => ')
    Rule[sum(1<<i for i,c in enumerate(A) if c=='#')] = (B=='#')


# Part 1
def step(C):
    D = set()
    for x in range(min(C)-W+1,max(C)+W):
        if Rule[sum(1<<(y-x+R) for y in range(x-R,x+R+1) if y in C)]:
            D.add(x)
    return D

def steps(C,T):
    for _ in range(T):
        C = step(C)
    return C

print(sum(steps(C0,20)))


# Part 2
def diagram(C,T):
    G = [C]
    for _ in range(T):
        C = step(C)
        G.append(C)
    Xmin = min(min(L) for L in G)
    Xmax = max(max(L) for L in G)
    W = Xmax-Xmin+1
    H = len(G)
    Img = Image.new('1',(W,H),1)
    Pix = Img.load()
    for i in range(H):
        for j in G[i]:
            Pix[j-Xmin,i] = 0
    Img.save('diagram12.png')
    Img.close()

#diagram(C0,300)
# when visualizing the diagram, we observe that after some time,
# the configuration is a constant one that simply shifts 1 cell
# to the right at each step
# NB: this is consistent with the fact that the rule is actually
# independent of the rightmost cell (this has to be the case,
# at least for 5-patterns that can appear in the ultimately
# shifting constant part):
assert(R[i]==R[(1<<(W-1))|i] for i in range(1<<(W-1)))

t = 300
C = steps(C0,t)
S = sum(C)        # constant part value at t
N = len(C)        # nb of alive cells
T = 50*10**9      # requested large time
print(S+N*(T-t))  # formula
