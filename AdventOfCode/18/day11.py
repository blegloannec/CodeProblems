#!/usr/bin/env python3

S = 300
I = 5235  # Input


# Part 1
G = [[(((((x+10)*y+I)*(x+10))//100)%10)-5 for y in range(1,S+1)] for x in range(1,S+1)]

SL = [L[:] for L in G]
for x in range(S):
    for y in range(1,S):
        SL[x][y] += SL[x][y-1]

SG = [[0]*(S+1) for _ in range(S+1)]
for x in range(1,S+1):
    for y in range(1,S+1):
        SG[x][y] = SL[x-1][y-1] + SG[x-1][y]

def max_square(size):
    s = size-1
    V = float('-inf')
    for x in range(1,S-s+1):
        for y in range(1,S-s+1):
            v = SG[x+s][y+s] - SG[x+s][y-1] - SG[x-1][y+s] + SG[x-1][y-1]
            if v>V:
                V,X,Y = v,x,y
    return V,X,Y

print(','.join(map(str,max_square(3)[1:])))


# Part 2
(_,x,y),s = max((max_square(s),s) for s in range(1,S+1))
print('%d,%d,%d' % (x,y,s))
