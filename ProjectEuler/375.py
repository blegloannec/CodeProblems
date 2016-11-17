#!/usr/bin/env python

# runs in <1m30 with pypy
# could be greatly improved by exploiting
# the periodicity of the sequence S (as the modulus
# is actually 100 times smaller than the problem bound)

def main():
    N = 2*10**9
    S = 290797
    M = 0
    Q = [(0,0,0)]
    for i in xrange(1,N+1):
        S = (S*S)%50515093
        # on cherche la derniere valeur Sk <= Si
        while Q[-1][0]>S:
            Q.pop()
        # Mi = sum( A(j,i), j<=i )
        #    = Mk + (i-k)*Si
        Mi = Q[-1][2]+(i-Q[-1][1])*S
        M += Mi
        Q.append((S,i,Mi))
    print M

main()
