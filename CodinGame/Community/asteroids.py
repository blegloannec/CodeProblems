#!/usr/bin/env python3

from math import floor

W,H, t1,t2,t3 = map(int, input().split())
Pic1 = {}
Pic2 = {}
for i in range(H):
    row1,row2 = input().split()
    for j in range(W):
        if row1[j]!='.': Pic1[row1[j]] = complex(i,j)
        if row2[j]!='.': Pic2[row2[j]] = complex(i,j)
Pic3 = [['.']*W for _ in range(H)]
for a,z1 in Pic1.items():
    z3 = z1 + (Pic2[a]-z1)*(t3-t1)/(t2-t1)
    i,j = floor(z3.real),floor(z3.imag)
    if 0<=i<H and 0<=j<W and (Pic3[i][j]=='.' or a<Pic3[i][j]):
        Pic3[i][j] = a
print('\n'.join(''.join(L) for L in Pic3))
