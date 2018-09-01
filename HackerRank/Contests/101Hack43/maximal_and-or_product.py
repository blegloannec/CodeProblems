#!/usr/bin/env python

import sys

# soit opt(E,n) la paire optimale parmi les nombres
# de l'ensemble E dont on ne garde que les n bits de poids faible
# soit E = E0 U E1 la partition de E selon le n-ieme bit
# - si E0 ou E1 est vide, la solution est opt(E,n-1)
# - si |E1| >= 2, alors la paire solution est clairement dans E1
#   (car le pire cas possible (10^(n-1),10^(n-1)) dans E1 reste meilleur
#   que le meilleur cas (1^(n-1),1^(n-1)) possible dans S0)
#   et c'est donc assez clairement opt(E1,n-1)
# - sinon E1 est un singleton et la paire solution est soit
#   cet element et un element de E0, soit opt(E0,n-1)

def bit(a,n):
    return (a>>n)&1

def f(x,y):
    return (x&y)*(x|y)

def opt(E,n):
    if len(E)<2:
        return -1
    if n<0: # nombres de E forcement identiques
        return f(E[0],E[0])
    P = [[],[]]
    for x in E:
        P[bit(x,n)].append(x)
    if len(P[0])==0 or len(P[1])==0:
        return opt(E,n-1)
    elif len(P[1])>1:
        return opt(P[1],n-1)
    else:
        res = 0
        x = P[1][0]
        for y in P[0]:
            res = max(res,f(x,y))
        return max(res,opt(P[0],n-1))

def main():
    n = int(sys.stdin.readline())
    A = map(int,sys.stdin.readline().split())
    print opt(A,29)

main()
