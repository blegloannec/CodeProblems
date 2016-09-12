#!/usr/bin/env python

# rather naive and dirty approach, yet only takes 2.2s, so...

# generating top dice increasing combinations
def gen_top(d,n,s,a0=1,D=[]):
    if n==0:
        if s==0:
            yield D
    else:
        for a in xrange(a0,d+1):
            if a>s:
                break
            D.append(a)
            for X in gen_top(d,n-1,s-a,a,D):
                yield X
            D.pop()

# generating increasing combinations for the remaining dice
def gen_rem(n,a0,D=[]):
    if n==0:
        yield D
    else:
        for a in xrange(1,a0+1):
            D.append(a)
            for X in gen_rem(n-1,a,D):
                yield X
            D.pop()

def fact(n):
    return 1 if n<2 else n*fact(n-1)

def analyze(d,D,c):
    cpt  = [0 for _ in xrange(d+1)]
    # counting repetitions in top dice
    for x in D:
        cpt[x] += 1
    m = min(D)
    res = 0
    # generate compatible combinations for the remaining dice
    for X in gen_rem(c,m):
        key = tuple(sorted(D+X))
        res0 = fact(len(D)+c)
        cpt0 = cpt[:]
        # counting repetitions in remaining dice
        for x in X:
            cpt0[x] += 1
        # counting top+rem combinations
        for x in cpt0:
            res0 /= fact(x)
        res += res0
    return res

def main():
    c = 0
    #for D in gen_top(6,3,15):
    #    c += analyse(6,D,2)
    for D in gen_top(12,10,70):
        c += analyze(12,D,10)
    print c

main()
