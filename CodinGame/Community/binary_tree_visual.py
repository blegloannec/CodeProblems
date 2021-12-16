#!/usr/bin/env python3

class Canvas:
    def __init__(self):
        self.Surf = []
    def __setitem__(self, pos, c):
        i,j = pos
        while len(self.Surf)<=i:
            self.Surf.append([])
        while len(self.Surf[i])<=j:
            self.Surf[i].append(' ')
        self.Surf[i][j] = c
    def __str__(self):
        return '\n'.join(''.join(L) for L in self.Surf)

def traversal(u=0, h=0,w=-1):
    v,l,r = Tree[u]
    if l>=0:
        w = traversal(l, h+4,w)
    w += wcell
    Pos[u] = (h,w)
    if r>=0:
        w = traversal(r, h+4,w)
    # output
    ui,uj = Pos[u]
    for j,c in enumerate(v):
        Out[ui,uj-len(v)+1+j] = c
    if r>=0 or l>=0:
        Out[ui+1,uj] = '|'
        Out[ui+2,uj] = '+'
        if l>=0:
            lj = Pos[l][1]
            for j in range(lj+1,uj):
                Out[ui+2,j] = '-'
            Out[ui+2,lj] = '+'
            Out[ui+3,lj] = '|'
        if r>=0:
            rj = Pos[r][1]
            for j in range(uj+1,rj):
                Out[ui+2,j] = '-'
            Out[ui+2,rj] = '+'
            Out[ui+3,rj] = '|'
    return w

def main():
    global Tree, wcell, Pos, Out
    Tree = []
    N = int(input())
    for _ in range(N):
        v,l,r = input().split()
        Tree.append((v, int(l), int(r)))
    wcell = max(len(v) for v,_,_ in Tree)+1
    Pos = [None]*N
    Out = Canvas()
    traversal()
    print(Out)

main()
