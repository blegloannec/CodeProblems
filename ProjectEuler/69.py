#!/usr/bin/env python

def sieve_decomp(N):
    P = [True for _ in xrange(N)]
    Decomp = [[] for _ in xrange(N)]
    P[0] = False
    P[1] = False
    for i in xrange(2,N):
        if P[i]:
            Decomp[i].append((i,1))
            for k in xrange(2*i,N,i):
                P[k] = False
                m = 1
                l = k/i
                while l%i==0:
                    l /= i
                    m += 1
                Decomp[k].append((i,m))
    return P,Decomp

def euler(decomp):
    res = 1
    for (p,m) in decomp:
        res *= (p-1)*(p**(m-1))
    return res

# NB: seul le rapport n/phi(n) nous interesse ici
# or phi(n)/n = Prod( 1 - 1/p, p facteur premier de n)
# on pourrait donc ameliorer ce code en n'utilisant un crible
# ne determinant que les facteurs premiers (sans leur multiplicite)
# et un calcul direct de n/phi(n)

# NB2: au passage, phi(n) = n*Prod( 1 - 1/p, p facteur premier de n)
# donc phi(n) est calculable a partir des facteurs seuls (sans multiplicite)
# mais ce calcul est a base de float, alors qu'on le fait ici en int

# Meilleure solution (a posteriori) :
# n/phi(n) = Prod( p/(p-1), p facteur premier de n)
# est maximise lorsqu'il y a un maximum de facteurs premiers distincts
# (la multiplicite ne joue pas) et qu'ils sont les plus petits possibles
# (ainsi les p/(p-1) sont les plus grands possibles)
# la solution est donc le plus grand produit 2*3*5*7*11*... inferieur a 10^6

def main():
    N = 1000001
    _,Decomp = sieve_decomp(N)
    nphimax = 0
    for n in xrange(2,N):
        nphi = float(n)/euler(Decomp[n])
        #print n,nphi
        if nphi>nphimax:
            nphimax = nphi
            nmax = n
    print nmax

main()
