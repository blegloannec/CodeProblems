#!/usr/bin/env python3

MOD = 7140
A = 7562100%MOD
B = 907598307%MOD
MASK = (1<<8)-1

def RNG_next(R):
    return (A*R+B)%MOD


# Methode 1 : approche sans utiliser l'offset (en exploitant simplement les
# caracteres attendus dans le message clair)...
def seeded_attack(C,R0,M):
    R = R0
    for i in range(1,len(C)):
        R = RNG_next(R)
        m = (R&MASK)^C[i]        
        if 32<=m<=126:
            M.append(m)
        else:
            return False
    return True

def attack(C):
    for R0 in range(C[0]^ord('@'),7140,256):
        M = []
        if seeded_attack(C,R0,M):
            return ''.join(chr(m) for m in M)


# Methode 2 (non implementee) : exploiter le fait que sur les entiers [0,MOD]
# la fonction RNG_next() n'a que 2 cycles (un cycle de taille 16 et dont le
# plus petit element est 147 et une boucle sur 2667) et TOUS les autres
# elements sont DIRECTEMENT envoyes dans un cycle (en une seule application
# de la fonction)... Si l'offset est >=2, ou encore sur le message M[2:],
# il n'y a que 17 seeds possibles...


def main():
    _ = int(input())
    L = int(input())
    C = [int(input()) for _ in range(L)]
    print(attack(C))

main()
