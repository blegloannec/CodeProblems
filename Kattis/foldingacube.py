#!/usr/bin/env python3

#  3
# 4015
#  2

C0 = (0,1,2)
MoveLeft  = lambda C: (C[1], 5-C[0], C[2])
MoveRight = lambda C: (5-C[1], C[0], C[2])
MoveUp    = lambda C: (C[2], C[1], 5-C[0])
MoveDown  = lambda C: (5-C[2], C[1], C[0])

S = 6

def main():
    G = [list(input()) for _ in range(S)]
    i0,j0 = next((i,j) for i in range(S) for j in range(S) if G[i][j]=='#')
    Q = [(i0,j0,C0)]
    Seen = [False]*6
    while Q:  # DFS
        i,j,c = Q.pop()
        Seen[c[0]] = True
        for vi,vj,vc in ((i-1,j,MoveUp(c)),(i+1,j,MoveDown(c)),(i,j-1,MoveLeft(c)),(i,j+1,MoveRight(c))):
            if 0<=vi<S and 0<=vj<S and G[vi][vj]=='#':
                G[vi][vj] = '.'
                Q.append((vi,vj,vc))
    print(('can' if all(Seen) else 'cannot'), 'fold')

main()
