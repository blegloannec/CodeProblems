#!/usr/bin/env python3

adj = lambda a,b: abs(a-b)%8==1

# C = correct, A = adjacent, I = incorrect
def hypothesis(C,A):
    assert all(len(s)<=1 for s in Nums[C])
    I = 3-C-A
    Comb = [next(iter(s)) if s else None for s in Nums[C]]
    for j in range(L):
        if Comb[j] is not None:
            assert all(adj(Comb[j],a) for a in Nums[A][j])
            assert all(not adj(Comb[j],a) for a in Nums[I][j])
        else:
            H = [d for d in range(10) if d not in Nums[I][j] and \
                 all(adj(d,a) for a in Nums[A][j]) and all(not adj(d,a) for a in Nums[I][j])]
            assert len(H)==1
            Comb[j] = H[0]
    return tuple(Comb)

if __name__=='__main__':
    N = int(input())
    L = int(input())
    Attempts = [list(map(int,input().split())) for _ in range(N)]
    Sounds = [['AIU'.index(S[2]) for S in input().split()] for _ in range(N)]
    Nums = [[set() for _ in range(L)] for _ in range(3)]
    for i in range(N):
        for j in range(L):
            Nums[Sounds[i][j]][j].add(Attempts[i][j])
    Combs = set()
    for C in range(3):
        for A in range(3):
            if A!=C:
                try:
                    Combs.add(hypothesis(C,A))
                except:
                    pass
    if len(Combs)==1:
        print(*next(iter(Combs)))
    else:
        print('FLEE')
