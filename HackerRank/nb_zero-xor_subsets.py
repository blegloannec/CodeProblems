#!/usr/bin/env python3

# E = {1,...,2^N-1}
# Posons B = {2^0,2^1,...,2^(N-1)} les puissances de 2 dans E
# (i.e. les valeurs avec exactement 1 bit a 1)
# et A = E\B.
# Si X inclus dans E est de xor nul, alors X est parfaitement caracterise
# par Y = X inter A, car on sait alors exactement et de facon unique completer
# Y en X avec des elements de B (ajouter les elements correspondant aux bits
# a 1 de xor(Y)). Il y a donc exactement autant de sous-ensembles de xor nul
# dans E que de sous-ensembles de A (de cardinal |E|-|B| = 2^N-N)
# i.e. 2^(2^N-N).

P = 10**9+7
Phi = P-1

T = int(input())
for _ in range(T):
    N = int(input())
    print(pow(2,(pow(2,N,Phi)-N)%Phi,P))
