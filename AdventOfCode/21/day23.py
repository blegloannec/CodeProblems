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
                    yield (cost, enc_conf(H1,R1))
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
                            yield (cost, enc_conf(H1,R1))
                break


# Pathfinding
def dijkstra(c0):
    Dist = {c0: 0}
    Q = [(0,c0)]
    while Q:
        d,c = heappop(Q)
        if final_enc(c):
            return d
        if d>Dist[c]:
            continue
        for w,c1 in conf_succ(c):
            if c1 not in Dist or Dist[c1]>d+w:
                Dist[c1] = d+w
                heappush(Q, (Dist[c1],c1))


# Input & MAIN
def parse_conf():
    I = sys.stdin.readlines()
    H = list(I[1][1:-2])
    for k in range(4):
        H[2*k+2] = '_'
    H = ''.join(H)
    R = [''.join(I[i][2*k+3] for i in range(2,len(I)-1)) for k in range(4)]
    R = [S.rstrip(a) for S,a in zip(R,'ABCD')]  # remove already final positions
    return enc_conf(H,R)

print(dijkstra(parse_conf()))
