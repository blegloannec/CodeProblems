#!/usr/bin/env python3

# on trie les serpents, on preservera leur ordre
# reste a trouver la position dans la fenetre a laquelle
# commencer la file de serpents
# calculer la distance pour une position donnee coute O(N)
# la distance sera monotone decroissante avant l'optimal,
# puis monotone croissante apres
# on peut donc proceder par recherche dichotomique du min
# (en comparant a chaque fois 2 valeurs consecutives)
# O(N log(B-A))

def main():
    T = int(input())
    for _ in range(T):
        N,L,A,B = map(int,input().split())
        S = list(map(int,input().split()))
        S.sort()
        X = []
        a,b = A,B-L*N
        while a<b:
            m = (a+b)//2
            d0 = sum(abs(S[i]-(m+i*L)) for i in range(N))
            d1 = sum(abs(S[i]-(m+1+i*L)) for i in range(N))
            if d0<d1:
                b = m
            else:
                a = m+1
        print(sum(abs(S[i]-(a+i*L)) for i in range(N)))

main()
