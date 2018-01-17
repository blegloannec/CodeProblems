#!/usr/bin/env python3

def nb_known(P):
    i,j = P
    cpt = 0
    for di in range(-1,2):
        for dj in range(-1,2):
            if not di==dj==0 and 0<=i+di<h and 0<=j+dj<w and G[i+di][j+dj]!='?':
                cpt += 1
    return cpt

def possible_mine(P):
    i,j = P
    for di in range(-1,2):
        for dj in range(-1,2):
            if not di==dj==0 and 0<=i+di<h and 0<=j+dj<w and G[i+di][j+dj]==0:
                return False
    return True

def up_neigh(P,x):
    i,j = P
    for di in range(-1,2):
        for dj in range(-1,2):
            if not di==dj==0 and 0<=i+di<h and 0<=j+dj<w and G[i+di][j+dj]!='?':
                G[i+di][j+dj] += x

def cleared():
    return all(G[i][j]==0 or G[i][j]=='?' for i in range(h) for j in range(w))

M = []
def backtrack(k=0):
    if k==len(Q):
        return (len(M)==nb and cleared())
    if len(Q)-k>nb-len(M) and backtrack(k+1):
        return True
    if len(M)<nb and possible_mine(Q[k]):
        M.append(Q[k])
        up_neigh(Q[k],-1)
        if backtrack(k+1):
            return True
        up_neigh(Q[k],1)
        M.pop()
    return False

def main():
    global h,w,nb,G,Q
    h,w = map(int,input().split())
    nb = int(input())
    G = [list(input()) for _ in range(h)]
    Q = []
    for i in range(h):
        for j in range(w):
            if G[i][j]=='.':
                G[i][j] = 0
            elif G[i][j]=='?':
                Q.append((i,j))
            else:
                G[i][j] = int(G[i][j])
    Q.sort(key=nb_known)
    assert(backtrack())
    for j,i in sorted((j,i) for (i,j) in M):
        print(j,i)

main()
