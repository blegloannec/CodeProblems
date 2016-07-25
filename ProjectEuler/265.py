#!/usr/bin/env python

# https://en.wikipedia.org/wiki/De_Bruijn_sequence
# les cycles de De Bruijn sont les cycles euleriens du
# graphe de De Bruijn d'ordre n-1
# mais c'est un peu penible a enumerer...
# on adopte ici une approche combinatoire moins efficace mais plus simple 
# un cycle de De Bruijn a autant de 0 que de 1 (2^(N-1) de chaque)
# comme on commence par le bloc de N 0, on peut enumerer les sous-ensembles
# a 2^(N-1) elements parmi 2^N-N (choix des positions des 1)
# et filter les cycles de De Bruijn

def subsets(n,c):
    if c==0:
        yield 0
    else:
        for x in xrange(c-1,n):
            for S in subsets(x,c-1):
                yield S | (1<<x)

def test(N,n):
    # on complete n pour le cycle :
    n += n<<(1<<N)
    mask = (1<<N)-1
    seen = [False for _ in xrange(1<<N)]
    for i in xrange(1<<N):
        m = (n>>i)&mask
        if seen[m]:
            return False
        seen[m] = True
    return True
 
def main():
    N = 5
    cpt = 0
    for S in subsets((1<<N)-N,1<<(N-1)):
        if test(N,S):
            cpt += S
    print cpt

main()
