#!/usr/bin/env pypy

def mex(S):
    x = 0
    while x in S:
        x += 1
    return x

# returns (grundy, #{winning moves}) of a subgrid
def grundy_count(r0,c0,r1,c1):  # r0, c0 included; r1, c1 excluded
    key = (r0,c0,r1,c1)
    if r0>=r1 or c0>=c1:
        return (0,0)
    if key not in memo:
        S = set()
        cnt = 0
        for r in xrange(r0,r1):
            if '#' not in G[r][c0:c1]:
                # we place a H in row r, dividing horizontally the grid in 2
                g = grundy_count(r0,c0,r,c1)[0] ^ grundy_count(r+1,c0,r1,c1)[0]
                S.add(g)
                if g==0:
                    cnt += c1-c0
        for c in xrange(c0,c1):
            if all(G[r][c]!='#' for r in xrange(r0,r1)):
                # we place a V in column c, dividing vertically the grid in 2
                g = grundy_count(r0,c0,r1,c)[0] ^ grundy_count(r0,c+1,r1,c1)[0]
                S.add(g)
                if g==0:
                    cnt += r1-r0
        g = mex(S)
        memo[key] = (g,cnt)
    return memo[key]

if __name__=='__main__':
    T = int(raw_input())
    for t in xrange(1,T+1):
        R,C = map(int,raw_input().split())
        G = [raw_input() for _ in xrange(R)]
        memo = {}
        print('Case #%d: %d' % (t, grundy_count(0,0,R,C)[1]))
