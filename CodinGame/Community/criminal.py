#!/usr/bin/env python3

class RoTable:
    def __init__(self, A):
        self.H = len(A)
        self.W = len(A[0])
        self.A = A
    
    def __getitem__(self, ij):
        i,j = ij
        return self.A[i][j]
    
    def __setitem__(self, ij, x):
        i,j = ij
        self.A[i][j] = x
    
    def rotate(self):
        self.A = [[self.A[i][j] for i in range(self.H)] for j in range(self.W-1,-1,-1)]
        self.H, self.W = self.W, self.H
    
    def __str__(self):
        return '\n'.join(''.join(L) for L in self.A)


if __name__=='__main__':
    H = int(input())
    W = int(input())
    G = RoTable([list(input()) for _ in range(H)])
    cnt = 0
    for c in 'v<^>':
        Yi = None
        for i in range(G.H-1,-1,-1):
            for j in range(G.W):
                if G[i,j]=='Y':
                    Yi,Yj = i,j
                elif G[i,j]==c:
                    if Yi is not None and Yi-i>=abs(Yj-j):
                        if j==Yj:
                            visible = all(G[x,j]=='.' for x in range(i+1,Yi))
                        elif j>Yj:
                            visible = all(G[x,Yj+y] in '.Y' for y in range(j-Yj) for x in range(i+j-Yj-y,Yi-y+1))
                        else:
                            visible = all(G[x,Yj-y] in '.Y' for y in range(Yj-j) for x in range(i+Yj-j-y,Yi-y+1))
                        if visible:
                            cnt += 1
        G.rotate()
    print(cnt)
