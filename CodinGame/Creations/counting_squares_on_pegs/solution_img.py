#!/usr/bin/env python3

def sqr_norm(S):
    i = S.index(min(S))
    return S[i:]+S[:i]

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
    xmax, ymax = max(x for x,_ in Pts), max(y for _,y in Pts)
    SVG = ['<svg width="{}" height="{}">'.format(xmax,ymax)]
    for S in Sqr:
        for i in range(4):
            (x1,y1), (x2,y2) = S[i], S[(i+1)%4]
            SVG.append('line x1="{}" y1="{}" x2="{}" y2="{}" stroke="blue" />'.format(x1,y1,x2,y2))
    for x,y in Pts:
        SVG.append('<circle cx="{}" cy="{}" r="1" fill="red" />'.format(x,y))
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
