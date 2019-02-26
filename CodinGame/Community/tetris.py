#!/usr/bin/env python3

# Lame puzzle...
# NB: "you do not need to ensure that a path effectively exists
#      or that the shape is effectively resting on another one"

def compat(i,j):
    for x in range(SH):
        for y in S[x]:
            if F[i+x][j+y]=='*':
                return -1
    return sum(int(Free[i+x]==len(S[x])) for x in range(SH))

if __name__=='__main__':
    SW,SH = map(int,input().split())
    S = [[y for y,c in enumerate(input()) if c=='*'] for _ in range(SH)]
    FW,FH = map(int,input().split())
    F = [input() for _ in range(FH)]
    Free = [L.count('.') for L in F]
    l,i,j = max((compat(i,j),i,j) for i in range(FH-SH+1) for j in range(FW-SW+1))
    print(j,FH-1-i)
    print(l)
