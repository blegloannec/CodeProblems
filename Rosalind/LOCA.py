#!/usr/bin/env python3

import rosalib

# AA to index
Num = {'P': 12, 'T': 16, 'F': 4, 'A': 0, 'E': 3, 'R': 14, 'V': 17, 'Q': 13, 'W': 18, 'D': 2, 'I': 7, 'L': 9, 'G': 5, 'C': 1, 'M': 10, 'S': 15, 'H': 6, 'Y': 19, 'K': 8, 'N': 11}

# PAM250 matrix
B = [[2,-2,0,0,-3,1,-1,-1,-1,-2,-1,0,1,0,-2,1,1,0,-6,-3],
     [-2,12,-5,-5,-4,-3,-3,-2,-5,-6,-5,-4,-3,-5,-4,0,-2,-2,-8,0],
     [0,-5,4,3,-6,1,1,-2,0,-4,-3,2,-1,2,-1,0,0,-2,-7,-4],
     [0,-5,3,4,-5,0,1,-2,0,-3,-2,1,-1,2,-1,0,0,-2,-7,-4],
     [-3,-4,-6,-5,9,-5,-2,1,-5,2,0,-3,-5,-5,-4,-3,-3,-1,0,7],
     [1,-3,1,0,-5,5,-2,-3,-2,-4,-3,0,0,-1,-3,1,0,-1,-7,-5],
     [-1,-3,1,1,-2,-2,6,-2,0,-2,-2,2,0,3,2,-1,-1,-2,-3,0],
     [-1,-2,-2,-2,1,-3,-2,5,-2,2,2,-2,-2,-2,-2,-1,0,4,-5,-1],
     [-1,-5,0,0,-5,-2,0,-2,5,-3,0,1,-1,1,3,0,0,-2,-3,-4],
     [-2,-6,-4,-3,2,-4,-2,2,-3,6,4,-3,-3,-2,-3,-3,-2,2,-2,-1],
     [-1,-5,-3,-2,0,-3,-2,2,0,4,6,-2,-2,-1,0,-2,-1,2,-4,-2],
     [0,-4,2,1,-3,0,2,-2,1,-3,-2,2,0,1,0,1,0,-2,-4,-2],
     [1,-3,-1,-1,-5,0,0,-2,-1,-3,-2,0,6,0,0,1,0,-1,-6,-5],
     [0,-5,2,2,-5,-1,3,-2,1,-2,-1,1,0,4,1,-1,-1,-2,-5,-4],
     [-2,-4,-1,-1,-4,-3,2,-2,3,-3,0,0,0,1,6,0,-1,-2,2,-4],
     [1,0,0,0,-3,1,-1,-1,0,-3,-2,1,1,-1,0,2,1,-1,-2,-3],
     [1,-2,0,0,-3,0,-1,0,0,-2,-1,0,0,-1,-1,1,3,0,-5,-3],
     [0,-2,-2,-2,-1,-1,-2,4,-2,2,2,-2,-1,-2,-2,-1,0,4,-6,-2],
     [-6,-8,-7,-7,0,-7,-3,-5,-3,-2,-4,-4,-6,-5,2,-2,-5,-6,17,0],
     [-3,0,-4,-4,7,-5,0,-1,-4,-1,-2,-2,-5,-4,-4,-3,-3,-2,0,10]]

LGap = 5

# scoring code from GLOB
def global_score(u,v):
    m,n = len(u),len(v)
    T = [[float('-inf')]*(n+1) for _ in range(m+1)]
    T[0][0] = 0
    for i in range(m+1):
        for j in range(n+1):
            if i>0:
                T[i][j] = max(T[i][j],T[i-1][j]-LGap)
            if j>0:
                T[i][j] = max(T[i][j],T[i][j-1]-LGap)
            if i>0 and j>0:
                T[i][j] = max(T[i][j],T[i-1][j-1]+B[Num[u[i-1]]][Num[v[j-1]]])
    return T

def local_score(A,B):
    # on commence par calculer le score global pour trouver les
    # possibles points d'arret (maxima locaux)
    T = global_score(A,B)
    M,R = float('-inf'),[]
    for i in range(len(A)+1):
        for j in range(len(B)+1):
            if T[i][j]>M:
                M = T[i][j]
                R = [(i,j)]
            elif T[i][j]==M:
                R.append((i,j))
    # puis pour chaque point d'arret on calcule le score global des
    # chaines *inversees* a partir du point d'arret et on cherche les
    # points de depart (maxima locaux)
    M,LR = float('-inf'),[]
    for (a,b) in R:
        T = global_score(A[a-1::-1],B[b-1::-1])
        for i in range(a+1):
            for j in range(b+1):
                if T[i][j]>M:
                    M = T[i][j]
                    LR = [(a-i,a,b-j,b)]
                elif T[i][j]==M:
                    LR.append((a-i,a,b-j,b))
    return M,LR

def main():
    A,B = tuple(S for _,S in rosalib.parse_fasta())
    M,P = local_score(A,B)
    print(M)
    la,ra,lb,rb = P[0]
    print(A[la:ra])
    print(B[lb:rb])

main()
