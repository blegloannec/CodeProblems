#!/usr/bin/env python3

G = [list(map(int,input().split())) for _ in range(4)]
nb4 = int(input())

# S(n) = score to generate a tile of value 2^n starting only from 2s (not 4s)
# clearly S(n) = 2^n + 2*S(n-1), leading to S(n) = (n-1)*2^n
TileScore = {2**i:(i-1)*2**i for i in range(1,20)}
TileScore[0] = 0
score = sum(sum(TileScore[tile] for tile in L) for L in G) - 4*nb4

total = sum(sum(L) for L in G)
nb2 = (total-4*nb4)//2
turns = nb2+nb4-2

print(score)
print(turns)
