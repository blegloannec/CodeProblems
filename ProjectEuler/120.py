#!/usr/bin/env python3

# en developpant on obtient (pour a>1) :
# (a-1)^n + (a+1)^n = 2 si n pair et (2na)%a^2 sinon
# 2na = 2(n-2)a + 4a
# donc la sequence des impairs est obtenue par iteration
# de f(x) = (x+2a) % a^2 donc ultimement periodique, etc

def rmax(a):
    vu = set()
    n,x = 1,0
    while (2*n*a)%(a*a) not in vu:
        vu.add((2*n*a)%(a*a))
        n += 2
    return max(2,max(vu))

print(sum(rmax(a) for a in range(3,1001)))
