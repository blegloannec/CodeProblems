#!/usr/bin/env python3

def verif(C,B,G):
    P = [1]*C
    for i in range(len(G)):
        Q = [0]*C
        for j in range(C):
            if G[i][j]=='/':
                Q[j-1] += P[j]
            elif G[i][j]=='\\':
                Q[j+1] += P[j]
            else:
                Q[j] += P[j]
        P = Q
    return P==B

def main():
    T = int(input())
    for t in range(1,T+1):
        C = int(input())
        B = list(map(int,input().split()))
        if B[0]==0 or B[C-1]==0:
            print('Case #%d: IMPOSSIBLE' % t)
            continue
        k = 0
        P = [0]*C
        for i in range(C):
            b = B[i]
            while b>0:
                P[k] = i
                k += 1
                b -= 1
        D = [P[i]-i for i in range(C)]
        H = max(abs(d) for d in D)+1
        G = [['.']*C for _ in range(H)]
        for i in range(1,C-1):
            if D[i]!=0:
                s = D[i]//abs(D[i])
                y = i
                for x in range(abs(D[i])):
                    G[x][y] = '/' if s<0 else '\\'
                    y += s
        if verif(C,B,G):
            print('Case #%d: %d' % (t,H))
            for L in G:
                print(''.join(L))
        else:
            print('Case #%d: IMPOSSIBLE' % t)

main()
