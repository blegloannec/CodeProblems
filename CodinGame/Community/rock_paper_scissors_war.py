#!/usr/bin/env python3

S = 'RPCLS'
W = [[0,1,0,0,4],
     [1,1,2,3,1],
     [0,2,2,2,4],
     [0,3,2,3,3],
     [4,1,4,3,4]]

def main():
    w, h, n = map(int, input().split())
    G = [list(map(S.index, input())) for _ in range(h)]
    for _ in range(n):
        Gsucc = [[None]*w for _ in range(h)]
        for i in range(h):
            for j in range(w):
                F = []
                for vi,vj in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                    if 0<=vi<h and 0<=vj<w:
                        F.append(W[G[i][j]][G[vi][vj]])
                # F contains at most the current form & the 2 forms it loses against.
                # The rules ensure they cannot form a cycle: One of them is stronger
                # than the 2 others. Hence the winner is uniquely defined.
                while len(F)>1:
                    F.append(W[F.pop()][F.pop()])
                Gsucc[i][j] = F[0]
        G = Gsucc
    print('\n'.join(''.join(S[c] for c in L) for L in G))

main()
