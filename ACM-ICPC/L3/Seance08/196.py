#!/usr/bin/env python3

def label2coord(L):
    c = i = 0
    while 'A'<=L[i]<='Z':
        c = 26*c + ord(L[i])-ord('A') + 1
        i += 1
    r = int(L[i:])
    return r-1, c-1

def topospread():
    PredCnt = [[0]*C for _ in range(R)]
    Succ = [[[] for _ in range(C)] for _ in range(R)]
    Q = []
    for r in range(R):
        for c in range(C):
            if S[r][c][0]=='=':
                Pred = S[r][c][1:].split('+')
                PredCnt[r][c] = len(Pred)
                for cell in Pred:
                    r0,c0 = label2coord(cell)
                    Succ[r0][c0].append((r,c))
                S[r][c] = 0
            else:
                S[r][c] = int(S[r][c])
                Q.append((r,c))
    while Q:  # topo sort
        r,c = Q.pop()
        for r1,c1 in Succ[r][c]:
            S[r1][c1] += S[r][c]
            PredCnt[r1][c1] -= 1
            if PredCnt[r1][c1]==0:
                Q.append((r1,c1))

if __name__=='__main__':
    T = int(input())
    for _ in range(T):
        C,R = map(int,input().split())
        S = [input().split() for _ in range(R)]
        topospread()
        print('\n'.join(' '.join(map(str,L)) for L in S))
