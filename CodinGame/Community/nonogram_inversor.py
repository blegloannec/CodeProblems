#!/usr/bin/env python3

# *simple* nonograms solver (deduction only, no backtracking)

import sys
from itertools import groupby

def gen_masks(Size, Bloc):
    Suff = list(Bloc)
    for i in range(len(Bloc)-2,-1,-1):
        Suff[i] += Suff[i+1]+1
    Suff.append(0)
    yield from _gen_masks(Size, Bloc, Suff)

def _gen_masks(Size, Bloc, Suff, x0=0, i=0, M=0):
    if i==len(Bloc):
        yield M
    else:
        bs = Bloc[i] + (i<len(Bloc)-1)
        for x in range(x0+bs, Size+1-Suff[i+1]):
            yield from _gen_masks(Size, Bloc, Suff, x, i+1, M|((1<<Bloc[i])-1)<<(x-bs))

def nonogram_solve(W, H, Blocs):
    size = lambda i:     H if i<W else W
    dual = lambda i,j: j+W if i<W else j
    # generate lists of possibilities for each line/column
    Masks = [list(gen_masks(size(i), Bloc)) for i,Bloc in enumerate(Blocs)]
    # Sure[i][b] = mask of known bits b of line/column i
    Sure = [[0,0] for _ in range(W+H)]
    Q = set(range(W+H))
    while Q:
        i = Q.pop()
        # let us update line/column i data
        assert Sure[i][0]&Sure[i][1]==0
        # Sure[i] has been modified since last visit of i
        # we filter the compatible masks
        Masks[i] = [M for M in Masks[i] if ~M&Sure[i][0]==Sure[i][0] and M&Sure[i][1]==Sure[i][1]]
        # we improve the known bits
        M0 = M1 = (1<<size(i))-1
        for M in Masks[i]:
            M0 &= ~M
            M1 &=  M
        Diff = [Sure[i][0]^M0, Sure[i][1]^M1]  # newly known bits
        Sure[i] = [M0,M1]
        # we propagate the newly known bits to dual lines/columns
        Bi = 1<<(i-W if i>=W else i)
        for b in range(2):
            j = 0
            while Diff[b]:
                if Diff[b]&1:
                    k = dual(i,j)
                    if not Sure[k][b]&Bi:
                        Sure[k][b] |= Bi
                        Q.add(k)
                Diff[b] >>= 1
                j += 1
    assert all(len(M)==1 for M in Masks)
    return Sure

def outblocs(M):
    if M==0:
        return (0,)
    return tuple(sum(1 for _ in g) for x,g in groupby(reversed('{:b}'.format(M))) if x=='1')

if __name__=='__main__':
    W,H = map(int,input().split())
    Blocs = [tuple(map(int,input().split())) for _ in range(W+H)]
    Sol = nonogram_solve(W, H, Blocs)
    F = '{:0%db}' % W
    for i in range(W,W+H):
        print(F.format(Sol[i][1]), file=sys.stderr)
    for i in range(W+H):
        print(*outblocs(Sol[i][0]))
