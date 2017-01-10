#!/usr/bin/env python

# On ignore les lettres des plaques.
# Le numero 000 n'a pas de complementaire.
# Le numero 500 est son propre complementaire.
# Les autres 998 numeros forment 499 paires de numeros
# complementaires distincts.
# Notons P(C,M,n) la probabilite de ne pas avoir gagne apres
# avoir vu n plaques se repartissant dans 0<=C<=499 categories
# avec complementaire et 0<=M<=1 plaque 500

memo = {}
def P(C,M,n):
    if C+M>n:
        return 0.
    if n==0:
        return 1.
    if (C,M,n) in memo:
        return memo[C,M,n]
    res = P(C,M,n-1)/1000 + C*P(C,M,n-1)/1000 # plaque 0 et categorie deja vue
    if C>0:
        res += (998-2*(C-1))*P(C-1,M,n-1)/1000 # nouvelle categorie
    if M==1:
        res += P(C,0,n-1)/1000 # plaque 500
    memo[C,M,n] = res
    return res

# proba de gagner avec exactement n plaques
def Q(n): 
    res = 0
    for C in xrange(500):
        for M in xrange(2):
            res += P(C,M,n-1)-P(C,M,n)
    return res

# avec seulement 300 on a deja "converge"
print sum(i*Q(i) for i in xrange(2,300))
