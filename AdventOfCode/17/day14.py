#!/usr/bin/env python3

# this is basically day 10 + day 12

import day10

I = 'uugsqrei'  # Input

# Part 1
G = []
cpt = 0
for i in range(128):
    h = day10.knot_hash('%s-%d' % (I,i))
    L = bin(int(h,16))[2:].zfill(128)
    G.append(L)
    cpt += L.count('1')
print(cpt)


# Part 2
def dfs(i,j):
    seen[i][j] = True
    for (vi,vj) in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
        if 0<=vi<128 and 0<=vj<128 and G[vi][vj]=='1' and not seen[vi][vj]:
            dfs(vi,vj)

seen =  [[False]*128 for _ in range(128)]
cpt = 0
for i in range(128):
    for j in range(128):
        if G[i][j]=='1' and not seen[i][j]:
            dfs(i,j)
            cpt += 1
print(cpt)
