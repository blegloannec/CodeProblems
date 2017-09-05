#!/usr/bin/env python3

import rosalib

# similaire a une edit distance classique mais en maximisant le couple (score, nb de gaps)
# essentiellement, peu importe m>0 et g<0 (ici 1 et -1), on doit simplement prendre d = -inf
# afin d'interdire les mismatches (non necessaires, ils peuvent toujours etre remplaces
# par 2 gaps consecutifs)

def max_align_max_gap(u,v):
    m,n = len(u),len(v)
    T = [[(-max(i,j),max(i,j)) for j in range(n+1)] for i in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            T[i][j] = max((T[i-1][j][0]-1, T[i-1][j][1]+1),
                          (T[i][j-1][0]-1, T[i][j-1][1]+1),
                          (T[i-1][j-1][0]+(1 if u[i-1]==v[j-1] else float('-inf')), T[i-1][j-1][1]))
    return T[m][n]

L = rosalib.parse_fasta()
print(max_align_max_gap(L[0][1],L[1][1])[1])
