#!/usr/bin/env python

from collections import defaultdict

# not really optimized DP-ish approach, yet runs in only 0.3s
# similar approach (though simpler) as for pb 189

# NB (a posteriori): gen_line peut se retrouver en appelant gen_succ(0)...

L,H = 32,10

# generer toutes les lignes valides
def gen_line(p=0,X=0):
    if p==L:
        yield X^(1<<L) # on retire la barre superflue de la fin
    else:
        for b in [2,3]:
            if p+b<=L:
                for A in gen_line(p+b,X|(1<<(p+b))):
                    yield A

# generer tous les successeurs valides possibles d'une ligne valide
def gen_succ(X,p=0,Y=0):
    if p==L:
        yield Y^(1<<L)
    else:
        for b in [2,3]:
            if p+b<=L and not (X>>(p+b))&1:
                for A in gen_succ(X,p+b,Y|(1<<(p+b))):
                    yield A

def main():
    # precalcul des successeurs
    succ = defaultdict(list)
    for X in gen_line():
        for Y in gen_succ(X):
            succ[X].append(Y)
    cpt = {}
    for X in gen_line():
        cpt[X] = 1
    for h in xrange(H-1):
        ncpt = defaultdict(int)
        for X in cpt:
            for Y in succ[X]:
                ncpt[Y] += cpt[X]
        cpt = ncpt
    print sum(cpt[X] for X in cpt)

main()
