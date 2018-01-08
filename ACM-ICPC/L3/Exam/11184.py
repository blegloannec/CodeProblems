#!/usr/bin/env python3

# la somme des ecarts est n(n+1)/2 et doit en particulier etre paire
# pour pouvoir fermer le cycle
# si n = 4k+1 ou 4k+2, elle est impaire donc pas de solution
# sinon on part de 1 et l'on fait +n, -(n-1), +(n-2), etc, +/-1
# en sautant simplement n/2 (qui sera l'ecart entre le nb final et 1)

def cycle(n):
    C,d,s = [1],n,1
    while d>0:
        C.append(C[-1]+s*d)
        d -= 1
        if d==n//2:
            d -= 1
        s = -s
    return C

def main():
    n = int(input())
    c = 1
    while n>0:
        res = ' '.join(map(str,cycle(n))) if n%4 in [0,3] else '-1'
        print('Case %d: %s' % (c,res))
        c += 1
        n = int(input())

main()
