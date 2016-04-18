#!/usr/bin/env python

import sys

# Dn d'ordre 2n
# le th. de Cayley dit que tout gp fini d'ordre n est sous-gp de Sn
# (l'action de gp des translations g.x = gx forme un HDG injectif de G dans S(G) ~ Sn)
# Donc Dn sg de S_2n, on cherche donc mieux que 2n...
# 1. Il est clair que Dn sg de Sn :
# on choisit le n-cycle (1,2,...,n) (soit la permutation [2,3,..,n,1])
# pour la rotation, et le produit de transpositions (1,n)(2,n-1)...
# pour la reflection (soit la permutation [n,n-1,...,1])
# (pour n impair, (n+1)/2 est point fixe)
# c'est un choix naturel, parmi de nombreux autres possibles.
# 2. On peut faire beaucoup mieux :
# un produit de cycles disjoints a pour ordre le ppcm de
# tailles des cycles. On peut alors chercher un produit de cycles les
# plus petits possibles dont le ppcm des tailles vaut n.
# Donc si n n'est pas premier, on peut esperer
# realiser Dn dans un Sk avec k<n. Pour cela, on decompose
# n = prod(p_i^a_i) en nb premiers et on pose Pi = p_i^a_i
# (ppcm(Pi) = n et sum(Pi) est minimale pour cela)
# une permutation d'ordre n existe alors dans Sk avec k = sum(Pi)
# et on l'obtient (ainsi que la reflection) en appliquant la
# methode du 1 pour chaque Pi sur des supports disjoints
# (support 1..P1 pour P1, support P1+1..P1+P2 pour P2, etc).
# Exemple : 6 = 2*3, 2+3=5 on va dans S5
# on prend r = (1,2)(3,4,5) = [2,1,4,5,3] et t = [2,1,5,4,3]

def sieve_factors(N):
    P = [True for _ in xrange(N)]
    Factors = [[] for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,N):
        if P[i]:
            Factors[i].append(i)
            for k in xrange(2*i,N,i):
                P[k] = False
                f = i
                while k%f==0:
                    f *= i
                Factors[k].append(f/i)
    return P,Factors

def main():
    P,F = sieve_factors(20001)
    T = int(sys.stdin.readline())
    for t in xrange(T):
        n = int(sys.stdin.readline())
        k = sum(F[n])
        r = [0 for _ in xrange(k)]
        p = [0 for _ in xrange(k)]
        d = 0
        for f in F[n]:
            for i in xrange(f-1):
                r[d+i] = d+i+2
                p[d+i] = d+f-i
            r[d+f-1] = d+1
            p[d+f-1] = d+1
            d += f
        print k
        print ' '.join(map(str,r))
        print ' '.join(map(str,p))

main()
