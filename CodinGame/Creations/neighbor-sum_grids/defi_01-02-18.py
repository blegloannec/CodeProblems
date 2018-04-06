#!/usr/bin/env pypy

# http://images.math.cnrs.fr/Fevrier-2018-1er-defi.html

N = 5
M = N*N

V = [0]*M
for i in xrange(N):
    for j in xrange(N):
        u = N*i+j
        for vi in xrange(i-1,i+2):
            for vj in xrange(j-1,j+2):
                if (vi,vj)!=(i,j) and 0<=vi<N and 0<=vj<N:
                    V[u] |= 1<<(N*vi+vj)

def elem(x):
    i = 0
    while x:
        if x&1:
            yield i
        x >>= 1
        i += 1

def grid(S):
    G = [0]*M
    for i in xrange(1,M+1):
        G[S[i]] = i
    return G

S = [None]*(M+1)
full = (1<<M)-1

def backtrack(Avail=full, i=1):
    if i>M:
        yield grid(S)
    else:
        if i<=2:
            P = Avail
        else:
            P = 0
            for k in xrange(1,(i+1)/2):
                l = i-k
                P |= V[S[k]] & V[S[l]] & Avail
        for p in elem(P):
            S[i] = p
            for x in backtrack(Avail^(1<<p),i+1):
                yield x

def main():
    C = list(backtrack())
    for G in C:
        print(' '.join(map(str,G)))

main()
