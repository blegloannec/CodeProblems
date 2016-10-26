#!/usr/bin/env python

# comme il y a au plus n restes modulo n
# et qu'on regarde la sequence des iteres de
# f(x) = (10*x+1)%n, on a A(n)<=n
def A(n):
    a = 1
    i = 1
    while a!=0:
        a = (10*a+1)%n
        i += 1
    return i

# NB: la sequence des iteres modulo n etant periodique (on part de 0),
# les valeurs de k pour lesquelles n | R(k) sont *exactement* les
# multiples de A(n)
# en particulier, A(n) | k <=> n | R(k)

def main():
    M = 1000000
    a = 0
    # comme A(n)<=n, on commence a M+1 impair
    # en esperant tomber sur la solution rapidement
    i = M+1
    while a<=M:
        i += 2
        if i%5!=0:
            a = A(i)
    print i

main()
