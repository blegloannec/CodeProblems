#!/usr/bin/env python

from math import sqrt,log

# R(10^(n+1)) = sum( R(10^n)*10^(i*10^n), i=0..9 )
#             = R(10^n)*sum( 10^(i*10^n), i=0..(n-1) )
#             = R(10^n)*(1-10^(10^(n+1)))/(1-10^(10^n))
# (d'ailleurs R(x) = (10^x-1)/9
# ce qui permettait egalement de retrouver facilement ce resultat)
# donc si p | R(10^n) alors p | R(10^(n+1))
# et donc p | R(10^k) pour tout k>=n
# du coup si pour tout p<N, on a une borne sup k sur l'eventuel
# plus petit n tel que p | R(10^n), il suffira de tester si
# R(10^k) = 0 mod p

# R(x+1) = 10*R(x)+1 donc les valeurs possibles des R(x)%p
# se trouvent parmi les R(x)%p pour 1<=x<=p
# il existe n tel que p | R(10^n) ssi il existe x = 2^a.5^b <= p
# tel que R(x) = 0 mod p
# auquel cas p | R(10^ppcm(a,b))
# si p < N, alors a <= log2(N) et b <= log5(N)
# et ppcm(a,b) <= a*b <= log2(N)*log5(N)
# ce qui permet d'obtenir une borne sup raisonnable sur n

def sieve_list(N):
    P = [True for _ in xrange(N)]
    L = []
    P[0] = False
    P[1] = False
    for i in xrange(2,N):
        if P[i]:
            L.append(i)
            for k in xrange(2*i,N,i):
                P[k] = False
    return L

def main():
    N = 10**5
    P = sieve_list(N)
    K = (int(log(N,2))+1)*(int(log(N,5))+1)
    # K = 136 pour N = 10^5
    k = 10**K
    S = 0
    for p in P:
        # R(n) = (10^n-1)/9
        # p | R(n) <=> p | (10^n-1)/9 <=> 9p | 10^n-1 <=> 10^n = 1 mod 9p
        if pow(10,k,9*p)!=1:
            S += p
    print S

main()
