#!/usr/bin/env python3

import sys
from heapq import *


# Config. management
def enc_conf(H,R):
    return '|'.join((H,R[0],R[1],R[2],R[3]))

def final_enc(c):
    return c.endswith('||||')

def dec_conf(S):
    H,RA,RB,RC,RD = S.split('|')
    return (H,[RA,RB,RC,RD])

def conf_succ(c):
    H,R = dec_conf(c)
    # moving from hallway to final room
    for j in range(len(H)):
        if 'A'<=H[j]<='D':
            a = ord(H[j])-ord('A')
            if R[a]=='.'*len(R[a]):
                ja = 2*a+2
                free =   all(H[ji] in '._' for ji in range(j+1,ja+1)) if j<ja \
                    else all(H[ji] in '._' for ji in range(ja,j))
                if free:  # possible move
                    H1 = H[:j]+'.'+H[j+1:]
                    R1 = R.copy()
                    R1[a] = R1[a][:-1]  # "pop" final pos.
                    cost = 10**a * (len(R[a])+abs(ja-j))
                    move = f'h{j}|{a}{len(R1[a])}'
                    yield (cost, enc_conf(H1,R1), move)
    # moving from initial room to hallway
    for k in range(4):
        for i in range(len(R[k])):
            if R[k][i]!='.':
                for j in range(len(H)):
                    if H[j]=='.':
                        jk = 2*k+2
                        free =   all(H[ji] in '._' for ji in range(j+1,jk+1)) if j<jk \
                            else all(H[ji] in '._' for ji in range(jk,j))
                        if free:  # possible move
                            H1 = H[:j]+R[k][i]+H[j+1:]
                            R1 = R.copy()
                            R1[k] = R[k][:i]+'.'+R[k][i+1:]
                            a = ord(R[k][i])-ord('A')
                            cost = 10**a * (i+1+abs(j-jk))
                            move = f'{k}{i}|h{j}'
                            yield (cost, enc_conf(H1,R1), move)
                break


# Pathfinding
def dijkstra(c0):
    Dist = {c0: 0}
    Pred = {}
    Q = [(0,c0)]
    while Q:
        d,c = heappop(Q)
        if final_enc(c):
            break
        if d>Dist[c]:
            continue
        for w,c1,m in conf_succ(c):
            if c1 not in Dist or Dist[c1]>d+w:
                Dist[c1] = d+w
                Pred[c1] = (c,m)
                heappush(Q, (Dist[c1],c1))
    Path = []
    while c!=c0:
        cpred,m = Pred[c]
        Path.append((c,m))
        c = cpred
    #Path.append(c0)
    Path.reverse()
    return (d, Path)


# Input & MAIN
I = sys.stdin.readlines()

def parse_conf():
    H = list(I[1][1:-2])
    for k in range(4):
        H[2*k+2] = '_'
    H = ''.join(H)
    R = [''.join(I[i][2*k+3] for i in range(2,len(I)-1)) for k in range(4)]
    R = [S.rstrip(a) for S,a in zip(R,'ABCD')]  # remove already final positions
    return enc_conf(H,R)

dist, Path = dijkstra(parse_conf())
print(dist)


# Animated GIF (dirty...)
from PIL import Image
import subprocess
TMPDIR = '/tmp/aoc21anim23'
subprocess.run(('mkdir', TMPDIR))

Color = {'A':(255,127,80),'B': (32,178,170),'C':(72,61,150),'D':(219,112,147),
         '.': (255,255,255), '#': (50,50,50)}

H = len(I)
RH = H-3
W = len(I[0])-1
H += 2
W += 2
BackImg = Image.new('RGB', (W,H), Color['.'])
BackPix = BackImg.load()
for i in range(len(I)):
    for j in range(len(I[i])-1):
        if I[i][j] in Color:
            BackPix[j+1,i+1] = Color[I[i][j]]

ft = 0
def save_frame(Img):
    global ft
    Img.resize((30*W,40*H),Image.NEAREST).save(f'{TMPDIR}/frame{ft:04d}.gif')
    ft += 1

def make_move_frames(conf, move):
    H,R = dec_conf(conf)
    Img = BackImg.copy()
    Pix = Img.load()
    for j in range(len(H)):
        if H[j] not in '._':
            Pix[j+1+1,1+1] = Color[H[j]]
    for a in range(4):
        R[a] = R[a].ljust(RH, 'ABCD'[a])
        for i in range(RH):
            Pix[3+2*a+1,2+i+1] = Color[R[a][i]]
    p1,p2 = move.split('|')
    if p1[0]=='h':
        x1 = int(p1[1:])+1
        x2 = 3+2*int(p2[0])
        y2 = 2+int(p2[1])
        col = Pix[x2+1,y2+1]
        Pix[x2+1,y2+1] = Color['.']
        rx = range(x1,x2+1) if x1<x2 else range(x1,x2-1,-1)
        for x in rx:
            Pix[x+1,1+1] = col
            save_frame(Img)
            Pix[x+1,1+1] = Color['.']
        for y in range(1, y2+1):
            Pix[x2+1,y+1] = col
            save_frame(Img)
            Pix[x2+1,y+1] = Color['.']
    else:
        x1 = 3+2*int(p1[0])
        y1 = 2+int(p1[1])
        x2 = int(p2[1:])+1
        col = Pix[x2+1,1+1]
        Pix[x2+1,1+1] = Color['.']
        for y in range(y1,0,-1):
            Pix[x1+1,y+1] = col
            save_frame(Img)
            Pix[x1+1,y+1] = Color['.']
        rx = range(x1,x2+1) if x1<x2 else range(x1,x2-1,-1)
        for x in rx:
            Pix[x+1,1+1] = col
            save_frame(Img)
            Pix[x+1,1+1] = Color['.']

for conf,move in Path:
    make_move_frames(conf, move)

subprocess.run(f'gifsicle -O3 -d10 -l {TMPDIR}/frame*.gif > anim23.gif', shell=True)
subprocess.run(('rm', '-rf', TMPDIR))
