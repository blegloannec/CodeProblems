#!/usr/bin/env python3

# non seulement ce PoW n'a aucune originalite
# mais en plus les conditions au bord ne sont pas precisees...

def next(C):
    w,h = len(C[0]),len(C)
    N = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            v = 0
            for di in range(-1,2):
                for dj in range(-1,2):
                    if (di!=0 or dj!=0) and 0<=i+di<h and 0<=j+dj<w:
                        v += C[i+di][j+dj]
            N[i][j] = int(2<=v<=3) if C[i][j] else int(v==3)
    return N

def main():
    _,h = map(int,input().split())
    C = [list(map(int,input())) for _ in range(h)]
    N = next(C)
    for L in N:
        print(''.join(map(str,L)))

main()
