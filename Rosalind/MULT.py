#!/usr/bin/env python3

from itertools import *
import rosalib
DNAS = [DNA for _,DNA in rosalib.parse_fasta()]
n = len(DNAS)

# dp((i1,i2,...,in)) = score max d'un alignement des DNAS[k][:ik] pour tout k
memo,pred = {(0,)*n:0},{}
def dp(I):
    if I in memo:
        return memo[I]
    res = float('-inf')
    for D in product(*(range(2 if I[k]>0 else 1) for k in range(n))):
        if max(D)==0:
            continue
        J = tuple(I[k]-D[k] for k in range(n))
        C = [DNAS[k][I[k]-1] if D[k]==1 else '-' for k in range(n)]
        s = dp(J) + sum(-int(C[k]!=C[l]) for k,l in combinations(range(n),2))
        if s>res:
            res = s
            # on retient le predecesseur pour faciliter la reconstruction
            # de la solution
            pred[I] = J
    memo[I] = res
    return res

def solution(I):
    Sol = [[] for _ in range(n)]
    while I in pred:
        J = pred[I]
        for k in range(n):
            Sol[k].append('-' if I[k]==J[k] else DNAS[k][I[k]-1])
        I = J
    return [''.join(reversed(X)) for X in Sol]

If = tuple(len(DNA) for DNA in DNAS)
print(dp(If))
print('\n'.join(solution(If)))
