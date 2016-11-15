#!/usr/bin/env python

# C(n) = nb de cycles hamiltoniens de Sn
# H(n) = nb de chemins hamiltoniens de Sn
#        d'un coin a un autre (fixes)
# H'(n) = nb de chemins (presque) hamiltoniens de Sn
#         d'un coin a un autre (fixes) sans
#         passer par le 3eme coin
# clairement C(n) = H(n-1)^3
# H(n) = 2*H'(n-1)*H(n-1)^2
# avec l'init. H(1) = 1
# H'(n) = 2*H(n-1)*H'(n-1)^2
# avec l'init. H'(1) = 1 et H'(2) = 3 (et non 2,
# car il y a un 3eme chemin sans passer par l'interieur
# du triangle median)

# on voit alors que H(n) = 2^(3^(n-2)) * 3^(3^(n-2)/2)
# et C(n) = 2^(3^(n-2)) * 3^((3^(n-3)/2)*3)

# calcul de C(n) mod p avec phi(p) = p
# on utilise Euler : n^phi(p) = 1 mod p pour n et p p-e-e
def Cmod(n,p,phip):
    return (pow(2,pow(3,n-2,phip),p) * pow(3,((pow(3,n-3,phip)/2)*3)%phip,p))%p

def main():
    N = 10000
    P = 13**8
    PhiP = 12*13**7 # 2^2 * 3 * 13^7
    PhiPhiP = 2*2*12*13**6 # 2^4 * 3 * 13^6
    PhiPhiPhiP = 2**3*2*12*13**5
    print Cmod(Cmod(Cmod(N,PhiPhiP,PhiPhiPhiP),PhiP,PhiPhiP),P,PhiP)

main()
