#!/usr/bin/env python3

Options = (('J',600,0), ('H',1200,1), ('C',2100,5))

if __name__=='__main__':
    L = int(input())
    Water = int(input())
    R = len(Options)-1
    while True:
        N = int(input())
        F = [tuple(map(int,input().split())) for _ in range(N)]
        while Options[R][1] > Water:
            R -= 1
        code,cost,thresh = Options[R]
        move = None
        while move is None:
            for x in range(L-R):
                for y in range(L-R):
                    cnt = sum(1 for a,b in F if 0<=a-x<=R and 0<=b-y<=R)
                    if cnt > thresh:
                        thresh, move = cnt, (x,y)
            if move is None:
                R -= 1
                code,cost,thresh = Options[R]
        print(code, *move)
        Water -= cost
