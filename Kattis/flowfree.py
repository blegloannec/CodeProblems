#!/usr/bin/env python3

S = 4

def gen_paths(u, uf, path):
    if u==uf:
        yield path
    else:
        i,j = divmod(u, S)
        for vi,vj in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
            if 0<=vi<S and 0<=vj<S:
                v = vi*S+vj
                if (G[v]=='W' or v==uf) and (path>>v)&1==0:
                    yield from gen_paths(v, uf, path|(1<<v))

def main():
    global G
    G = ''.join(input() for _ in range(S))
    C = {}
    for u,c in enumerate(G):
        if c!='W':
            if c not in C:
                C[c] = [u]
            else:
                C[c].append(u)
    Cov = {0}
    for u0,uf in C.values():
        NewCov = set()
        for m in gen_paths(u0, uf, 1<<u0):
            for c in Cov:
                if c&m==0:
                    NewCov.add(c|m)
        Cov = NewCov
    full = (1<<(S*S))-1
    print('solvable' if full in Cov else 'not solvable')

main()
