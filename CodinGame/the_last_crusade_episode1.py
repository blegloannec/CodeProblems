#!/usr/bin/env python3

N,S,E,W = 0,1,2,3
Dir2Vec = [(0,-1),(0,1),(1,0),(-1,0)]
Tile = [{},
        {N:S, E:S, W:S},
        {E:W, W:E},
        {N:S},
        {N:W, E:S},
        {N:E, W:S},
        {E:W, W:E}, # 6, idem 2
        {N:S, E:S},
        {E:S, W:S},
        {N:S, W:S},
        {N:W},
        {N:E},
        {E:S},
        {W:S}]

Pos2Dir = {'TOP':N, 'LEFT':W, 'RIGHT':E}

def main():
    W,H = map(int,input().split())
    G = [list(map(int,input().split())) for _ in range(H)]
    _ = int(input())  # X exit (useless in ep. 1)
    # game loop
    while True:
        x,y,p = input().split()
        x,y,p = int(x),int(y),Pos2Dir[p]
        dx,dy = Dir2Vec[Tile[G[y][x]][p]]
        print(x+dx,y+dy)

main()
