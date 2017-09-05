#!/usr/bin/env python3

import rosalib

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

def global_score(u,v):
    m,n = len(u),len(v)
    # T[i][j] = score max d'alignement de u[:i] et v[:j]
    T = [[float('-inf')]*(n+1) for _ in range(m+1)]
    T[0][0] = 0
    pred = [[[None]*(n+1) for _ in range(m+1)] for _ in range(3)]
    # Tgap_u[i][j] = idem en terminant par un gap (non vide) en u
    Tgap_u = [[float('-inf')]*(n+1) for _ in range(m+1)]
    Tgap_v = [[float('-inf')]*(n+1) for _ in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==j==0:
                continue
            if i>0:
                if Tgap_v[i-1][j]-LGap > T[i-1][j]-CGap:
                    Tgap_v[i][j] = Tgap_v[i-1][j]-LGap
                    pred[2][i][j] = (2,i-1,j)
                else:
                    Tgap_v[i][j] = T[i-1][j]-CGap
                    pred[2][i][j] = (0,i-1,j)
            if j>0:
                if Tgap_u[i][j-1]-LGap > T[i][j-1]-CGap:
                    Tgap_u[i][j] = Tgap_u[i][j-1]-LGap
                    pred[1][i][j] = (1,i,j-1)
                else:
                    Tgap_u[i][j] = T[i][j-1]-CGap
                    pred[1][i][j] = (0,i,j-1)
            if Tgap_u[i][j] >= Tgap_v[i][j]:
                T[i][j] = Tgap_u[i][j]
                pred[0][i][j] = pred[1][i][j]
            else:
                T[i][j] = Tgap_v[i][j]
                pred[0][i][j] = pred[2][i][j]
            if i>0 and j>0:
                s = T[i-1][j-1] + B[Num[u[i-1]]][Num[v[j-1]]]
                if s>T[i][j]:
                    T[i][j] = s
                    pred[0][i][j] = (0,i-1,j-1)
    return T,pred

def solution(A,B,pred):
    t,i,j = 0,len(A),len(B)
    SA,SB = [],[]
    while pred[t][i][j]!=None:
        t,pi,pj = pred[t][i][j]
        SA.append(A[i-1] if pi<i else '-')
        SB.append(B[j-1] if pj<j else '-')
        i,j = pi,pj
    return ''.join(reversed(SA)),''.join(reversed(SB))

def main():
    A,B = (X for _,X in rosalib.parse_fasta())
    T,pred = global_score(A,B)
    print(T[-1][-1])
    SA,SB = solution(A,B,pred)
    print(SA)
    print(SB)

main()
