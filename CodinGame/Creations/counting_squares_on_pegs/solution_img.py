#!/usr/bin/env python3

import random
random.seed()

def rand_color():
    return '#{:06x}'.format(random.randint(0,(1<<24)-1))

def sqr_norm(S):
    i = S.index(min(S))
    S = S[i:]+S[:i]
    if S[1]>S[3]:
        S = (S[0],S[3],S[2],S[1])
    return S

def squares(P):
    N = len(P)
    S = set(P)
    Sqr = set()
    for i in range(N):
        A = xi,yi = P[i]
        for j in range(i+1,N):
            B = xj,yj = P[j]
            dx,dy = xi-xj,yi-yj
            for nx,ny in [(-dy,dx),(dy,-dx)]:
                D = (xi+nx,yi+ny)
                C = (xj+nx,yj+ny)
                if C in S and D in S:
                    Sqr.add(sqr_norm((A,B,C,D)))
    return Sqr

def make_svg(Pts, Sqr):
    A, L = 100, 5
    xmax, ymax = max(x for x,_ in Pts)+1, max(y for _,y in Pts)+1
    C = lambda x: A*(x+1)
    SVG = ['<svg width="{}" height="{}">'.format(C(xmax),C(ymax))]
    for S in Sqr:
        col = rand_color()
        for i in range(4):
            (x1,y1), (x2,y2) = S[i], S[(i+1)%4]
            SVG.append('<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="{}" stroke-width="{}" />'.format(C(x1),C(y1),C(x2),C(y2),col,L))
    for x,y in Pts:
        SVG.append('<circle cx="{}" cy="{}" r="{}" fill="red" />'.format(C(x),C(y),2*L))
    SVG.append('</svg>')
    return '\n'.join(SVG)

def main():
    N = int(input())
    P = [tuple(map(int,input().split())) for _ in range(N)]
    S = squares(P)
    print(len(S))
    Out = open('cover.svg', 'w')
    Out.write(make_svg(P,S))
    Out.close()

main()
