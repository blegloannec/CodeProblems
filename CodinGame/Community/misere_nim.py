#!/usr/bin/env python3

# a position is losing iff:
#     A. it contains only 1s and has odd size;
#  or B. it contains at least one stack >1 and has xor of stack sizes = 0

def moves(C):
    N = len(C)
    T = [i for i in range(N) if C[i]>1]
    if len(T)==0:   # only 1s
        if N%2==1:  # odd size
            return []
        return [(i,1) for i in range(1,N+1)]
    if N==1:  # 1 stack of size >1
        return [(1,C[0]-1)]
    if len(T)==1 and N%2==0:  # critical position (transition B -> A)
        return [(T[0]+1,C[T[0]])]
    X = 0
    for c in C:
        X ^= c
    M = []
    if X!=0:
        for i in range(N):
            x = X^C[i]
            if x<=C[i]:
                M.append((i+1,C[i]-x))
    return M

def main():
    N,K = map(int,input().split())
    for _ in range(K):
        C = list(map(int,input().split()))
        M = moves(C)
        if M:
            print(' '.join('%d:%d'%m for m in M))
        else:
            print('CONCEDE')

main()
