#!/usr/bin/env python3

import numpy as np

Chars = ['V','G','Z']

def path(x,y,dx,dy):
    A,B = [],[]  # cells before and after the first mirror
    reflected = False
    while 0<=x<Size and 0<=y<Size:
        if Map[x][y]=='.':
            (B if reflected else A).append((x,y))
        elif Map[x][y]=='/':
            dx,dy = -dy,-dx
            reflected = True
        else:  # \
            dx,dy = dy,dx
            reflected = True
        x,y = x+dx,y+dy
    return A,B

def build_and_solve_system():
    global Target, VarVec, VarOrder, CurrVec, CurrCount, Sol
    Target = np.array(Top + Bottom + Left + Right)
    Eq  = [path(0,i,1,0) for i in range(Size)]        # Top
    Eq += [path(Size-1,i,-1,0) for i in range(Size)]  # Bottom
    Eq += [path(i,0,0,1) for i in range(Size)]        # Left
    Eq += [path(i,Size-1,0,-1) for i in range(Size)]  # Right
    EqSize = len(Eq)
    VarVec = [[np.zeros((EqSize,), dtype=int) for _ in range(VarCount)] for _ in range(2)]
    for i,(A,B) in enumerate(Eq):
        for p in A:
            VarVec[0][VarIdx[p]][i] += 1                       # Vampire coeff
        for p in B:
            VarVec[1][VarIdx[p]][i] += 1                       # Ghost coeff
    VarVec.append([v+g for v,g in zip(VarVec[0],VarVec[1])])   # Zombie coeffs
    VarOrder = sorted(range(VarCount), key=(lambda v: -np.sum(VarVec[2][v])))
    CurrVec = np.zeros((EqSize,), dtype=int)
    CurrCount = [0]*3
    Sol = [None]*VarCount
    assert backtrack()
    return Sol

def backtrack(i=0):
    global CurrVec
    if i==VarCount:
        return CurrCount==Count and (CurrVec==Target).all()
    v = VarOrder[i]
    for t in range(2,-1,-1):
        if CurrCount[t]+1<=Count[t] and (CurrVec+VarVec[t][v]<=Target).all():
            CurrCount[t] += 1
            CurrVec += VarVec[t][v]
            Sol[v] = t
            if backtrack(i+1):
                return True
            CurrVec -= VarVec[t][v]
            CurrCount[t] -= 1
    return False

if __name__=='__main__':
    Count = list(map(int,input().split()))
    Count[1],Count[2] = Count[2],Count[1]  # order Vampire, Ghost, Zombie
    Size = int(input())
    Top = list(map(int,input().split()))
    Bottom = list(map(int,input().split()))
    Left = list(map(int,input().split()))
    Right = list(map(int,input().split()))
    Map = [list(input()) for _ in range(Size)]
    Cells = [(i,j) for i in range(Size) for j in range(Size) if Map[i][j]=='.']
    VarCount = len(Cells)
    VarIdx = {P:i for i,P in enumerate(Cells)}
    Sol = build_and_solve_system()
    for (x,y),t in zip(Cells,Sol):
        Map[x][y] = Chars[t]
    print('\n'.join(''.join(L) for L in Map))
