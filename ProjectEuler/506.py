#!/usr/bin/env python

# u = 123432 repete periodiquement
# la somme sur la periode est 15 et a 15 on revient a l'offset 0
# de u, donc les nombres d'indices i = 15 à 29 sont obtenu en concatenant une
# rotation de u puis le nombre d'indice i-15, de facon generale le nombre
# d'indice i est obtenu en concatenant i/15 fois la bonne rotation de u
# (cf offsets i%15 ci-dessous) puis le nombre d'indice i%15 (avec par
# convention la representation "vide" pour l'indice 0)
# la sequence des offsets est : 001234035304321

M = 123454321

U = [1,2,3,4,3,2]
Off = [0,0,1,2,3,4,0,3,5,3,0,4,3,2,1]
End = [0,1,2,3,4,32,123,43,2123,432,1234,32123,43212,34321,23432]
Siz = [0,1,1,1,1,2,3,2,4,3,4,5,5,5,5]

def bezout(a,b):
    if b==0:
        return (a,1,0)
    g,u,v = bezout(b,a%b)
    return (g,v,u-(a/b)*v)

def inv_mod(a,n=M):
    g,u,_ = bezout(a,n)
    assert(g==1)
    return u

def main():
    N = 10**14
    P6 = pow(10,6,M)
    I = inv_mod(1-P6)
    S = 0
    for r in xrange(15):
        R = 0 # rotation de U d'offset Off[r]
        for i in xrange(6):
            R = R*10 + U[(i+Off[r])%6]
        # nombres de la forme "RR...REnd[r]"
        # ie sum(R*10^(6i), i) * 10^Siz[r] + End[r]
        # dont la somme est, en posant K ~ N/15 :
        # sum( R*sum((10^6)^i, i=0..k) * 10^Siz[r] + End[r], k=0..K-1 )
        # = sum( R*(1-10^(6(k+1)))/(1-10^6) * 10^Siz[r] + End[r], k=0..K-1 )
        # = R*10^Siz[r]*(K - sum( (10^6)^(k+1), k=0..K-1 ))/(1-10^6) + K*End[r]
        # = R*10^Siz[r]*(K - (1 - (10^6)^K)/(1-10**6))/(1-10^6) + K*End[r]
        K = N/15+int(r<=N%15)
        S = (S + R*pow(10,Siz[r],M)*(K-(1-pow(P6,K,M))*I)*I+K*End[r])%M
    print S

main()
