#!/usr/bin/env python

import sys

def winner(x,y):
    X,Y = T[x],T[y]
    ix,iy = len(X)-1,len(Y)-1
    while ix>=0 and iy>=0:
        # descente rapide de k tours jusqu'a la limite du palier
        k = min(X[ix][1]/Y[iy][0],Y[iy][1]/X[ix][0])
        ix -= k*Y[iy][0]
        iy -= k*X[ix][0]
        # descente d'un tour avec garantie de descente de palier
        # pour l'une des 2 equipes
        iy -= X[ix][0]
        if iy>=0:
            ix -= Y[iy][0]
    return (x if iy<0 else y)

def main():
    global T
    n,k,q = map(int,sys.stdin.readline().split())
    T = [[] for _ in xrange(k)]
    for _ in xrange(n):
        s,t = map(int,sys.stdin.readline().split())
        T[t-1].append(s)
    for t in T:
        if len(t)>0:
            # on trie les combattants par force croissante
            t.sort()
            # t[i] = (force du combattant i, nb de combattants <i de meme force)
            t[0] = (t[0],0)
            for i in xrange(1,len(t)):
                if t[i]==t[i-1][0]:
                    t[i] = (t[i],t[i-1][1]+1)
                else:
                    t[i] = (t[i],0)
    for _ in xrange(q):
        c,x,y = map(int,sys.stdin.readline().split())
        if c==1:
            if len(T[y-1])==0 or T[y-1][-1][0]!=x:
                T[y-1].append((x,0))
            else:
                T[y-1].append((x,T[y-1][-1][1]+1))
        else:
            print winner(x-1,y-1)+1

main()
