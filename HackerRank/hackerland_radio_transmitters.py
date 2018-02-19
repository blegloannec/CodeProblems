#!/usr/bin/env python3

# glouton, similaire a 101 Hack 39 Goodland Electricity

def optim(k,T):
    cpt = 0
    iu = 0  # indice de la premiere position non couverte
    it = 0  # indice de la prochaine antenne a considerer
    while iu<len(T):
        # on cherche la position la plus a droite qui couvre encore iu
        while it<len(T) and T[it]-k<=T[iu]:
            it += 1
        # on place une antenne en it-1 et on met a jour iu
        cpt += 1
        while iu<len(T) and T[iu]<=T[it-1]+k:
            iu += 1
    return cpt

def main():
    n,k = map(int,input().split())
    T = sorted(map(int,input().split()))
    print(optim(k,T))

main()
