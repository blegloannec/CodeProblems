#!/usr/bin/env python3

# Si x | y et x<y alors y = kx avec k>=2 et donc x<=y/2.
# Supposons a = 1. On remarque que X(b) = {b//2+1,...,b} est indivisible car
# chacun de ses elements est plus grand que la moitie de n'importe quel autre.
# Dans le treilli de la divisibilite sur les elements <=b, on cherche une
# antichaine de taille max. Par theoreme de Dilworth cela correspond a une
# plus petite partition en chaines (mais ici on n'a besoin que de l'inegalite
# facile de ce theoreme).
# Considerons la partition en les chaines C(x) = {x * 2^k, k>=0} pour x impair.
# Il y a (b+1)//2 telles chaines, toute antichaine contient au plus un element
# par chaine, donc la taille d'une plus grande antichaine est <=(b+1)//2.
# Or X(b) est de taille (b+1)//2 donc c'est une plus grande antichaine.
# Pour a qcq il suffit de prendre les elements >=a de X(b).

def main():
    t = int(input())
    for _ in range(t):
        a,b,x = map(int,input().split())
        c = max(a,b//2+1)
        if b-c+1<x:
            print(-1)
        else:
            print(' '.join(map(str,range(c,c+x))))

main()
