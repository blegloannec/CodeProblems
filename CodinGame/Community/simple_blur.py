#!/usr/bin/env python3

H,W = map(int, input().split())
I = [tuple(map(int, input().split())) for _ in range(H*W)]
O = []
for i in range(H):
    for j in range(W):
        r,g,b = I[i*W+j]
        vcnt = 1
        for vi,vj in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
            if 0<=vi<H and 0<=vj<W:
                vr,vg,vb = I[vi*W+vj]
                r += vr
                g += vg
                b += vb
                vcnt += 1
        O.append((r//vcnt, g//vcnt, b//vcnt))
for L in O:
    print(*L)
