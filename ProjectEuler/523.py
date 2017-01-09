#!/usr/bin/env python

# Dans le tri d'un tableau de taille n, on n'atteindra le
# dernier element que lorsque les n-1 premiers auront ete
# tries.
# Ainsi, avec proba 1/n le dernier element x est deja le
# plus grand et l'esperance du nb d'etapes est E(n-1).
# Sinon on trie les n-1 premiers elements en E(n-1) etapes
# puis on envoie le dernier element x en premiere position, le plus
# grand se retrouve alors en derniere position et il s'agit de compter
# le nb d'etapes pour inserer x a sa position parmi les n-1 premiers
# elements tries. Si x doit arriver en position 0<=k<=n-2, il faut
# 2^k - 1 etapes.
# Chaque k est equiprobable avec proba 1/n, et l'esperance
# pour k fixe est E(n-1) + 1 + 2^k-1

E = 3.25 # donne par l'enonce pour n=4
for n in xrange(5,31):
    E = sum((E+(2**i if i<n-1 else 0))/n for i in xrange(n))
print E
