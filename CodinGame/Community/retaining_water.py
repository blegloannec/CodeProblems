#!/usr/bin/env python3

# see also:
#  https://en.wikipedia.org/wiki/Water_retention_on_mathematical_surfaces
#  https://oeis.org/A201126

N = int(input())
H = [[ord(c)-ord('A') for c in input()] for _ in range(N)]
W = [[25 if 0<i<N-1 and 0<j<N-1 else H[i][j] for j in range(N)]
     for i in range(N)]
change = True
while change:
    change = False
    for i in range(1, N-1):
        for j in range(1, N-1):
            w = max(H[i][j],
                    min(W[i-1][j], W[i+1][j], W[i][j-1], W[i][j+1]))
            if w < W[i][j]:
                W[i][j] = w
                change = True
vol = sum(W[i][j]-H[i][j] for i in range(N) for j in range(N))
print(vol)
