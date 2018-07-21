#!/usr/bin/env python

# rectangle caracterise par {x,x'} et {y,y'}
# nb rect = (2 parmi X) * (2 parmi Y)
def nb_rect(x,y):
    return x*(x+1)*y*(y+1)/4

cible = 2000000
m = cible
xy = 0
N = 1000
for x in range(N):
    for y in range(N):
        d = abs(cible-nb_rect(x,y))
        if d<m:
            m = d
            xy = x*y
print xy
