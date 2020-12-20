#!/usr/bin/env python3

import sys
from collections import defaultdict

I = [L.strip() for L in sys.stdin.readlines()]


# Part 1
val  = lambda c: '.#'.index(c)
mask = lambda s: sum(val(c)<<i for i,c in enumerate(s))

def sym(tile):
    size = len(tile)
    rota = [''.join(tile[i][j] for i in range(size)) for j in range(size-1,-1,-1)]
    for t in (tile, rota):
        yield t
        yield t[::-1]
        yield [l[::-1] for l in t]
        yield [l[::-1] for l in reversed(t)]

class Tile:
    def __init__(self, num, tile):
        self.num = num
        self.tile = tile
        self.n = mask(tile[0])                                # North
        self.s = mask(tile[-1])                               # South
        self.w = mask(tile[i][0]  for i in range(len(tile)))  # West
        self.e = mask(tile[i][-1] for i in range(len(tile)))  # East

N2T = defaultdict(list)  # North color -> tiles
S2T = defaultdict(list)
W2T = defaultdict(list)
E2T = defaultdict(list)
Tiles = []
for i in range(0, len(I), 12):
    num = int(I[i].split()[1][:-1])
    tile = I[i+1:i+11]
    T = [Tile(num, t) for t in sym(tile)]
    for i,t in enumerate(T):
        j = len(Tiles)+i
        N2T[t.n].append(j)
        S2T[t.s].append(j)
        W2T[t.w].append(j)
        E2T[t.e].append(j)
    Tiles += T

# Identify a valid top-left corner
for i,t in enumerate(Tiles):
    if len(S2T[t.n])==len(E2T[t.w])==1: # only a symmetry of itself
        t00 = t
        break

# Building the tiling
def get_east(t):
    Cand = [i for i in W2T[t.e] if Tiles[i].num!=t.num]
    if Cand:
        assert len(Cand) == 1
        return Tiles[Cand[0]]
    return None

def get_south(t):
    Cand = [i for i in N2T[t.s] if Tiles[i].num!=t.num]
    if Cand:
        assert len(Cand) == 1
        return Tiles[Cand[0]]
    return None

Tiling = [[t00]]
while True:
    e = get_east(Tiling[-1][0])
    while e is not None:
        Tiling[-1].append(e)
        e = get_east(e)
    s = get_south(Tiling[-1][0])
    if s is not None:
        Tiling.append([s])
    else:
        break

part1 = Tiling[0][0].num * Tiling[0][-1].num * Tiling[-1][0].num * Tiling[-1][-1].num
print(part1)


# Part 2
tsize = len(Tiles[0].tile)
Sea = []
for L in Tiling:
    for i in range(1, tsize-1):
        Sea.append(''.join(t.tile[i][1:-1] for t in L))
ssize = len(Sea)

Monster = ('                  # ',
           '#    ##    ##    ###',
           ' #  #  #  #  #  #   ')
monh = len(Monster)
monw = len(Monster[0])
Mon1 = [(i,j) for i in range(monh) for j in range(monw) if Monster[i][j]=='#']

for S in sym(Sea):
    mcnt = 0
    for i0 in range(ssize-monh+1):
        for j0 in range(ssize-monw+1):
            valid = True
            for i,j in Mon1:
                if S[i0+i][j0+j]!='#':
                    valid = False
                    break
            if valid:
                mcnt += 1
    if mcnt>0:
        break

# monsters do not intersect
sea1 = sum(L.count('#') for L in Sea)
print(sea1 - mcnt*len(Mon1))
