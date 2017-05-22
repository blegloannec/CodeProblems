#!/usr/bin/env python3

# 11..1 N fois est le "repunit" R(N)
# R(N) = (10^n-1) / 9 (somme geometrique)
# calculable simplement %M si M est premier avec 9, i.e. avec 3
# si M est multiple de 3 en revanche, on peut decomposer M = 3^k * M'
# faire les calculs modulo 3^k et M' et recomposer par th. chinois
# le pb est que modulo 3^k, on ne sait pas trop... on sait seulement
# que R(n)%3 = n%3 et R(n)%9 = n%9

# du coup changement de methode, on peut faire une somme geometrique rapide
# en O(log n) en exploitant le fait que :
# 1 + a + a^2 + ... + a^(2n+1) = (1 + a) * (1 + (a^2) + (a^2)^2 + ... + (a^2)^n)
# 1 + a + a^2 + ... + a^2n = 1 + a * (1 + a + a^2 + ... + a^(2*n-1))
#                          = 1 + a * (1 + a) * (1 + (a^2) + (a^2)^2 + ... + (a^2)^(n-1))

def geo_sum_mod(r,n,m):
    if n==0:
        return 1
    if n%2==1:
        return ((1+r)*geo_sum_mod((r*r)%m,(n-1)//2,m))%m
    return (1 + r*((1+r)*geo_sum_mod((r*r)%m,n//2-1,m))%m)%m

def main():
    T = int(input())
    for _ in range(T):
        N,M = map(int,input().split())
        print(geo_sum_mod(10,N-1,M))

main()
