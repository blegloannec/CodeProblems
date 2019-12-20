#!/usr/bin/env python3

import sys, os
from collections import deque
from PIL import Image, ImageDraw

G = [L.rstrip('\n') for L in sys.stdin.readlines()]
H,W = len(G),len(G[0])


# Gif for part 1
def bfs():
    u0 = (x0,y0)
    u1 = (x1,y1)
    Dist = {u0: 0}
    Pred = {u0: None}
    Q = deque([u0])
    while Q:
        x,y = u = Q.popleft()
        if u==u1:
            break
        for vx,vy in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
            if 0<=vx<H and 0<=vy<W and \
               (G[vx][vy]=='.' or ('A'<=G[vx][vy]<='Z' and (vx,vy) in Portal)):
                if 'A'<=G[vx][vy]<='Z':
                    vx,vy = Portal[vx,vy]
                v = (vx,vy)
                if v not in Dist:
                    Dist[v] = Dist[u] + 1
                    Pred[v] = u
                    Q.append(v)
    Path = []
    u = u1
    while u is not None:
        Path.append(u)
        u = Pred[u]
    Path.reverse()
    return Path

Seen = set()
Label = {}
Portal = {}
for i in range(H):
    for j in range(W):
        if 'A'<=G[i][j]<='Z' and (i,j) not in Seen:
            Seen.add((i,j))
            if 'A'<=G[i+1][j]<='Z':
                Seen.add((i+1,j))
                l = G[i][j] + G[i+1][j]
                if i+2<H and G[i+2][j]=='.':
                    if l in Label:
                        (i2,j2),(ii2,jj2) = Label[l]
                        Portal[i+1,j] = (ii2,jj2)
                        Portal[i2,j2] = (i+2,j)
                    else:
                        Label[l] = ((i+1,j),(i+2,j))
                else:
                    assert G[i-1][j]=='.'
                    if l in Label:
                        (i2,j2),(ii2,jj2) = Label[l]
                        Portal[i,j] = (ii2,jj2,)
                        Portal[i2,j2] = (i-1,j)
                    else:
                        Label[l] = ((i,j),(i-1,j))
            else:
                assert 'A'<=G[i][j+1]<='Z'
                Seen.add((i,j+1))
                l = G[i][j] + G[i][j+1]
                if j+2<W and G[i][j+2]=='.':
                    if l in Label:
                        (i2,j2),(ii2,jj2) = Label[l]
                        Portal[i,j+1] = (ii2,jj2)
                        Portal[i2,j2] = (i,j+2)
                    else:
                        Label[l] = ((i,j+1),(i,j+2))
                else:
                    assert G[i][j-1]=='.'
                    if l in Label:
                        (i2,j2),(ii2,jj2) = Label[l]
                        out = 1 if j==W-2 else -1
                        Portal[i,j] = (ii2,jj2)
                        Portal[i2,j2] = (i,j-1)
                    else:
                        Label[l] = ((i,j),(i,j-1))

x0,y0 = Label['AA'][1]
x1,y1 = Label['ZZ'][1]
Path = bfs()

A = 3
Img = Image.new('RGB',(W,H))
Pix = Img.load()
PDest = set(Portal.values())
for y in range(H):
    for x in range(W):
        if (y,x) in PDest:
            Pix[x,y] = (50,50,255)
        elif G[y][x]=='.':
            Pix[x,y] = (220,220,220)
        elif G[y][x]=='#':
            Pix[x,y] = (50,50,50)
Pix[y0,x0] = (255,255,0)
Pix[y1,x1] = (0,255,0)
os.system('mkdir anim20')
f = 0
y0,x0 = Path[0]
for y,x in Path:
    col = Pix[x,y]
    Pix[x,y] = (255,0,0)
    Img.resize((A*W,A*H)).save('anim20/frame%04d.gif' % f)
    f += 1
    Pix[x,y] = col
    if abs(x-x0)+abs(y-y0)>1:
        Img1 = Img.copy()
        Drw = ImageDraw.Draw(Img1)
        Drw.line((x0,y0,x,y), fill=(0,255,255))
        Img1.resize((A*W,A*H)).save('anim20/frame%04d.gif' % f)
        f += 1
        Img1.close()
    x0,y0 = x,y
Img.close()
os.system('convert -loop 0 -delay 3 anim20/*.gif anim20.gif')
os.system('rm -r anim20')
