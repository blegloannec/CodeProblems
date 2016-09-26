#!/usr/bin/env python

# runs in ~4min with pypy :/

# renvoie un couple de booleens :
# (n n'a que des chiffres <=2, n%10^k n'a que des chiffres <=2)
def test(n,k):
    p = 1
    while n>0:
        if n%10>2:
            return False,(p>=k)
        n /= 10
        p += 1
    return True,True

def f(n):
    # p = 10^a puissance de 10 courante
    p = 1
    a = 0
    # V = valeurs des 0 <= v < p tels que (v*n)%p ne
    #     contient que des chiffres <=2
    # V sera maintenue croissante dans l'algo
    V = [0]
    while True:
        # puissance superieure
        p10 = 10*p
        V10 = []
        # pour chaque v, on teste les valeurs 0 <= v + i*p < 10*p
        # et on retient celles pour lesquelles (n*(v+i*p))%(10*p)
        # ne contient que des chiffres <=2
        # on teste suivant i, puis v croissants pour construire
        # une liste V10 croissante
        for i in xrange(int(p==1),10):
            for v in V:
                v10 = p*i+v
                m = n*v10
                sol,valid = test(m,a)
                if sol:
                    # comme on teste suivant i, puis v, croissants
                    # la premiere solution trouvee est la plus petite
                    return v10
                if valid:
                    V10.append(v10)
        V = V10
        p = p10
        a += 1

print sum(f(n) for n in xrange(1,10001))
