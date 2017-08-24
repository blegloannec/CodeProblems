#!/usr/bin/env python3

import rosalib

_,RNA = rosalib.parse_fasta()[0]
pair = {'A':'U','U':'A','C':'G','G':'C'}

memo = {}
# nb de planar matchings de RNA[i:j+1]
def planar_match(i,j):
    if i>j:
        return 1
    if (i,j) in memo:
        return memo[i,j]
    res = planar_match(i+1,j) # on ne match pas i
    for k in range(i+1,j+1):  # indice avec lequel on match i
        if pair[RNA[i]]==RNA[k]:
            res += planar_match(i+1,k-1)*planar_match(k+1,j)
    memo[i,j] = res
    return res

print(planar_match(0,len(RNA)-1) % 10**6)
