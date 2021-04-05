#!/usr/bin/env python3

def main():
    H,W = map(int, input().split())
    G = [input() for _ in range(H)]
    Seen = [[False]*W for _ in range(H)]
    C = 0
    for i0 in range(H):
        for j0 in range(W):
            if G[i0][j0]=='L' and not Seen[i0][j0]:
                C += 1
                Seen[i0][j0] = True
                S = [(i0,j0)]
                while S:
                    i,j = S.pop()
                    for vi,vj in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                        if 0<=vi<H and 0<=vj<W and G[vi][vj] in 'LC' and not Seen[vi][vj]:
                            Seen[vi][vj] = True
                            S.append((vi,vj))
    print(C)

main()
