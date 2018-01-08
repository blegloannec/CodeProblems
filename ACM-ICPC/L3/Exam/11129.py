#!/usr/bin/env python3

# Appelons PAA(n) une permutation 3-anti-arithmetique de taille n
# et SAA une suite finie (qcq) 3-anti-arithmetique.
# Une SAA le reste (clairement) si l'on :
#  - supprime des elements ;
#  - ajoute une constante a tous les elements ;
#  - multiplie tous les elements par une constante.
# Pour construire une PAA(n) :
#  - on construit une SAA sur les elements pairs et une SAA sur les
#    elements impairs a partir d'une PAA(n/2) et des operations precedentes ;
#  - on les concatene.
# On obtient une PAA(n) car tout triplet "a cheval" sur les pairs/impairs
# contient 2 elements de meme parite, dont l'ecart est pair, tandis que l'autre
# ecart est entre un pair et un impair donc est impair.

def aaperm(n):
    if n==1:
        return [0]
    B = aaperm((n+1)//2)
    return [2*x for x in B] + [2*x+1 for x in B if 2*x+1<n]

def main():
    n = int(input())
    while n>0:
        print('%d: %s' % (n,' '.join(map(str,aaperm(n)))))
        n = int(input())

main()
