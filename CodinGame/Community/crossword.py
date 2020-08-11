#!/usr/bin/env python3

def cross(H,V):
    for i,h in enumerate(H):
        for j,v in enumerate(V):
            if h==v:
                yield (i,j)

def main():
    H1 = input()
    H2 = input()
    V1 = input()
    V2 = input()
    C2 = list(cross(H2,V2))
    cnt = 0
    for h1,v1 in cross(H1,V1):
        for h2,v2 in C2:
            for i in range(len(V1)):
                if abs(i-v1)>1:
                    for j in range(len(H1)):
                        if abs(j-h1)>1 and                               \
                           0<=v2+v1-i<len(V2) and V2[v2+v1-i]==H1[j] and \
                           0<=h2+h1-j<len(H2) and H2[h2+h1-j]==V1[i]:
                            cnt += 1
                            sol = h1,v1,h2,v2,i,j
    if cnt==1:
        h1,v1,h2,v2,i0,j0 = sol
        di = max(0, v2-i0)
        dj = max(0, h2-j0)
        hh = max(len(V1)+di, i0+len(V2)-v2+di)
        ww = max(len(H1)+dj, j0+len(H2)-h2+dj)
        G = [['.']*ww for _ in range(hh)]
        for j,c in enumerate(H1):
            G[v1+di][j+dj] = c
        for i,c in enumerate(V1):
            G[i+di][h1+dj] = c
        for j,c in enumerate(H2):
            G[i0+di][j0-h2+j+dj] = c
        for i,c in enumerate(V2):
            G[i0-v2+i+di][j0+dj] = c
        print('\n'.join(''.join(L) for L in G))
    else:
        print(cnt)

main()
