#!/usr/bin/env python3

# Probleme medium-hard (apparemment il y avait une ancienne version,
# avec des bornes sur la seed donnees en entree, beaucoup plus simple)
# Attaque predictive sur generateur congruentiel lineaire (modulo 2^48 et
# connaissant des valeurs de sortie modulo 1000 disible par 2^3)
# https://en.wikipedia.org/wiki/Linear_congruential_generator

# 1000 = 2^3 * 5^3
# donc les valeurs ai % 2^3 nous donnent les bits 17-19 des seed successives
# 1. Comme les bits >19 de seed n'ont aucune influence sur les bits <=19
# des seed suivantes (c'est d'ailleurs l'une des raisons pour lesquelles
# on jette les 17 bits faibles : avec ce type de generateur, les bits
# des nombres generes sont d'autant plus biaises qu'ils sont faibles),
# on peut brute-forcer les 17 bits faibles (associes aux 3 bits forts
# de a0%8) jusqu'a en trouver qui generent tous les ai%8.
# 2. On peut alors brute-forcer les 31 bits forts, dont on sait qu'ils
# valent a0 modulo 1000 (donc complexite 2^31/1000 ~ 2*10^6), jusqu'a
# trouver la seed qui genere tous les ai.

M = (1<<48)-1
A = 0x5DEECE66D
B = 0xB

def nextInt(n):
    global seed
    seed = (A*seed + B) & M
    return (seed>>17) % n 

def guess17low(A):
    global seed
    seed3 = (A[0]&7)<<17
    for s17 in range(1<<17):
        seed = seed3 | s17
        i = 1
        while i<len(A) and nextInt(8)==A[i]&7:
            i += 1
        if i==len(A):
            yield s17

def guess31high(A,low17):
    global seed
    for s31 in range(A[0],1<<31,1000):  # O(10^6)
        seed = (s31<<17) | low17
        i = 1
        while i<len(A) and nextInt(1000)==A[i]:
            i += 1
        if i==len(A):
            yield s31

def guess_seed(A):
    for low17 in guess17low(A):
        for high31 in guess31high(A,low17):
            return (high31<<17) | low17

def main():
    global seed
    N = int(input())
    for _ in range(N):
        A = list(map(int,input().split()))
        seed = guess_seed(A)
        for _ in range(9):
            nextInt(1000)
        print(*(nextInt(1000) for _ in range(10)))
main()
