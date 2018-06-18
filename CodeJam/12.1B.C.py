#!/usr/bin/python
# -*- coding: utf-8 -*-

'''Solution pour la LARGE input uniquement.
L'astuce consiste a remarquer qu'il y a TOUJOURS une solution de taille 6 !
En effet, par principe des tiroirs : la valeur de toute somme d'un sous-ensemble est
bornee par 500*10^12. Or il y a 2^500 (> 500*10^12) sous-ensembles possibles, donc
il y en a au moins 2 qui ont la même somme.
De plus, si on fixe la taille k des sous-ensembles consideres, on a au plus k*10^12 sommes et
binom(500,k) sous-ensembles. La premiere valeur pour laquelle binom(500,k) > k*10^12 (et donc
pour laquelle on a une solution a coup sur) est k = 6.

L'algo, base sur le principe des anniversaires (il n'y a pas besoin de tirer beaucoup de
sous-ensembles differents pour en trouver 2 de meme somme), consiste alors a tirer aleatoirement
des sous-ensembles de taille 6 jusqu'a en avoir 2 differents de meme somme.

Le seuil a partir duquel on est sur d'avoir toujours une solution (sans
restriction sur la taille, avec nombres <= 10^12) est 46. En revanche,
il faut attendre 48 pour pouvoir se restreindre aux sous-ensembles d'une
taille donnee (en l'occurrence 21). A 50, on peut regarder les
sous-ensembles de taille 18.

Les ensembles de taille 6 fonctionnent a partir de 407, taille 5 a 905,
4 a 3132, 3 a 26209 et 2 a 2000001.

Pour le problème donne, la solution la plus rapide (car minimisant le
nombre de sous-ensembles a considerer) est de regarder les
sous-ensembles de taille 6 sur 407 éléments parmi les 500. Inutile ici
d'essayer de regarder les tailles 7, 8, 9, etc, car même si le nombre
total d'elements a considerer est beaucoup plus petit (235, 158, 119
respectivement), on y perd quand meme sur le nombre de sous-ensembles.

Mais ce qui est amusant, c'est que ce n'est pas toujours le cas (la
fonction n'est pas toujours decroissante) : il vaut mieux regarder les
sous-ensembles de taille 15 parmi 56 (seuil a partir duquel la taille
minimale a considerer passe a 15) que ceux de taille 14 parmi 60 (idem
avec 14). Du coup entre 60 et 63 (a 64 la taille passe a 13, ce qui
redevient plus avantageux), il vaut mieux redescendre a 56.'''

import sys, random
random.seed()

def main():
    entree = sys.stdin.readlines()
    T = int(entree[0])
    for i in range(1,T+1):
        S = map(int,entree[i].split(' '))[1:408]
        D = dict()
        while True:
            sub6 = random.sample(S,6)
            sub6.sort()
            sum6 = sum(sub6)
            if sum6 in D:
                if D[sum6]!=sub6:
                    break
            else:
                D[sum6] = sub6
        print 'Case #'+str(i)+':'
        print ' '.join(map(str,D[sum6]))
        print ' '.join(map(str,sub6))

main()
