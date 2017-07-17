#!/usr/bin/env python3

# le nb d'arbres est catalan(n)  (cf. nb de Catalan)
# la probabilite que la racine n'ait qu'un fils est
# catalan(n-1) / catalan(n)
# par symetrie (?) l'esperance du nb de sommets
# n'ayant qu'un fils est n * esperance de la racine

P1,P2 = 10**9+7,10**9+9

def inv_mod(n,p):
    return pow(n,p-2,p)

def E(n,p):
    return (n*(n+1)*inv_mod(2*(2*n-1),p))%p

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())-1
        print(E(N,P1),E(N,P2))

main()
