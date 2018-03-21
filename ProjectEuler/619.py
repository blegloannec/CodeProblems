#!/usr/bin/env python3

# Soit (p_i)_i la suite des nb premiers.
# A chaque n>=1, on associe la suite binaire X(n) ultimement nulle
# telle que X(n)_i = (valuation p_i-adique de n) modulo 2.
# Il s'agit de denombrer les sous-ensembles de [A,B] dont le xor des
# X(.) est nul.
# Meme idee que pour les sous-ensembles de xor nul de [1,2^n[
# (cf. eg. HR/nb_zero-xor_subsets.py ou la remarque dans PE 409).
# Si [A,B] est assez grand et pour k le nb de nombres premiers apparaissant
# dans les decompositions des nb de [A,B] (i.e. le nb de bits "utiles" des X),
# il existe "certainement" un sous-ensemble E de taille k de [A,B] dont les
# xor des sous-ensembles sont distincts et forment donc de maniere unique les
# 2^k valeurs utiles possibles. Des lors, pour tout sous-ensemble du
# complementaire de E, il existe une unique maniere de le completer avec
# des elements de E de maniere a obtenir un xor nul.
# La solution est alors 2^(B-A+1-k) - 1 (pour l'ensemble vide).

def sieve_cpt(A,B):
    N = B+1
    cpt = 0
    P = [True]*N
    for i in range(2,N):
        if P[i]:
            for k in range(2*i,N,i):
                P[k] = False
            if B - B%i >= A: # there exists a multiple of i in [A,B]
                cpt += 1
    return cpt

def C(A,B,M):
    return pow(2,B-A+1-sieve_cpt(A,B),M)-1

print(C(1000000,1234567,10**9+7))
