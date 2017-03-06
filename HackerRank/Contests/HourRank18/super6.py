#!/usr/bin/env python3

# Prog. Dyn. en O(n)
# on parcourt S de gauche a droite
# a chaque instant, on maintient pour tout 0 <= x < 6,
# R[x] = nb de facteurs de S se terminant en la position
#        courante et dont la valeur modulo 6 est x

S = input()
R = [0]*6
T = 0
for s in S:
    y = int(s)
    # anciens facteurs prolonges
    R0 = [0]*6
    for x in range(6):
        R0[(10*x+y)%6] += R[x]
    R = R0
    # nouveau facteur de taille 1
    if y!=0:
        R[y%6] += 1
    else: # cas particulier de "0"
        T += 1
    T += R[0]
print(T)
