#!/usr/bin/env python3

H = int(input())
W = int(input())
Dir = input()
G = [input() for _ in range(H)]
try:
    line_x = G[0].index('|')
except:
    line_x = G[0].index('C')
Fish = []
Garbage = float('inf')
for i in range(H):
    obstacles = 0
    for j in range(line_x-1,-1,-1):
        if G[i][j]=='.':
            continue
        elif G[i][j]=='>':
            if obstacles:
                obstacles -= 1
            else:
                Fish.append(line_x-j)
        elif G[i][j]!='<' and Dir=='RIGHT':
            Garbage = min(Garbage, line_x-j)
            break
        else:
            obstacles += 1
    obstacles = 0
    for j in range(line_x+1,W):
        if G[i][j]=='.':
            continue
        elif G[i][j]=='<':
            if obstacles:
                obstacles -= 1
            else:
                Fish.append(j-line_x)
        elif G[i][j]!='>' and Dir=='LEFT':
            Garbage = min(Garbage, j-line_x)
            break
        else:
            obstacles += 1
    if G[i][line_x]=='C':
        break
print(sum(int(f<=Garbage) for f in Fish))
