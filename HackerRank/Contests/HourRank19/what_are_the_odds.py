#!/usr/bin/env python3

# Alice gagne si elle force Bob a jouer sur une
# conf de xor nul
# on doit donc compter le nombre d'intervalles dont
# le xor est egal au xor du total

def main():
    n = int(input())
    S = list(map(int,input().split()))
    xor_total = 0
    for s in S:
        xor_total ^= s
    X = [0]*(1<<17) # compteurs des xor des prefixes
    X[0] = 1
    xor_curr,cpt = 0,0
    for s in S:
        xor_curr ^= s
        cpt += X[xor_curr^xor_total]
        X[xor_curr] += 1        
    print(cpt)

main()
