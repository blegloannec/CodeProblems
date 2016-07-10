#!/usr/bin/env python3

import sys

# modulo a^2
# (a-1)^n + (a+1)^n = 2 si n pair et 2na sinon
# 2na % a^2 est maximise pour n = (a-1)/2 si a impair et n = (a-2)/2 si a pair
# soit a*(a-1) si a impair et a*(a-2) si a pair
# soit a*(a-2+a%2)

# modulo a^3
# (a-1)^n + (a+1)^n = 2na si n impair et 2 + 2*binom(n,2)*a^2 sinon
# de facon similaire au cas du modulo a^2
# 2na % a^3 est maximise par a*(a*a-2+(a*a)%2)
# et l'autre valeur est toujours moins bonne (car on s'approche moins
# bien de a avec n(n-1)/2 que l'on ne s'approche de a^2 avec 2n)

# On en deduit les formules exactes pour les sommes...

P = 10**9+7

def S2(A):
    B = (A-1)/2
    return 3 + A*(A+1)*(2*A+1)/6 - A*(A+1) + B*(B+1) + B

def S3(A):
    B = (A-1)/2
    return 1 + A*A*(A+1)*(A+1)/4 - A*(A+1) + B*(B+1) + B

def main():
    T = int(sys.stdin.readline())
    for _ in xrange(T):
        A,e = map(int,sys.stdin.readline().split())
        if A==1:
            print 0
            continue
        if e==2:
            #s = 2
            #for a in xrange(3,A+1):
            #    s = (s+a*(a-2+a%2))%P
            #     print s,S2(a)
            print S2(A)%P
        else:
            #s = 0
            #for a in xrange(2,A+1):
            #    s = s + a*(a*a-2+(a*a)%2)
            #    print s,S3(a)
            print S3(A)%P

main()
