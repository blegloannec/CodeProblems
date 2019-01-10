#!/usr/bin/env python3

from collections import deque
from PIL import Image
import os

RE = input().strip()

Dir = {'N':(-1,0),'S':(1,0),'E':(0,1),'W':(0,-1)}

# Even though the problem statement is not absolutely clear about that,
# the input verifies the following property:
# "Regardless of which option is taken, the route continues from the position
#  it is left at after taking those steps."
# I.e. the alternatives/options are detours that all lead to the same cell!
# This makes the exploration much easier.

# Part 1
G = set([(0,0)])
S,E = set(),set()

def parse_same_detours(RE):
    x = y = 0
    P = []
    for c in RE:
        if c=='(':
            P.append((x,y))
        elif c==')':
            P.pop()
        elif c=='|':
            x,y = P[-1]
        else:
            dx,dy = Dir[c]
            if c=='S':
                S.add((x,y))
            elif c=='N':
                S.add((x-1,y))
            elif c=='E':
                E.add((x,y))
            else:
                E.add((x,y-1))
            x += dx
            y += dy
            G.add((x,y))

def neigh(x,y):
    if (x,y) in S:
        yield (x+1,y)
    if (x,y) in E:
        yield (x,y+1)
    if (x-1,y) in S:
        yield (x-1,y)
    if (x,y-1) in E:
        yield (x,y-1)

def bfs():
    u0 = (0,0)
    Dist = {u0: 0}
    Pred = {u0: None}  # only for the picture
    Q = deque([u0])
    while Q:
        u = Q.popleft()
        for v in neigh(*u):
            if v not in Dist:
                Dist[v] = Dist[u] + 1
                Pred[v] = u
                Q.append(v)
    return Dist,Pred

parse_same_detours(RE[1:-1])
Dist,Pred = bfs()
max_dist = max(Dist[u] for u in Dist)
print(max_dist)

# Part 2
print(sum(int(Dist[u]>=1000) for u in Dist))


# Picture for the fun!
def pic():
    X0,X1 = min(x for x,_ in G),max(x for x,_ in G)
    Y0,Y1 = min(y for _,y in G),max(y for _,y in G)
    A = 5
    W,H = A*(Y1-Y0+1)+1,A*(X1-X0+1)+1
    white = (255,255,255)
    Img = Image.new('RGB',(W,H))
    Pix = Img.load()
    Final = []
    for x,y in G:
        col = white
        if Dist[x,y]==max_dist:
            Final.append((x,y))
            col = 255,100,100
        if Dist[x,y]==0:
            col = 100,100,255
        for i in range(1,A):
            for j in range(1,A):
                Pix[A*(y-Y0)+j,A*(x-X0)+i] = col
    for x,y in E:
        for i in range(1,A):
            Pix[A*(y-Y0)+A,A*(x-X0)+i] = white
    for x,y in S:
        for j in range(1,A):
            Pix[A*(y-Y0)+j,A*(x-X0)+A] = white
    Paths = []
    for u in Final:
        P = []
        while u is not None:
            P.append(u)
            u = Pred[u]
        P.reverse()
        Paths.append(P[1:-1])
    step,L = 20,len(Paths[0])
    for t in range(0,L,step):
        dt = 0
        while dt<step and t+dt<L:
            for P in Paths:
                x,y = P[t+dt]
                for i in range(2,A-1):
                    for j in range(2,A-1):
                        Pix[A*(y-Y0)+j,A*(x-X0)+i] = (255,100,100)
            dt += 1
        Img.save('gif20/frame%04d.gif' % t)
    Img.close()
    os.system('convert -loop 0 -delay 10 gif20/*.gif anim20.gif')

#pic()
