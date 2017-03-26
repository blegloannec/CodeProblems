#!/usr/bin/env python3

from collections import defaultdict

# (x^4+x^3+x^2+x+1)^k = sum( multinom(n ; a,b,c,d,e)*x^(4a+3b+2c+d) , a+b+c+d+e=n )
# https://en.wikipedia.org/wiki/Multinomial_theorem
# multinom(k ; a,b,c,d,e) = k! / (a! b! c! d! e!)

# le coeff de degre l est donc
# sum( multinom(n ; a,b,c,d,e), 4a+3b+2c+d=l et a+b+c+d+e=n )

# https://en.wikipedia.org/wiki/Lucas%27s_theorem
# le theoreme de Lucas nous indique que
# binom(n,m) = prod_i( binom(ni,mi) ) mod p premier
# pour ni,mi les chiffres de n et m en base p

# or multinom(n ; m1,...,mk) = prod_i( binom(sum(mj,j=1..i),mi) )
# donc en appliquant Lucas a chaque binom() et en inversant les 2 produits
# on obtient la generalisation de Lucas aux coeff multinomiaux :
# multinom(n ; m1,...,mk) = prod_i( multinom(n@i ; m1@i,...,mk@i) ) mod p
# ou x@i est le i-eme chiffre de l'ecriture de x en base p
# SI n@i = m1@i + ... + mk@i pour tout i
# (ou, autrement dit, il n'y a jamais de retenue dans l'addition au bit i
#  ie m1@i + ... + mk@i < p pour tout i)
# SINON le coeff vaut 0
# voir aussi pour plus de details :
# http://mathoverflow.net/questions/80169/reference-needed-for-lucas-theorem-for-multinomial-coefficients-modulo-a-prime

# pour p = 2, multinom(k ; a,b,c,d,e) = 1 ssi
# pour tout i, ai+bi+ci+di+ei < 2  (chiffres en base 2)
# ie exactement au plus un des 5 vaut 1 et les autres 0
# il s'agit donc de compter le nb de manieres de repartir les
# bits 1 de k parmi les 5 nombres

def Q(k):
    # on calcule les bits 1 de k
    B,i = [],0
    while k:
        if k&1:
            B.append(1<<i)
        k >>= 1
        i += 1
    nb1 = len(B)
    C = defaultdict(int)
    # 1. distribution naive
    #for i in range(5**nb1):
    #    A = [0]*5 #a,b,c,d,e
    #    for j in range(nb1):
    #        A[i%5] += B[j]
    #        i //= 5
    #    C[4*A[0]+3*A[1]+2*A[2]+A[3]] += 1
    # 2. methode plus rapide, facon dp
    C[0] += 1
    for i in range(nb1):
        C0 = dict(C) # copie
        for s in C0:
            for c in range(1,5):
                s0 = s+c*B[i]
                C[s0] += C0[s]
    # on compte
    res = 0
    for x in C:
        if C[x]%2==1:
            res += 1
    return res

# la methode precedente ne permet pas de calculer le resultat
# pour k au dela de 10^10
# mais on se rend compte que les Q(i) sont : https://oeis.org/A247649
# ce qui donne un moyen d'accelerer le calcul :
# on decoupe l'ecriture binaire de k en blocs separes par deux 0 ou plus
# alors Q(k) est le produit des Q() de chacun des blocs
# sans demonstration, ce resultat est logique car si l'ecart entre 2 bits 1
# est d'au moins deux 0, i.e. un facteur 4, il ne peut pas y avoir de
# collision des degres 4a+3b+2c+d generes de part et d'autre, ainsi on peut
# considerer les ensembles de bits independemment et fabriquer les degres
# en sommant 2 a 2 les degres generes par les 2 ensembles (ce qui ne creera
# pas de collision, d'ou le simple produit des nb de coeffs)

def decomp(n):
    cpt0,x,i = 0,0,0
    D = []
    while n:
        if n&1:
            if cpt0>=2:
                D.append(x)
                x,i = 0,0
            x |= 1<<i
            cpt0 = 0
        else:
            cpt0 += 1
        i += 1
        n >>= 1
    if x:
        D.append(x)
    return D

def Qeff(k):
    res = 1
    for a in decomp(k):
        res *= Q(a)
    return res

print(sum(Qeff(10**i) for i in range(1,19)))
