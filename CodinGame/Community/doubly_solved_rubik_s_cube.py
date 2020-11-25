#!/usr/bin/env python3

SOL = ('    UUU',
       '    UUU',
       '    UUU',
       '',
       'LLL FFF RRR BBB',
       'LLL FFF RRR BBB',
       'LLL FFF RRR BBB',
       '',
       '    DDD',
       '    DDD',
       '    DDD')

NET = ('    rgs',
       '    hai',
       '    tju',
       '',
       'rht tju uis sgr',
       'kbl lcm mdz zek',
       'vnw wox xpy yqv',
       '',
       '    wox',
       '    nfp',
       '    vqy')

def precomp_cubes():
    Cubes = [[] for _ in range(26)]
    for i,L in enumerate(NET):
        for j,a in enumerate(L):
            if 'a'<=a<='z':
                Cubes[ord(a)-ord('a')].append((i,j))
    return Cubes

CUBES = precomp_cubes()
extract_cubes = lambda Net: [''.join(Net[i][j] for i,j in C) for C in CUBES]

def get_perm(Net0, Net1):
    sig = lambda C: ''.join(sorted(C))
    Net0_cub = extract_cubes(Net0)
    Net1_cub = extract_cubes(Net1)
    Net1_map = {sig(C):i for i,C in enumerate(Net1_cub)}
    cub_perm = [Net1_map[sig(C)] for C in Net0_cub]
    perm = {}
    for k,C in enumerate(Net0_cub):
        for i,c in enumerate(C):
            j = Net1_cub[cub_perm[k]].index(c)
            perm[CUBES[k][i]] = CUBES[cub_perm[k]][j]
    return perm

def main():
    In = [input() for _ in range(11)]
    sol_perm = get_perm(In, SOL)
    Out = [[' ']*len(L) for L in In]
    for (i1,j1),(i2,j2) in sol_perm.items():
        Out[i2][j2] = SOL[i1][j1]
    print('\n'.join(''.join(L) for L in Out))

main()
