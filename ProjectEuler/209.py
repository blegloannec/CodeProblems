#!/usr/bin/env python

# tau satisfies the formula iff
# forall X, tau(X) = 1 => tau(F(X)) = 0
def F(X):
    a = X>>5
    b = (X>>4)&1
    c = (X>>3)&1
    return ((X&31)<<1)|(a^(b&c))

# affichons le graphe de la fonction F
def dot():
    G = ['digraph F {']
    for x in xrange(64):
        G.append('%d -> %d;'%(x,F(x)))
    G.append('}')
    print '\n'.join(G)

#dot()
# il n'y a que des cycles independants, de tailles [1,2,3,6,6,46]
# (autrement dit c'est une permutation, encore fallait-il remarquer
#  que la fonction etait inversible...)
# reste a compter le nombre de 2-coloriages d'un cycle de facon
# a ce qu'un 1 soit toujours suivi d'un 0

# nombre de coloriages d'une chaine de taille n
# commencant par a (0 ou 1) et terminant par b
memo = {(1,0,0):1,(1,0,1):0,(1,1,0):0,(1,1,1):1}
def chaine(n,a,b):
    if (n,a,b) in memo:
        return memo[n,a,b]
    res = chaine(n-1,0,b)
    if a==0:
        res += chaine(n-1,1,b)
    memo[n,a,b] = res
    return res

# nb de coloriages d'un cycle de taille n
def cycle(n):
    return chaine(n,0,0)+chaine(n,0,1)+chaine(n,1,0)

# NB: il s'agit des nb de Lucas (variante de Fibonacci)
# http://oeis.org/A000032

def main():
    res = 1
    for n in [1,2,3,6,6,46]:
        res *= cycle(n)
    print res

main()
