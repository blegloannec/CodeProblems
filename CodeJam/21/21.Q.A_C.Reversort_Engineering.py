#!/usr/bin/env python3

def reverse(L, i, j):
    while i<j:
        L[i],L[j] = L[j],L[i]
        i += 1
        j -= 1

def reversort(L):
    cost = 0
    for i in range(len(L)-1):
        j = min(range(i,len(L)), key=(lambda j: L[j]))
        reverse(L, i, j)
        cost += j-i+1
    return cost

def mainA():
    T = int(input())
    for t in range(1, T+1):
        N = int(input())
        L = list(map(int, input().split()))
        cost = reversort(L)
        print(f'Case #{t}: {cost}')

def gen(N, C):
    if C<N-1:
        return None
    C -= N-1
    L = [N]
    for i in range(N-1, 0, -1):
        j = min(C, len(L))
        L = L[:j][::-1] + [i] + L[j:]
        C -= j
    return L if C==0 else None

def mainC():
    T = int(input())
    for t in range(1, T+1):
        N,C = map(int, input().split())
        L = gen(N, C)
        if L is None:
            print(f'Case #{t}: IMPOSSIBLE')
        else:
            print(f'Case #{t}: {" ".join(map(str, L))}')

#mainA()
mainC()
