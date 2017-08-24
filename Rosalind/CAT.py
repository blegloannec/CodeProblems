#!/usr/bin/env python3

import rosalib

_,RNA = rosalib.parse_fasta()[0]
num = {'A':0,'U':1,'C':2,'G':3}
pair = {'A':'U','U':'A','C':'G','G':'C'}

memo = {}
# nb de perfect planar matchings de RNA[i:j+1]
# supposee equilibree en A/U et C/G
def planar_match(i,j):
    if i>j:
        return 1
    if (i,j) in memo:
        return memo[i,j]
    C = [0]*4  # compteur des lettres des indices i+1 a k-1
    res = 0
    for k in range(i+1,j+1): # indice avec lequel on match i
        if k-1>i:
            C[num[RNA[k-1]]] += 1
        if pair[RNA[i]]==RNA[k] and C[0]==C[1] and C[2]==C[3]:
            # decoupage possible ici
            res += planar_match(i+1,k-1)*planar_match(k+1,j)
    memo[i,j] = res
    return res

print(planar_match(0,len(RNA)-1) % 10**6)
