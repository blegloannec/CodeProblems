#!/usr/bin/env python3

import sys
from collections import deque

# Boring BFS as usual with that kind of pb...

def P(x,y):
    return 4*x+y

def iP(p):
    return (p//4,p%4)

D = ['LEFT','RIGHT','UP','DOWN']
# L,R,U,D
Move = [{'W':'B', 'E':'T', 'N':'N', 'S':'S', 'T':'W', 'B':'E'},
        {'W':'T', 'E':'B', 'N':'N', 'S':'S', 'T':'E', 'B':'W'},
        {'W':'W', 'E':'E', 'N':'B', 'S':'T', 'T':'N', 'B':'S'},
        {'W':'W', 'E':'E', 'N':'T', 'S':'B', 'T':'S', 'B':'N'}]

class Config:
    def __init__(self,T,p):
        self.T = T
        self.C = [iP(p)]
        self.dfs(*iP(p))

    def dfs(self,x,y):
        for (vx,vy) in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
            if 0<=vx<4 and 0<=vy<4 and self.T[P(vx,vy)]!=None and (vx,vy) not in self.C:
                self.C.append((vx,vy))
                self.dfs(vx,vy)

    def win(self):
        return len(self.C)==N and all(self.T[P(x,y)][0] in ['T','I'] for (x,y) in self.C)

    # we should remove the last-minute-added ids from the key
    # as they are not actually relevant (we can "identify" configs up to a permutation of the ids)
    # yet do we care for such small inputs?...
    def key(self):
        return (self.T,min(self.C))

    def next(self):
        for (x,y) in self.C:
            if self.T[P(x,y)][0]!='I':
                V = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
                for m in range(4):
                    vx,vy = V[m]
                    if 0<=vx<4 and 0<=vy<4 and self.T[P(vx,vy)]==None:
                        X = list(self.T)
                        d,did = X[P(x,y)]
                        X[P(vx,vy)] = (Move[m][d],did)
                        X[P(x,y)] = None
                        C = Config(tuple(X),P(vx,vy))
                        yield (C,did,m)

def bfs(C0):
    global pred
    pred = {}
    Q = deque([(C0,None,None)])
    pred[C0.key()] = None
    while Q:
        C,_,_ = Q.popleft()
        for V in C.next():
            K = V[0].key()
            if K not in pred:
                pred[K] = (C,V[1],V[2])
                if V[0].win():
                    return V[0]
                Q.append(V)

def main():
    global N
    N = int(sys.stdin.readline())
    X = [None for _ in range(16)]
    for i in range(N):
        x,y,d = sys.stdin.readline().split()
        x,y = int(x),int(y)
        if i==0:
            x0,y0 = x,y
        # last minute dirty hack to keep the die id as
        # required in the output (questionable pb design)...
        X[P(x,y)] = (d[0],i)
    C0 = Config(tuple(X),P(x0,y0))
    C = bfs(C0)
    K = C.key()
    Sol = []
    while pred[K]!=None:
        C,did,m = pred[K]
        K = C.key()
        Sol.append((did,m))
    for (did,m) in reversed(Sol):
        print(did,D[m])

main()
