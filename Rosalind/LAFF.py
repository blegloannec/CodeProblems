#!/usr/bin/env pypy

# basically GAFF with LOCA modifications, O(n^2) with n ~ 10^4
# using module array for memory efficient arrays
# runs in ~13s with pypy

import rosalib
import array

# AA to index
Num = {'P': 12, 'T': 16, 'F': 4, 'A': 0, 'E': 3, 'R': 14, 'V': 17, 'Q': 13, 'W': 18, 'D': 2, 'I': 7, 'L': 9, 'G': 5, 'C': 1, 'M': 10, 'S': 15, 'H': 6, 'Y': 19, 'K': 8, 'N': 11}

# BLOSUM62 matrix
B = [[4, 0, -2, -1, -2, 0, -2, -1, -1, -1, -1, -2, -1, -1, -1, 1, 0, 0, -3, -2],
     [0, 9, -3, -4, -2, -3, -3, -1, -3, -1, -1, -3, -3, -3, -3, -1, -1, -1, -2, -2],
     [-2, -3, 6, 2, -3, -1, -1, -3, -1, -4, -3, 1, -1, 0, -2, 0, -1, -3, -4, -3],
     [-1, -4, 2, 5, -3, -2, 0, -3, 1, -3, -2, 0, -1, 2, 0, 0, -1, -2, -3, -2],
     [-2, -2, -3, -3, 6, -3, -1, 0, -3, 0, 0, -3, -4, -3, -3, -2, -2, -1, 1, 3],
     [0, -3, -1, -2, -3, 6, -2, -4, -2, -4, -3, 0, -2, -2, -2, 0, -2, -3, -2, -3],
     [-2, -3, -1, 0, -1, -2, 8, -3, -1, -3, -2, 1, -2, 0, 0, -1, -2, -3, -2, 2],
     [-1, -1, -3, -3, 0, -4, -3, 4, -3, 2, 1, -3, -3, -3, -3, -2, -1, 3, -3, -1],
     [-1, -3, -1, 1, -3, -2, -1, -3, 5, -2, -1, 0, -1, 1, 2, 0, -1, -2, -3, -2],
     [-1, -1, -4, -3, 0, -4, -3, 2, -2, 4, 2, -3, -3, -2, -2, -2, -1, 1, -2, -1],
     [-1, -1, -3, -2, 0, -3, -2, 1, -1, 2, 5, -2, -2, 0, -1, -1, -1, 1, -1, -1],
     [-2, -3, 1, 0, -3, 0, 1, -3, 0, -3, -2, 6, -2, 0, 0, 1, 0, -3, -4, -2],
     [-1, -3, -1, -1, -4, -2, -2, -3, -1, -3, -2, -2, 7, -1, -2, -1, -1, -2, -4, -3],
     [-1, -3, 0, 2, -3, -2, 0, -3, 1, -2, 0, 0, -1, 5, 1, 0, -1, -2, -2, -1],
     [-1, -3, -2, 0, -3, -2, 0, -3, 2, -2, -1, 0, -2, 1, 5, -1, -1, -3, -3, -2],
     [1, -1, 0, 0, -2, 0, -1, -2, 0, -2, -1, 1, -1, 0, -1, 4, 1, -2, -3, -2],
     [0, -1, -1, -1, -2, -2, -2, -1, -1, -1, -1, 0, -1, -1, -1, 1, 5, 0, -2, -2],
     [0, -1, -3, -2, -1, -3, -3, 3, -2, 1, 1, -3, -2, -2, -3, -2, 0, 4, -3, -1],
     [-3, -2, -4, -3, 1, -2, -2, -3, -3, -2, -1, -4, -4, -2, -3, -3, -2, -3, 11, 2],
     [-2, -2, -3, -2, 3, -3, 2, -1, -2, -1, -1, -2, -3, -1, -2, -2, -2, -1, 2, 7]]

CGap = 11  # gap opening penalty
LGap = 1   # gap extension penalty

def suffix_score(u,v):
    m,n = len(u),len(v)
    # T[i][j] = score max d'alignement de u[:i] et v[:j]
    T = [array.array('i',[0]*(n+1)) for _ in xrange(m+1)]
    pred = [[[array.array('b',[0]*(n+1)) for _ in xrange(m+1)] for _ in xrange(3)] for _ in xrange(3)]
    # Tgap_u[i][j] = idem en terminant par un gap (non vide) en u
    inf = 1<<30
    Tgap_u = [array.array('i',[-inf]*(n+1)) for _ in xrange(m+1)]
    Tgap_v = [array.array('i',[-inf]*(n+1)) for _ in xrange(m+1)]
    for i in xrange(m+1):
        for j in xrange(n+1):
            if i>0:
                if Tgap_v[i-1][j]-LGap > T[i-1][j]-CGap:
                    Tgap_v[i][j] = Tgap_v[i-1][j]-LGap
                    #pred[2][i][j] = (2,i-1,j)
                    pred[0][2][i][j],pred[1][2][i][j],pred[2][2][i][j] = 2,-1,0
                else:
                    Tgap_v[i][j] = T[i-1][j]-CGap
                    #pred[2][i][j] = (0,i-1,j)
                    pred[0][2][i][j],pred[1][2][i][j],pred[2][2][i][j] = 0,-1,0
                if Tgap_v[i][j]>T[i][j]:
                    T[i][j] = Tgap_v[i][j]
                    #pred[0][i][j] = pred[2][i][j]
                    pred[0][0][i][j],pred[1][0][i][j],pred[2][0][i][j] = pred[0][2][i][j],pred[1][2][i][j],pred[2][2][i][j]
            if j>0:
                if Tgap_u[i][j-1]-LGap > T[i][j-1]-CGap:
                    Tgap_u[i][j] = Tgap_u[i][j-1]-LGap
                    #pred[1][i][j] = (1,i,j-1)
                    pred[0][1][i][j],pred[1][1][i][j],pred[2][1][i][j] = 1,0,-1
                else:
                    Tgap_u[i][j] = T[i][j-1]-CGap
                    #pred[1][i][j] = (0,i,j-1)
                    pred[0][1][i][j],pred[1][1][i][j],pred[2][1][i][j] = 0,0,-1
                if Tgap_u[i][j]>T[i][j]:
                    T[i][j] = Tgap_u[i][j]
                    #pred[0][i][j] = pred[1][i][j]
                    pred[0][0][i][j],pred[1][0][i][j],pred[2][0][i][j] = pred[0][1][i][j],pred[1][1][i][j],pred[2][1][i][j]
            if i>0 and j>0:
                s = T[i-1][j-1] + B[Num[u[i-1]]][Num[v[j-1]]]
                if s>T[i][j]:
                    T[i][j] = s
                    #pred[0][i][j] = (0,i-1,j-1)
                    pred[0][0][i][j],pred[1][0][i][j],pred[2][0][i][j] = 0,-1,-1
    return T,pred

def local_score(A,B):
    T,pred = suffix_score(A,B)
    m,n = len(A),len(B)
    # finding a maximal score ending position
    smax = float('-inf')
    for i in xrange(m+1):
        for j in xrange(n+1):
            if T[i][j]>smax:
                smax = T[i][j]
                imax,jmax = i,j
    # climbing back to score 0 where prefixes were discarded
    t,i,j = 0,imax,jmax
    while not pred[1][t][i][j]==pred[2][t][i][j]==0:
        t,i,j = pred[0][t][i][j],i+pred[1][t][i][j],j+pred[2][t][i][j]
    return (smax,i,imax,j,jmax)

def main():
    A,B = (S for _,S in rosalib.parse_fasta())
    s,la,ra,lb,rb = local_score(A,B)
    print(s)
    print(A[la:ra])
    print(B[lb:rb])

main()
