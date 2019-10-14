#!/usr/bin/env python3

# How hard can it be? Surprisingly harder than it looks!
# https://stackoverflow.com/a/8778592

from collections import deque
#from PIL import Image

V = ((-1,-2),(-2,-1),(1,-2),(-2,1),(1,2),(2,1),(-1,2),(2,-1))

def bfs(S):
    Dist = [[-1]*S for _ in range(S)]
    Dist[0][0] = 0
    Dist[1][1] = 2
    Q = deque([(0,0)])
    while Q:
        i,j = Q.popleft()
        for di,dj in V:
            vi,vj = i+di,j+dj
            if 0<=vi<S and 0<=vj<S and Dist[vi][vj]<0:
                Dist[vi][vj] = Dist[i][j] + 1
                Q.append((vi,vj))
    return Dist

def formula(x,y):
    x,y = abs(x),abs(y)
    if x<y:
        x,y = y,x
    if (x,y)==(1,0):
        return 3
    if x==y==2:
        return 4
    d = x-y
    return d - 2*((d-y)//3) if y>d else d - 2*((d-y)//4)

def draw_pattern(S):
    Dist = bfs(S)
    dmax = max(max(L) for L in Dist)
    Img = Image.new('L',(S,S))
    Pix = Img.load()
    for i in range(S):
        for j in range(S):
            Pix[i,j] = 255*Dist[i][j]//dmax
    Img.save('out.png')
    Img.close()
    Out = []
    for i in range(S):
        Out.append(' '.join('{:2d}'.format(d) for d in Dist[i]))
        Out.append(' '.join('{:2d}'.format(formula(i,j)) for j in range(S)))
    F = open('out.txt','w')
    F.write('\n'.join(Out))
    F.close()
    Img = Image.new('L',(S,S))
    Pix = Img.load()
    for i in range(S):
        for j in range(S):
            d = abs(i-j)
            Pix[i,j] = 255*(j<d)
    Img.save('out2.png')
    Img.close()

def main():
    while True:
        L = input()
        if L=='END':
            break
        x,y = map(int,L.split())
        print(formula(x,y))

#draw_pattern(25)
main()
