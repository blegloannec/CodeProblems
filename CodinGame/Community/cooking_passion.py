#!/usr/bin/env python3

import re

class Quantity:
    def __init__(self, q, u):
        if u=='kg':
            self.q = int(1000.*float(q))
            self.u = 'g'
        elif u=='L':
            self.q = int(100.*float(q))
            self.u = 'cl'
        else:
            self.q = int(q)
            self.u = u

    def __str__(self):
        if self.u=='g' and self.q>=1000:
            return f'{self.q/1000.}kg'
        elif self.u=='cl' and self.q>=100:
            return f'{self.q/100.}L'
        return f'{self.q}{self.u}'

    def __lt__(self, Q):
        if Q.u!=self.u:
            return self.u=='g'
        return self.q<Q.q

    def divmod(self, Q):
        assert self.u==Q.u
        return divmod(self.q, Q.q)

    def __rmul__(self, k):
        assert isinstance(k, int)
        return Quantity(k*self.q, self.u)

    def __sub__(self, Q):
        assert self.u==Q.u
        return Quantity(self.q-Q.q, self.u)


def main():
    num_recipe, num_ingredients = map(int, input().split())
    Recipe = {}
    for _ in range(num_recipe):
        line = re.fullmatch(r'- ([0-9.]+)(k?g|cl|L) ([a-zA-Z ]+)', input())
        if line:
            quant,unit,ingr = line.groups()
            Recipe[ingr] = Quantity(quant, unit)

    Avail = {}
    for _ in range(num_ingredients):
        line = re.fullmatch(r'([a-zA-Z ]+) ([0-9.]+)(k?g|cl|L)', input())
        ingr,quant,unit = line.groups()
        Avail[ingr] = Quantity(quant, unit)

    nmin = float('inf')
    for i,q in Recipe.items():
        assert i in Avail
        n,r = Avail[i].divmod(q)
        if r==0 and n<nmin:
            imin = i
            nmin = n

    Remain = []
    for i,a in Avail.items():
        if i!=imin:
            assert i in Recipe
            Remain.append((i, a-nmin*Recipe[i]))
    Remain.sort(key=(lambda iq: iq[1]))

    print(imin)
    print(nmin)
    for i,q in Remain:
        print(i,q)

main()
