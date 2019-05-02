#!/usr/bin/env python3

# partial solution code to draw energy paths (for cover)

size = lambda I: (len(I[0]),len(I))
range_clamp = lambda A,a,b,B: range(max(a,A),min(b,B))

def energy(I, x, y):
    return   (abs(I[y][x+1]-I[y][x-1]) if 0<x<len(I[0])-1 else 0)  \
           + (abs(I[y+1][x]-I[y-1][x]) if 0<y<len(I)-1    else 0)

def energy_img(I):
    W,H = size(I)
    E = [[energy(I,x,y) for x in range(W)] for y in range(H)]
    for y in range(H-2,-1,-1):
        for x in range(W):
            E[y][x] += min(E[y+1][x0] for x0 in range_clamp(0,x-1,x+2,W))
    return E

def pgm(I):
    W,H = size(I)
    Imax = max(max(L) for L in I)
    O = ['P2', '%d %d'%(W,H), str(Imax)]
    for y in range(H):
        O.append(' '.join(map(str,I[y])))
    return '\n'.join(O)

if __name__=='__main__':
    assert input()=='P2'
    W,H = map(int,input().split())
    #V = int(input().split()[1])
    assert input()=='255'
    I = [list(map(int,input().split())) for _ in range(H)]
    print(pgm(energy_img(I)))
