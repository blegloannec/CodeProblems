#!/usr/bin/env python

def comptes(V,d,n,v=0):
    if n==0:
        V[v] += 1
    else:
        for i in xrange(1,d+1):
            comptes(V,d,n-1,v+i)

def main():
    V94 = [0 for _ in xrange(37)]
    V66 = [0 for _ in xrange(37)]
    comptes(V94,4,9)
    comptes(V66,6,6)
    cpt = 0
    for v4 in xrange(9,37):
        for v6 in xrange(6,v4):
            cpt += V94[v4]*V66[v6]
    print float(cpt)/(4**9*6**6)
    # rounded to 7 decimals: 0.5731441

main()
