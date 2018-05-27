#!/usr/bin/env python3

def find(x):
    if T[x]<0:
        return x
    T[x] = find(T[x])
    return T[x]

def union(x,y):
    x0,y0 = find(x),find(y)
    if x0!=y0 and sum(S[x0])+sum(S[y0])<=B and all(S[x0][g]+S[y0][g]<=L[g] for g in range(3)):
        T[y0] = x0
        for i in range(3):
            S[x0][i] += S[y0][i]

def main():
    global L,B,T,S
    N,M,A,B,f,s,t = map(int,input().split())
    L = [f,s,t]
    T = [-1]*N
    S = [[0,0,0] for _ in range(N)]
    Name = [None]*N
    Grd = [None]*N
    Name2Id = {}
    for i in range(N):
        Name[i],Grd[i] = input().split()
        Grd[i] = int(Grd[i])-1
        Name2Id[Name[i]] = i
        S[i][Grd[i]] = 1
    for _ in range(M):
        x,y = input().split()
        X = Name2Id[x]
        Y = Name2Id[y]
        union(X,Y)
    smax = 0
    H = set()
    for x in range(N):
        if find(x)==x:
            s = sum(S[x])
            if s>=A:
                if s>smax:
                    H.clear()
                    H.add(x)
                    smax = s
                elif s==smax:
                    H.add(x)
    R = []
    for x in range(N):
        if find(x) in H:
            R.append(Name[x])
    if R:
        R.sort()
        for r in R:
            print(r)
    else:
        print('no groups')    

main()
