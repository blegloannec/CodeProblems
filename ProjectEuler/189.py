#!/usr/bin/env python

from collections import defaultdict

# unoptimized DP on the consecutive lines of the trangle
# yet runs in only 9s

N = 8

# generate all complementaries of a triangle base
def gen_compl(X,i,Y):
    if i==len(X):
        yield tuple(Y)
    else:
        for c in xrange(3):
            if c==X[i]:
                continue
            Y.append(c)
            for A in gen_compl(X,i+1,Y):
                yield A
            Y.pop()

# completing a complementary of a base of rank n
# into a new base of rank n+1
def gen_line(X,i,Y):
    if i==0:
        for c in xrange(3):
            if c==X[0]:
                continue
            Y.append(c)
            for A in gen_line(X,i+1,Y):
                yield A
            Y.pop()
    elif i==len(X):
        for c in xrange(3):
            if c==X[i-1]:
                continue
            Y.append(c)
            yield tuple(Y)
            Y.pop()
    else:
        for c in xrange(3):
            if c==X[i-1] or c==X[i]:
                continue
            Y.append(c)
            for A in gen_line(X,i+1,Y):
                yield A
            Y.pop()       

# counting triangles of base n
memo = [defaultdict(int) for _ in xrange(N)]
memo[0] = {(0,):1,(1,):1,(2,):1}
def base(n):
    for X in memo[n-1]:
        for Y in gen_compl(X,0,[]):
            for Z in gen_line(Y,0,[]):
                memo[n][Z] += memo[n-1][X]

def main():
    for i in xrange(1,N):
        base(i)
    s = 0
    for X in memo[N-1]:
        s += memo[N-1][X]
    print s

main()
