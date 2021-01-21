#!/usr/bin/env python3

def captured_groups(col):
    Seen = [[False]*S for _ in range(S)]
    for i in range(S):
        for j in range(S):
            if not Seen[i][j] and Board[i][j]==col:
                Q = [(i,j)]
                Seen[i][j] = True
                liberty = False
                G = []
                while Q:
                    x,y = Q.pop()
                    G.append((x,y))
                    for vx,vy in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                        if 0<=vx<S and 0<=vy<S:
                            if Board[vx][vy]=='.':
                                liberty = True
                            elif Board[vx][vy]==col and not Seen[vx][vy]:
                                Q.append((vx,vy))
                                Seen[vx][vy] = True
                if not liberty:
                    yield G

def main():
    global S, Board
    S = int(input())
    M = int(input())
    Board = [list(input()) for _ in range(S)]
    KO = set()
    valid = True
    prev_bw = None
    for _ in range(M):
        bw,i,j = input().split()
        i = int(i); j = int(j)
        if prev_bw==bw or Board[i][j]!='.':
            valid = False
            break
        prev_bw = bw
        Board[i][j] = bw
        for G in captured_groups('B' if bw=='W' else 'W'):
            for i,j in G:
                Board[i][j] = '.'
        if any(captured_groups(bw)):
            valid = False
            break
        sig = ''.join(''.join(L) for L in Board)
        if sig in KO:
            valid = False
            break
        KO.add(sig)
    print('\n'.join(''.join(L) for L in Board) if valid else 'NOT_VALID')

main()
