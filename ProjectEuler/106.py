#!/usr/bin/env python

# comme la condition 2 est deja verifiee
# il suffit de tester les sous-ensembles de meme cardinal
# si de plus on veut tester A = {X_a1 < ... < X_an} et B = {X_b1 < ... < X_bn}
# mais que pour tout i, ai < bi, alors X_ai < X_bi, et donc S(A) < S(B)
# donc ce n'est pas la peine de tester A et B
# autrement dit on doit tester seulement les sous-ensembles pour lesquels les
# ensembles d'indices "se croisent" : il existe i,j tels que ai<bi et aj>bj

def enum(n):
    i = 0
    s = []
    while n>0:
        if n&1:
            s.append(i)
        n >>= 1
        i += 1
    return s

def sub(n):
    cpt = 0
    for s1 in xrange(1,1<<n):
        e1 = enum(s1)
        for s2 in xrange(s1+1,1<<n):
            if s1&s2==0:
                e2 = enum(s2)
                if len(e1)==len(e2):
                    test = False
                    for i in xrange(len(e1)):
                        if e1[i]>e2[i]:
                            cpt += 1
                            break
    return cpt

print sub(12)
