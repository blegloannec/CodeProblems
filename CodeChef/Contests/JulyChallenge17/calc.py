#!/usr/bin/env python3

# on a toujours interet a effectuer toutes les
# utilisations du bouton 1 avant celles du bouton 2
# si l'on utilise K fois le bouton 1
# on peut afficher f(K) = K*((N-K)//B) sur l'ecran 2
# en continu, f'(K) = (N-2K) / B s'annule en N/2
# en discret, on ajuste K pour avoir B | N-K

def main():
    T = int(input())
    for _ in range(T):
        N,B = map(int,input().split())
        K = N//2
        K += N%B - K%B
        res = K*((N-K)//B)
        print(res)

main()
