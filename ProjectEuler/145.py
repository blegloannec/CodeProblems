#!/usr/bin/env python

# init chiante de la progdyn
memo = {(0,0,0):1, (0,1,0):0, (0,0,1):0, (0,1,1):0, (1,0,0):0, (1,0,1):0, (1,1,0):0, (1,1,1):0}
for a in xrange(10):
    if (a+a)%2==1:
        memo[1,0,(a+a)/10] += 1
    else:
        memo[1,1,(a+a+1)/10] += 1

# progdyn(n,rin,rout) est le nb de nb a n chiffres (incluant
# les 0 en debut et fin) dont la somme n rev(n) n'a que des
# chiffrs impairs lorsque l'on commence la somme avec la retenue
# rin et qu'il sort une retenue rout
# ainsi, pour tout (a,b), on considere :
# rout <- a___(n-2)___b <- rin
# avec a+b+rin impair
# et un progdyn(n-2,(a+b+rin)/10,rin) au milieu
# et (a+b+rin)/10 == rout
# + on ajoute un param a0 pour le "cas limite" dans lequel
# les leading 0 sont interdits (dans ce cas on appelle avec a0=1)
def progdyn(n,rin,rout,a0=0):
    if a0==0 and (n,rin,rout) in memo:
        return memo[n,rin,rout]
    res = 0
    for a in xrange(a0,10):
        for b in xrange(a0,10):
            if (a+b+rin)/10==rout and (a+b+rin)%2==1:
                res += progdyn(n-2,rout,rin)
    if a0==0:
        memo[n,rin,rout] = res
    return res

def main():
    cpt = 0
    for n in xrange(2,10):
        cpt += progdyn(n,0,0,1)+progdyn(n,0,1,1)
    print cpt

main()
