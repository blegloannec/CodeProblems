#!/usr/bin/env python3

from fractions import gcd

# imaginons le rectangle repete periodiquement
# de maniere a former une grille et le laser se
# propageant en ligne droite jusqu'au prochain
# point sur la grille

def lcm(a,b):
    return a*b//gcd(a,b)

U,V = map(int,input().split())
k = lcm(U,V)
C = {(0,0):'S',(1,0):'A',(1,1):'B',(0,1):'C'}
print(C[(k//U)%2,(k//V)%2],k)
