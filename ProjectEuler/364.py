#!/usr/bin/env python3

# On decompose en 3 phases comme dans l'enonce.
# A la fin de la phase 1, la configuration est composee
# de places occupees separees par 1 ou 2 places libres.
# L'ordre dans lequel ces places sont occupees est completement
# arbitraire et peut etre permute librement donc on ne s'interesse
# qu'a la configuration finale de phase 1.
# les blocs de 2 places libres ainsi que les places des deux
# extremites (si elles sont encore libres) sont eligibles en phase 2.
# Les autres ne seront eligibles qu'en phase 3.
# En phase 2 on doit choisir 1 place par bloc de 2 + les extremites,
# toute permutation de l'ordre est acceptable.
# En phase 3 on prend les places restantes et toute permutation de l'ordre
# est acceptable.
# Soit N(e,b1,b2) = le nb de configurations finales de phase 1 comportant
# exactement 0<=e<=2 extremites libres, b1 places libres isolees (hors
# extremites) et b2 blocs de 2 places libres (les extremites sont naturellement
# exclues car si leur voisine est libre elles sont encore eligibles en phase 1).
# Le nb de remplissages associes a une configuration finale de phase 1 de type
# (e,b1,b2) est exactement : N(e,b1,b2) * N1! * 2^b2 * (b2+e)! * (b1+b2)!
# avec N1 = N - (e+b1+2*b2) le nb de places occupees en phase 1.
# Il suffit donc de savoir calculer les N(e,b1,b2).
# N(e,b1,b2) = binom(b1+b2,b1)    si e = 0 ou 2
#              2*binom(b1+b2,b1)  si e = 1

P = 10**8+7
N = 10**6
F = [1] # factorielles modulo
for n in range(1,N+1):
    F.append((F[-1]*n)%P)

def bezout(a,b):
    if b==0:
        return (a,1,0)
    g,u,v = bezout(b,a%b)
    return (g,v,u-(a//b)*v)

def inv_mod(a,n):
    _,u,_ = bezout(a,n)
    return u

def binom(n,p):
    return (F[n]*(inv_mod(F[p],P)*inv_mod(F[n-p],P))%P)%P
    
def main():
    cpt = 0
    for e in range(3):
        for N1 in range(N//3,N//2+1):
            # N1 + b1 + 2*b2 + e = N
            # b1+b2 = N1-1
            b2 = N-e-2*N1+1
            b1 = N1-1-b2
            if b1<0 or b2<0:
                continue
            cpt = (cpt + ((1+e%2)*binom(b1+b2,b1) * (F[N-e-b1-2*b2] * (pow(2,b2,P) * (F[b2+e] * F[b1+b2])%P)%P)%P)%P)%P
    print(cpt)

main()
