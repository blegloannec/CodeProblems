#!/usr/bin/env python3

# Il est equivalent de considerer que les fourmis se croisent sans faire
# demi-tour (cela revient a echanger les 2 fourmis lorsqu'elles se rencontrent
# et cela n'a aucune incidence sur le probleme).
# Une fourmi se deplace a 0.1 m/s, la piste fait 10^3 m, une fourmi
# fait le tour en 10^4 s. Deux fourmis qui se deplacent dans le meme
# sens ne se recontrent jamais, deux fourmis qui se deplacent en sens
# contraire se rencontrent exactement 2 fois par tour (aux 2 "milieux" de
# leurs points de depart sur la piste circulaire), ce qui fait 4 saluts.
# Si l'on a a foumis en sens direct et b en sens indirect, on a 4*a*b
# saluts par tours. Pour maximiser, on prend a ~= b ~= N/2.
# En 10^9+6 s, on fait 10^5 tours + 6 s.
# Deux fourmis initialement separees d'un nb pair/impair de m se rencontrent
# sur des positions entieres/demi-entieres en m.
# En 6 s, seules des fourmis initialement separees de 1 m peuvent se croiser.
# Pour maximiser les saluts lors des 6 s restantes, on regarde les "chaines"
# de fourmis initialement separees de 1 m et on choisit leurs orientations
# de maniere a maximiser les rencontres a 5s : pour une chaine de c fourmis,
# on a au max floor(c/2) rencontres a t = 5s (ex. c=4, x-> <-x     x-> <-x)
# (et comme ce choix est fait par paires, il est compatible avec le choix
# a ~= b ~= N/2).

def main():
    N = int(input())
    V = sorted(map(int,input().split()))
    C = [1]  # tailles des chaines de fourmis distantes de 1m
    for i in range(1,N):
        if V[i]-V[i-1]==1:
            C[-1] += 1
        else:
            C.append(1)
    if V[0]+1000-V[N-1]==1:  # fermeture de la boucle
        C[0] += C.pop()
    # 10^5 tours
    a = N//2
    res = 400000*a*(N-a)
    # 6 s restantes
    for c in C:
        res += 2*(c//2)
    print(res)

main()
