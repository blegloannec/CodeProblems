#!/usr/bin/env python3

Animals = {'Rabbits':  {'Heads':1, 'Horns':0, 'Legs':4, 'Wings':0, 'Eyes':2},
           'Chickens': {'Heads':1, 'Horns':0, 'Legs':2, 'Wings':2, 'Eyes':2},
           'Cows':     {'Heads':1, 'Horns':2, 'Legs':4, 'Wings':0, 'Eyes':2},
           'Pegasi':   {'Heads':1, 'Horns':0, 'Legs':4, 'Wings':2, 'Eyes':2},
           'Demons':   {'Heads':1, 'Horns':4, 'Legs':4, 'Wings':2, 'Eyes':4}}


### some old matrix inversion code ###
from fractions import *

def id(n):
    return [[int(i==j) for j in range(n)] for i in range(n)]

def copy(M):
    return [L[:] for L in M]

def l_swap(M,i,j):
    w = len(M[0])
    for k in range(w):
        M[i][k],M[j][k] = M[j][k],M[i][k]

def first_non_zero(M,i):
    h = len(M)
    for j in range(i,h):
        if M[j][i]!=0:
            return j
    return None

def sline_prod(a,M,i):
    w = len(M[0])
    for j in range(w):
        M[i][j] *= a

def line_diff(a,M,i,j):
    # Mj <- Mj - a*Mi
    w = len(M[0])
    for k in range(w):
        M[j][k] -= a*M[i][k]

def inverse(M0):
    M = copy(M0)
    n = len(M)
    I = id(n)
    for i in range(n):
        j0 = first_non_zero(M,i)
        assert(j0!=None)
        if j0>i:
            l_swap(M,i,j0)
            l_swap(I,i,j0)
        a = Fraction(1,M[i][i])  # for exact fraction computation
        sline_prod(a,M,i)
        sline_prod(a,I,i)
        for j in range(n):
            if j!=i:
                a = M[j][i]
                line_diff(a,M,i,j)
                line_diff(a,I,i,j)
    return I

def mv_prod(M,x):
    n = len(x)
    y = [0]*n
    for i in range(n):
        for j in range(n):
            y[i] += x[j]*M[i][j]
    return y
### === ###


def main():
    n = int(input())
    Species = input().split()
    M = []
    B = []
    for _ in range(n):
        thg,cnt = input().split()
        cnt = int(cnt)
        M.append([Animals[spc][thg] for spc in Species])
        B.append(cnt)
    Minv = inverse(M)
    A = mv_prod(Minv,B)
    for spc,cnt in zip(Species,A):
        print(spc,cnt)

main()
