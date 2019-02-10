#!/usr/bin/env python3

Dirs = [(1,1,0,'|'),(2,-1,0,'|'),(4,0,1,'-'),(8,0,-1,'-')]  # first = bitmask

def solve():
    Cell = []
    for x in range(H):
        for y in range(W):
            opt = 0
            for d,dx,dy,_ in Dirs:
                if 0<=x+2*dx<H and 0<=y+2*dy<W and G[x+dx][y+dy]=='.':
                    opt |= d
            if opt:
                Cell.append((x,y,opt))
    Cell.sort(key=(lambda C: (int(G[C[0]][C[1]]=='.'),C[2])))
    Sol = [['.']*W for _ in range(H)]
    assert backtrack(Cell,Sol)
    return Sol

def backtrack(Cell,Sol,i=0,n=0):
    if i==len(Cell):
        return n==N
    x,y,opt = Cell[i]
    if n==N and G[x][y]=='.':
        return True
    if Sol[x][y]!='.':
        return backtrack(Cell,Sol,i+1,n)
    for d,dx,dy,c in Dirs:
        if opt&d and Sol[x+dx][y+dy]=='.' and Sol[x+2*dx][y+2*dy]=='.':
            Sol[x][y],Sol[x+dx][y+dy],Sol[x+2*dx][y+2*dy] = 'o',c,'o'
            if backtrack(Cell,Sol,i+1,n+1):
                return True
            Sol[x][y] = Sol[x+dx][y+dy] = Sol[x+2*dx][y+2*dy] = '.'
    if G[x][y]=='.' and backtrack(Cell,Sol,i+1,n):
        return True
    return False

if __name__=='__main__':
    N = int(input())
    H,W = map(int,input().split())
    G = [input() for _ in range(H)]
    Sol = solve()
    print('\n'.join(''.join(L) for L in Sol))
