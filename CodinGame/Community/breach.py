#!/usr/bin/env python3

# unusual puzzle, inspired by https://bubmet.itch.io/intercept
# uninteresting and unoriginal small challenges though...

import sys, re

Elements = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']
Col = {'W': 'GRAY', 'w': 'WHITE', 'R': 'RED', 'r': 'LIGHT_RED', 'G': 'GREEN', 'g': 'LIGHT_GREEN', 'B': 'BLUE', 'b': 'LIGHT_BLUE', 'y': 'YELLOW', 'o': 'ORANGE', 'P': 'PINK', 'p': 'LIGHT_PINK', 'V': 'VIOLET', 'v': 'LIGHT_VIOLET'}
Set2Num = {
    frozenset([(0, 0), (1, -1), (2, -1), (3, -1), (4, -1), (5, 0), (5, 1), (5, 2), (5, 3), (4, 4), (3, 4), (2, 4), (1, 4), (0, 3), (0, 2), (0, 1)]): '0',
    frozenset([(0, 0), (1, 1), (2, 2), (3, 3), (4, 3), (5, 4), (5, 3), (5, 2), (5, 1), (5, 0), (4, 1), (4, 2), (3, 2), (3, 1), (2, 3), (1, 3), (0, 3), (2, 1), (1, 2), (0, 2), (1, 0), (1, -1), (0, 1)]): '1',
    frozenset([(0, 0), (1, 0), (2, 0), (1, -1), (0, 1), (0, 2), (0, 3), (1, 4), (2, 4), (3, 3), (4, 2), (5, 3), (5, 4), (5, 5), (5, 2), (5, 1), (5, 0), (5, -1), (4, 1), (3, 2), (2, 3), (1, 5), (0, 4)]): '2',
    frozenset([(0, 0), (1, 0), (1, -1), (0, 1), (0, 2), (0, 3), (1, 4), (2, 4), (3, 5), (4, 4), (4, 3), (4, 2), (4, 1), (4, 0), (3, -1), (3, 0), (3, 4), (2, 3), (1, 5), (0, 4)]): '3',
    frozenset([(0, 0), (1, -1), (2, -1), (3, 0), (3, 1), (3, 2), (4, 3), (5, 4), (5, 3), (4, 4), (3, 4), (2, 4), (1, 4), (0, 3), (0, 2), (1, 3), (3, 3), (2, 3), (3, -1), (3, -2), (3, -3), (2, -2), (1, -2), (0, 1)]): '4',
    frozenset([(0, 0), (1, 0), (2, 1), (2, 2), (2, 3), (3, 4), (4, 4), (5, 4), (5, 3), (5, 2), (5, 1), (5, 0), (2, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5)]): '5',
    frozenset([(0, 0), (1, -1), (2, 0), (3, -1), (4, 0), (4, 1), (4, -1), (2, 1), (2, 2), (3, 3), (2, -1), (0, 1), (0, 2)]): '6',
    frozenset([(0, 0), (0, 1), (0, 2), (0, 3), (1, 4), (2, 4), (3, 3), (4, 2), (5, 1), (4, 1), (3, 2), (2, 3), (1, 5), (0, 5), (0, 4)]): '7',
    frozenset([(0, 0), (1, -1), (2, 0), (3, -1), (4, 0), (4, 1), (3, 2), (2, 1), (1, 2), (0, 1)]): '8',
    frozenset([(0, 0), (1, -1), (2, 0), (2, 1), (2, 2), (3, 3), (4, 3), (2, 3), (1, 4), (0, 3), (0, 2), (0, 1)]): '9'}

def components(pic):
    H,W = len(pic),len(pic[0])
    pic[-1] += ' '*(W-len(pic[-1]))  # last line padding
    seen = [[False]*W for _ in range(H)]
    Comp = []
    for j in range(W):
        if pic[0][j]=='+' and not seen[0][j]:
            comp = []
            seen[0][j] = True
            Q = [(0,j)]
            while Q:
                x,y = Q.pop()
                comp.append((x,y-j))
                for vx in range(x-1,x+2):
                    if 0<=vx<H:
                        for vy in range(y-1,y+2):
                            if 0<=vy<W and pic[vx][vy]=='+' and not seen[vx][vy]:
                                seen[vx][vy] = True
                                Q.append((vx,vy))
            Comp.append(comp)
    return Comp

while True:
    lines = int(input())
    lock = input().split(':')[0]
    if lock=='ss_n':
        O = re.match('\[([0-9]+),.*\]\[([0-9]+)\]', input())
        u0, u1, n = 0, int(O.group(1)), int(O.group(2))
        for _ in range(n):
            u1, u0 = u0+u1, u1
        print(u1)
    elif lock=='rs_n':
        O = re.match('\[([0-9]+), ([0-9]+),.*\]\[([0-9]+)\]', input())
        u0,u1,n = int(O.group(1)), int(O.group(2)), int(O.group(3))
        print(u0 + n*(u1-u0))
    elif lock in ('ss_f','rs_f'):
        c = next(c for c in input() if 'a'<=c<='z')  # always the first char for rs_f
        print(ord(c)-ord('a'))
    elif lock=='gs_m':
        print(Elements[int(input().split(': ')[1])-1])
    elif lock=='ss_m':
        print(Elements.index(input())+1)
    elif lock=='ss_colv':
        print(Col[input().split('+')[0][-1]])
    elif lock=='rs_colv':
        print(Col[input()[1]])
    elif lock=='ss_asc':
        pic = [input() for _ in range(1,lines)]
        #for L in pic: print(L, file=sys.stderr)
        Comp = components(pic)
        print( ''.join(Set2Num[frozenset(comp)] for comp in Comp))
    elif lock=='ss_con':
        I = input().split('...')
        try:
            i = next(i for i in range(1,6) if I[i-1][-1]!='g')
        except:
            i = 0
        print(i)
    else:  # new lock discovered
        print(lock, file=sys.stderr)
        for _ in range(1,lines):
            print(input(), file=sys.stderr)
        sys.exit()
