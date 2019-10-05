#!/usr/bin/env python3

# https://en.wikipedia.org/wiki/Catalan_number
NMAX = 5001
Catalan = [1]*NMAX
for n in range(1,NMAX):
    Catalan[n] = 2*(2*n-1)*Catalan[n-1]//(n+1)

Q = int(input())
for _ in range(Q):
    print(Catalan[int(input())])
