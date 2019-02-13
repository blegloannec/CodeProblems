#!/usr/bin/env python3

def pos2coord(P):
    return (ord(P[0])-ord('a'), int(P[1])-1)

def coord2pos(x,y):
    return '%s%d' % (chr(x+ord('a')),y+1)

if __name__=='__main__':
    rook_pos = input()
    Rx,Ry = pos2coord(rook_pos)
    count = int(input())
    Board = [[-1]*8 for _ in range(8)]
    for _ in range(count):
        color,pos = input().split()
        x,y  = pos2coord(pos)
        Board[x][y] = int(color)
    Pos = []
    for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        x,y = Rx+dx,Ry+dy
        while 0<=x<8 and 0<=y<8 and Board[x][y]!=0:
            if Board[x][y]==1:
                Pos.append('R%sx%s' % (rook_pos,coord2pos(x,y)))
                break
            Pos.append('R%s-%s' % (rook_pos,coord2pos(x,y)))
            x,y = x+dx,y+dy
    Pos.sort()
    print('\n'.join(Pos))
