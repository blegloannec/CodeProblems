#!/usr/bin/env python

# un maximix d'ordre n requiert 2(n-2)+1 rotations
# (2 rotations pour placer chacun des n-2 premiers elements
#  puis 1 pour inverser les 2 derniers)

# Partant d'un maximix d'ordre n, on place la separation devant le A
# on retourne le suffixe pour placer le A a la fin,
# puis on retourne le tout pour placer le A au debut.
# On doit alors avoir un maximix d'ordre n-1 a partir de la 2eme
# position (i.e. en ignorant le A bien place).
# En realisant ces etapes a l'envers, on obtient une methode pour
# generer tous les maximix d'ordre n a partir de ceux d'ordre n-1.
# (on a n-2 positions pour le A car il ne doit etre ni au tout debut,
#  ni a la toute fin, on a donc (n-2)! maximix d'ordre n)

def maxigen(n):
    if n==2:
        yield [1,0]
    else:
        for M0 in maxigen(n-1):
            M = map((lambda x: x+1),M0[::-1])
            M.append(0)
            for i in xrange(1,n-1):
                yield M[:i]+M[n-1:i-1:-1]

def to_str(l):
    return ''.join(map((lambda x: chr(x+ord('A'))),l))

def main():
    L = list(maxigen(11))
    L.sort()
    print to_str(L[2010])

main()
