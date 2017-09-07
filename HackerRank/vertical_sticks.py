#!/usr/bin/env python3

M = 51
F = [1]*M
B = [[int(i==0) for i in range(M)] for _ in range(M)]
for i in range(1,M):
    F[i] = i*F[i-1]
    for j in range(1,i+1):
        B[i][j] = B[i-1][j-1]+B[i-1][j]
        
def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        Y = sorted(map(int,input().split()))
        E = 0
        for i in range(N):
            if i>0 and Y[i]==Y[i-1]:
                # doublon, on reprend la valeur precedente
                E += Ei
                continue
            Ei = 0  # esperance de v pour la valeur Y[i]
            # NB: comme on a traite le cas des doublons precedemment,
            #     alors ici i est la premiere occurrence de la valeur Y[i]
            # il y a  i elements < Y[i], donc v ne peut depasser i+1
            # il y a N-i-1 elements >= Y[i]
            for v in range(1,i+2):
                # Y[i] en position v (blocage par le bord gauche)
                Ei += v * B[i][v-1]*F[v-1] * F[N-v] / F[N]
                # Y[i] en position > v, N-v positions possibles
                # il faut choisir un element >= Y[i] pour bloquer
                Ei += v * (N-v) * (N-i-1)*B[i][v-1]*F[v-1] * F[N-v-1] / F[N]
            E += Ei
        print('%.2f' % round(E,2))

main()
