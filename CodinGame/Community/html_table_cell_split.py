#!/usr/bin/env python3

# really tediously done...

def build_table():
    W = sum(cs for cs,_ in A[0])
    G = [[None]*W]
    r = c = 0
    for L in A:
        for cs,rs in L:
            while G[r][c] is not None:
                while c<W and G[r][c] is not None:
                    c += 1
                if c==W:
                    r,c = r+1,0
                    if r==len(G):
                        G.append([None]*W)
            for i in range(r,r+rs):
                for j in range(c,c+cs):
                    if i==len(G):
                        G.append([None]*W)
                    if (i,j)==(r,c):
                        G[i][j] = ('cell',cs,rs)
                    else:
                        G[i][j] = ('span',c,r)
    return G

def horizontal_split(r,c):
    global G,H
    G = G[:r+1] + [G[r][:]] + G[r+1:]
    H += 1
    updated = set([(c,r)])
    for j in range(W):
        if j!=c:
            t,c0,r0 = G[r+1][j]
            if t=='cell':
                G[r+1][j] = ('span',j,r)
                c0,r0 = j,r
            elif (c0,r0)==(c,r):
                G[r+1][j] = ('span',c,r+1)
            if (c0,r0) not in updated:
                _,cs,rs = G[r0][c0]
                G[r0][c0] = ('cell',cs,rs+1)
                updated.add((c0,r0))

def vertical_split(r,c):
    global G,W
    G = [L[:c+1] + [L[c]] + L[c+1:] for L in G]
    W += 1
    updated = set([(c,r)])
    for i in range(H):
        if i!=r:
            t,c0,r0 = G[i][c+1]
            if t=='cell':
                G[i][c+1] = ('span',c,i)
                c0,r0 = c,i
            elif (c0,r0)==(c,r):
                G[i][c+1] = ('span',c+1,r)
            if (c0,r0) not in updated:
                _,cs,rs = G[r0][c0]
                G[r0][c0] = ('cell',cs+1,rs)
                updated.add((c0,r0))

def split_table():
    k = 0
    for i in range(H):
        for j in range(W):
            if G[i][j][0]=='cell':
                if k==IS:
                    if DS=='R':
                        horizontal_split(i,j)
                    else:
                        vertical_split(i,j)
                    return
                k += 1

def print_table():
    for i in range(H):
        L = []
        for j in range(W):
            t,cs,rs = G[i][j]
            if t=='cell':
                L.append('%d,%d' % (cs,rs))
        if L:
            print(' '.join(L))

if __name__=='__main__':
    NR = int(input())
    A = [[tuple(map(int,c.split(','))) for c in input().split()] for _ in range(NR)]
    IS,DS = input().split()
    IS = int(IS)
    G = build_table()
    H,W = len(G),len(G[0])
    split_table()
    print_table()
