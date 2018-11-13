#!/usr/bin/env python3

# find(x,y) = A[x]^A[x+1]^...^A[y]  (tour d'exponentielles)
# dont on recherche la parite
# c'est toujours celle de A[x], sauf si y>=x+1 et A[x+1] = 0,
# auquel cas, comme il n'y a pas deux 0 consecutifs, find(x+1,y) = 0
# et donc find(x,y) = 1

O = ['Even','Odd']

N = int(input())
A = list(map(int,input().split()))
Q = int(input())
for _ in range(Q):
    x,y = map(int,input().split())  # x & y 1-indexed
    print(O[1 if x<y and A[x]==0 else A[x-1]%2])
