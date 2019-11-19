#!/usr/bin/env python3

import sys

# X0 >= X1 >= ... >= X(2N-1). X0 sera toujours le max de la premiere ligne.
# Si on choisit Xi comme max de la seconde ligne, alors tous les elements
# de X0 a X(i-1) doivent etre places sur la premiere ligne et les
# elements de X(i+1) a la fin peuvent etre repartis ou l'on veut.
# Il est alors optimal de coupler ainsi :
#   X(0) | X(1)   | ... | X(i-1)  || X(2i)   | X(2i+2) | ... | X(2N-2)
#   X(i) | X(i+1) | ... | X(2i-1) || X(2i+1) | X(2i+3) | ... | X(2N-1)
# Modulo quelques pre-calculs, il est aise d'obtenir la valeur correspondante
# en O(1) pour chaque X(i). Reste a essayer chaque X(i), pour 1 <= i <= N.

def icons(N,S):
    Pref = S[:N]
    for i in range(1,N):
        Pref[i] += Pref[i-1]
    Suff2 = S[:]
    for i in range(2*N-3,-1,-1):
        Suff2[i] += Suff2[i+2]
    Suff2.append(0)
    return min((S[0]+S[i])*(Pref[i-1]+Suff2[2*i]) for i in range(1,N+1))

def main():
    N = int(sys.stdin.readline())
    S = [int(sys.stdin.readline()) for _ in range(2*N)]
    sys.stdout.write('%d\n' % icons(N,S))

main()
