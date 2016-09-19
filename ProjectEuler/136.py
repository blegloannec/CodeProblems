#!/usr/bin/env python

# cf analyse du 135 : y(3y-4z) = n
# + approche generative :
# on balaye selon y, puis z a y fixe, et on genere les n associes
# il faut 3y-4z > 0 donc 4z < 3y
# on va balayer selon les 4z decroissants
# runs in ~5s with pypy

def main():
    N = 50*10**6
    cpt = [0 for _ in xrange(N)]
    for y in xrange(1,N):
        z4 = (3*y-1) - ((3*y-1)%4)
        n = y*(3*y-z4)
        while z4>0 and n<N:
            cpt[n] += 1
            z4 -= 4
            n = y*(3*y-z4)
    S = 0
    for n in xrange(N):
        if cpt[n]==1:
            S += 1
    print S

main()
