#!/usr/bin/env python3

# NB: recyclage partiel du code de high-rise_buildings.py

S = 10  # 0-9

def prod_pos(C,L,i=0):
    if i==S:
        # non contiguite horizontale des * (-1)
        if not any(L[i]==L[i+1]==-1 for i in range(N-1)):
            yield L[:]  # copy
    else:
        yield from prod_pos(C,L,i+1)
        for j in C[i]:
            L[j] = i
            yield from prod_pos(C,L,i+1)
            L[j] = -1

def precomp():
    # Pos[i] contiendra les configurations possibles pour la ligne i
    Pos = [[] for _ in range(N)]
    for i in range(N):
        C = [[] for _ in range(S)]
        for j in range(N):
            C[G[i][j]].append(j)
        Pos[i] = list(prod_pos(C,[-1]*N))
    return Pos

def dfs(G,i,j,seen):
    seen[i][j] = True
    for vi,vj in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
        if 0<=vi<N and 0<=vj<N and G[i][j]>=0 and not seen[vi][vj]:
            dfs(G,vi,vj,seen)

def is_connected(G):
    seen = [[False]*N for _ in range(N)]
    first = True
    for i in range(N):
        for j in range(N):
            if G[i][j]>=0 and not seen[i][j]:
                if first:
                    dfs(G,i,j,seen)
                    first = False
                else:
                    return False
    return True

def backtrack(Pos,Used,Sol,i=0):
    if i==N:
        # on verifie finalement la connexite
        return is_connected(Sol)
    # on traite la ligne i
    for P in Pos[i]:
        # conditions de "carre latin" et de non contiguite verticale des * (-1)
        if all(P[j]<0 or Used[j]&(1<<P[j])==0 for j in range(N)) and not (i>0 and any(Sol[i-1][j]==P[j]==-1 for j in range(N))):
            Sol[i] = P
            for j in range(N):
                if P[j]>=0:
                    Used[j] ^= 1<<P[j]
            if backtrack(Pos,Used,Sol,i+1):
                return True
            for j in range(N):
                if P[j]>=0:
                    Used[j] ^= 1<<P[j]
    return False

def main():
    global N,G
    N = int(input())
    G = [list(map(int,list(input()))) for _ in range(N)]
    Pos = precomp()
    Used = [0]*N
    Sol = [[-1]*N for _ in range(N)]
    assert(backtrack(Pos,Used,Sol))
    for L in Sol:
        print(''.join(str(c) if c>=0 else '*' for c in L))

main()
