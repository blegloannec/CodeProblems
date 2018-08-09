#!/usr/bin/env python3

Dir = [(1,0),(0,1),(-1,0),(0,-1)]
DirName = {(1,0):'SOUTH', (0,1):'EAST', (-1,0):'NORTH', (0,-1):'WEST'}
CharDir = {'S':(1,0), 'E':(0,1), 'N':(-1,0), 'W':(0,-1)}

def simu():
    T = []
    for i in range(H):
        for j in range(W):
            if G[i][j]=='@':
                X,Y = i,j
            elif G[i][j]=='T':
                T.append((i,j))
    if T:
        T = {T[0]:T[1],T[1]:T[0]}
    D = (1,0)
    inv = breaker = False
    seen = set()
    res = []
    while G[X][Y]!='$':
        state = (X,Y,D,inv,breaker)
        if state in seen:  # loop
            return []
        seen.add(state)
        if G[X][Y] in CharDir:
            D = CharDir[G[X][Y]]
        elif G[X][Y]=='B':
            breaker = not breaker
        elif G[X][Y]=='I':
            inv = not inv
        elif G[X][Y]=='T':
            X,Y = T[X,Y]
        for DX,DY in [D]+(Dir[::-1] if inv else Dir):
            if G[X+DX][Y+DY] not in '#X' or (breaker and G[X+DX][Y+DY]=='X'):
                X += DX
                Y += DY
                D = (DX,DY)
                res.append(D)
                if G[X][Y]=='X':  # broken wall
                    G[X][Y] = ' '
                    seen.clear()  # reset states
                break
    return res

def main():
    global H,W,G
    H,W = [int(i) for i in input().split()]
    G = [list(input()) for _ in range(H)]
    Path = simu()
    if Path:
        for D in Path:
            print(DirName[D])
    else:
        print('LOOP')

main()
