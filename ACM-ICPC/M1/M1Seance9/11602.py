#!/usr/bin/env python3

from heapq import *
import random
random.seed(42)

chars = '_abcdefghilmnoprstu'
L = len(chars)
num = {chars[i]:i for i in range(L)}

def succ(P):
    for i in range(L):
        for j in range(i+1,L):
            dc = (j-i)*(S[P[i]]-S[P[j]])
            if dc<0:
                Q = list(P)
                Q[i],Q[j] = Q[j],Q[i]
                yield (dc,tuple(Q))

def score(P):
    return sum((i+1)*S[P[i]] for i in range(L))

def bfs(P0,C):
    P0 = tuple(P0)
    seen = {P0}
    H = [(score(P0),P0)]
    while H:
        c,P = heappop(H)
        if c==C:
            return P
        for (dc,Q) in succ(P):
            if c+dc>=C and Q not in seen:
                heappush(H,(c+dc,Q))
                seen.add(Q)

def main():
    global S
    I = input()
    while I!='*':
        C = int(input())
        S = [0]*L
        for c in I:
            S[num[c]] += 1
        # permutation de score maximal
        P = [i for (_,i) in sorted((S[i],i) for i in range(L))]
        T = [(score(P),P[:])]
        # on genere au hasard quelques autres permutations
        # (potentiellement de meilleurs points de depart)
        for _ in range(5):
            random.shuffle(P)
            c = score(P)
            if c>=C:
                T.append((c,P[:]))
        T.sort()
        for _,P in T:
            Q = bfs(P,C)
            if Q:
                break
        sol = ''.join(chars[p] for p in Q)
        print(sol)
        I = input()

main()
