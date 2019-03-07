#!/usr/bin/env python3

S = 8

def sandwitch(dx,dy):
    i, j, k = x+dx, y+dy, 0
    while 0<=i<S and 0<=j<S and G[i][j]!='-':
        if G[i][j]==color:
            return k
        i, j, k = i+dx, j+dy, k+1
    return 0

if __name__=='__main__':
    G = [input() for _ in range(S)]
    color, square = input().split()
    y, x = ord(square[0])-ord('a'), ord(square[1])-ord('1')
    if G[x][y]!='-':
        print('NOPE')
    else:
        s = 0
        for dx in range(-1,2):
            for dy in range(-1,2):
                if not dx==dy==0:
                    s += sandwitch(dx,dy)
        if s==0:
            print('NULL')
        else:
            W, B = sum(L.count('W') for L in G), sum(L.count('B') for L in G)
            W, B = (W-s,B+s+1) if color=='B' else (W+s+1,B-s)
            print(W,B)
