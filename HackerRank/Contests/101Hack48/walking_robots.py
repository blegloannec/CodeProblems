#!/usr/bin/env python3

# chaque r contribue ssi il existe un l ou d plus loin a sa droite
#        l                            r ou d                gauche
# le resultat est donc le nb de l et r de la chaine dont on retire
# les l au debut et les r a la fin

q = int(input())
for _ in range(q):
    s = input().lstrip('l').rstrip('r')
    print(len(s)-s.count('d'))
