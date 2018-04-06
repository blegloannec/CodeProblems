#!/usr/bin/env python3

N = 5
M = N*N

# neighborhood masks precomp
V = [0]*M
for i in range(N):
    for j in range(N):
        u = N*i+j
        for vi in range(i-1,i+2):
            for vj in range(j-1,j+2):
                if (vi,vj)!=(i,j) and 0<=vi<N and 0<=vj<N:
                    V[u] |= 1<<(N*vi+vj)

def elem(x):
    i = 0
    while x:
        if x&1:
            yield i
        x >>= 1
        i += 1

def backtrack(G, Avail, S, i=1):
    if i>M:
        return True
    if G[i]!=None:
        S[i] = G[i]
        P = 1<<G[i]
        if i<=2 or any(V[S[k]] & V[S[i-k]] & P for k in range(1,(i+1)//2)):
            return backtrack(G,Avail,S,i+1)
        return False
    if i<=2:
        P = Avail
    else:
        P = 0
        for k in range(1,(i+1)//2):
            P |= V[S[k]] & V[S[i-k]] & Avail
    for p in elem(P):
        S[i] = p
        if backtrack(G,Avail^(1<<p),S,i+1):
            return True
    return False

def grid(S):
    G = [[0]*N for _ in range(N)]
    for x in range(1,M+1):
        i,j = divmod(S[x],N)
        G[i][j] = x
    return G

def main():
    G = [None]*(M+1)
    Avail = (1<<M)-1
    for i in range(N):
        L = list(map(int,input().split()))
        for j in range(N):
            if L[j]>0:
                G[L[j]] = N*i+j
                Avail ^= 1<<(N*i+j)
    S = [None]*(M+1)
    assert(backtrack(G,Avail,S))
    Sol = grid(S)
    for L in Sol:
        print(*L)

if __name__=='__main__':
    main()
