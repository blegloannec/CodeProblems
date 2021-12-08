#!/usr/bin/env python3

Dir = {'^':(-1,0), 'v':(1,0), '<':(0,-1), '>':(0,1)}

def main():
    W,H = map(int, input().split())
    G = [input() for _ in range(H)]

    # Computing successors
    Succ = [[None]*W for _ in range(H)]
    Pred = [[0]*W for _ in range(H)]
    for i0 in range(H):
        for j0 in range(W):
            if G[i0][j0]!='.':
                di,dj = Dir[G[i0][j0]]
                i = i0+di
                j = j0+dj
                while 0<=i<H and 0<=j<W and G[i][j]=='.':
                    i += di
                    j += dj
                if 0<=i<H and 0<=j<W:
                    Succ[i0][j0] = (i,j)
                    Pred[i][j] += 1

    # Leaf elimination
    Q = [(i,j) for i in range(H) for j in range(W)
         if G[i][j]!='.' and Pred[i][j]==0]
    while Q:
        i,j = Q.pop()
        if Succ[i][j] is not None:
            si,sj = Succ[i][j]
            Pred[si][sj] -= 1
            if Pred[si][sj]==0:
                Q.append((si,sj))

    # Cycles traversal
    cyc = 0
    for i0 in range(H):
        for j0 in range(W):
            if Pred[i0][j0]!=0:
                Pred[i0][j0] = 0      # to mark as seen
                cyc += 1
                i,j = Succ[i0][j0]
                while (i,j)!=(i0,j0):
                    Pred[i][j] = 0    # mark the cycle
                    i,j = Succ[i][j]
    print(cyc)

main()
