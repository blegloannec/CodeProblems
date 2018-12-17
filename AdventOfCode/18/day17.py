#!/usr/bin/env python3

import sys, re, os
from PIL import Image
sys.setrecursionlimit(10000)

form = re.compile('([xy])=(\d+), ([xy])=(\d+)\.\.(\d+)')
I = []
for L in sys.stdin.readlines():
    ly,y0,_,x0,x1 = form.match(L.strip()).groups()
    y1 = y0
    if ly=='x':
        y0,y1,x0,x1 = x0,x1,y0,y1
    I.append(tuple(map(int,(y0,y1,x0,x1))))

Ymin,Ymax = min(y0 for y0,_,_,_ in I),max(y1 for _,y1,_,_ in I)
Xmin,Xmax = min(x0 for _,_,x0,_ in I),max(x1 for _,_,_,x1 in I)
W,H = Xmax-Xmin+3,Ymax-Ymin+2  # we add 1 column on each side and 1 first line for the spring
X0,Y0 = Xmin-1,Ymin-1
Xspring = 500-X0


# Part 1 & 2
G = [['.']*W for _ in range(H)]
for y0,y1,x0,x1 in I:
    for y in range(y0,y1+1):
        for x in range(x0,x1+1):
            G[y-Y0][x-X0] = '#'

def flow(x=Xspring, y=0):
    assert(G[y][x]=='.')
    G[y][x] = '|'
    if y+1<H:
        if G[y+1][x]=='.':
            flow(x,y+1)
        if G[y+1][x]=='#' or G[y+1][x]=='~':
            rest = 0
            if x>0:
                if G[y][x-1]=='.':
                    rest += flow(x-1,y)
                elif G[y][x-1]=='#':
                    rest += 1
            if x<W:
                if G[y][x+1]=='.':
                    rest += flow(x+1,y)
                elif G[y][x+1]=='#':
                    rest += 1
            if rest==2:
                # blocked on both sides, we (iteratively) mark the | line as ~
                i = x
                while G[y][i]=='|':
                    G[y][i] = '~'
                    i += 1
                i = x-1
                while G[y][i]=='|':
                    G[y][i] = '~'
                    i -= 1
            return rest
    return 0

flow()
#print('\n'.join(''.join(L) for L in G))
print(sum(L.count('|')+L.count('~') for L in G)-1)  # -1 to remove the first line |
print(sum(L.count('~') for L in G))


# GIF output and anim for the fun!
def pic(anim=False):
    Col = {'#':(64,64,64), '~':(150,150,255), '|':(190,190,255)}
    Img = Image.new('RGB',(W,H),(255,255,255))
    Pix = Img.load()
    for i in range(H):
        for j in range(W):
            if G[i][j] in Col:
                Pix[j,i] = Col[G[i][j]]
    Img.resize((2*W,2*H)).save('out17.png')
    if anim:
        assert(H>W)
        for i in range(0,H-W+1,2):
            Img.crop((0,i,W,i+W)).resize((2*W,2*W)).save('gif17/frame%04d.gif' % i)
        os.system('convert -loop 0 -delay 4 gif17/frame*.gif anim17.gif')
    Img.close()

#pic()
