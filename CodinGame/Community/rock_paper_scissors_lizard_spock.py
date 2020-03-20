#!/usr/bin/env python3

S = 'RPCLS'
W = [[ 0,-1, 1, 1,-1],
     [ 1, 0,-1,-1, 1],
     [-1, 1, 0, 1,-1],
     [-1, 1,-1, 0, 1],
     [ 1,-1, 1,-1, 0]]

def win(i,j):
    w = W[Sign[i]][Sign[j]]
    if w==1 or (w==0 and i<j):
        i,j = j,i
    History[j].append(i)
    return j

def main():
    global Sign, History
    N = int(input())
    Sign = [None]*(N+1)
    T = []
    for _ in range(N):
        i,s = input().split()
        i = int(i)
        Sign[i] = S.index(s)
        T.append(i)
    History = [[] for _ in range(N+1)]
    while len(T)>1:
        T = [win(T[i],T[i+1]) for i in range(0,len(T),2)]
    print(T[0])
    print(*History[T[0]])

main()
