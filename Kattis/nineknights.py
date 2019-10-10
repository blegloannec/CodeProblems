#!/usr/bin/env python3

S = 5
V = ((1,-2),(1,2),(2,1),(2,-1))

def valid(G):
    cnt = 0
    for i in range(S):
        for j in range(S):
            if G[i][j]=='k':
                cnt += 1
                for di,dj in V:
                    vi,vj = i+di,j+dj
                    if 0<=vi<S and 0<=vj<S and G[vi][vj]=='k':
                        return False
    return cnt==9

G = [input() for _ in range(S)]
print('valid' if valid(G) else 'invalid')
