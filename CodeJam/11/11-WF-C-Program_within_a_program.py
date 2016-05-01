#!/usr/bin/env python

import sys

# Il s'agit de programmer une machine de Turing pour
# s'arreter exactement sur la case N partant de la case 0
# en au plus X etapes et 30 transitions definies.
# La contrainte small est N<=500, X<=500^2
# La contrainte large est N<=5000, X<=150000(~3Nlog(N))
# Impossible de compter jusqu'a N dans les etats (strategie unaire).
# Une possibilite est de coder N en binaire dans les etats,
# de l'ecrire a gauche de la case 0 sur la bande en debut de
# calcul puis de le convertir en unaire par decrementations
# successives sur la partie droite de la bande.
# Cela demande beaucoup d'allers-retours entre le bord droit
# et le bord gauche : N*(N+log(N)) etapes.
# On peut gagner un facteur constant C en ecrivant N/C et
# en ecrivant des blocs de C 1 a droite a chaque fois (plus
# etats particuliers a la fin pour ajuster la position de N%C).
# Cela suffirait pour le small case.
# Pour le large en revanche, il faut autre chose.
# Astuce bidon : on embarque le compteur binaire avec nous en le decalant
# d'une case a chaque fois : 2Nlog(N) etapes suffisent alors !

# les 0/1 binaires seront codes par 1/2

def gen_prog(N):
    trans = {}
    trans[1,1] = ('E',2,0) # start
    trans[1,2] = ('E',4,0)
    trans[2,0] = ('W',6,0) # 0 detected
    trans[2,1] = ('E',2,2) # decr + shift
    trans[2,2] = ('E',4,2)
    trans[3,0] = ('W',5,2) # shift
    trans[3,1] = ('E',4,2)
    trans[3,2] = ('E',3,2)
    trans[4,0] = ('W',5,1)
    trans[4,1] = ('E',4,1)
    trans[4,2] = ('E',3,1)
    trans[5,1] = ('W',5,1) # go back
    trans[5,2] = ('W',5,2)
    trans[5,0] = ('E',1,0)
    trans[6,2] = ('W',6,0) # got back erasing counter
    trans[6,0] = ('R',6,0) # stop
    # ecrire N en binaire vers la droite
    s = 7
    trans[0,0] = ('E',s,N%2+1) # init state
    N /= 2
    while N>1:
        trans[s,0] = ('E',s+1,N%2+1)
        N /= 2
        s += 1
    trans[s,0] = ('W',5,2)
    return trans

def simu(N,printing=True):
    prog = gen_prog(N)
    p = 0
    s = 0
    tape = [0 for _ in xrange(N+20)]
    while True:
        if printing:
            print '%s[%d]%s' % (''.join(map(str,tape[:p])),s,''.join(map(str,tape[p:])))
        if not ((s,tape[p]) in prog):
            print 'UNDEFINED'
            return
        d,ns,m = prog[s,tape[p]]
        if d=='R':
            print 'HALT',p
            return
        tape[p] = m
        p += 1 if d=='E' else -1
        s = ns
    
        
def main():
    T = int(sys.stdin.readline())
    for t in range(1,T+1):
        N = int(sys.stdin.readline())
        #print N
        if N==0:
            print 'Case #%d: 1' % (t)
            print '0 0 -> R'
            continue
        if N==1:
            print 'Case #%d: 2' % (t)
            print '0 0 -> E 1 0'
            print '1 0 -> R'
            continue
        prog = gen_prog(N)
        print 'Case #%d: %d' %(t,len(prog))
        #simu(N,False)
        #continue
        for (s,m) in prog:
            d,ns,nm = prog[s,m]
            if d=='R':
                print '%d %d -> R' % (s,m)
            else:
                print '%d %d -> %s %d %d' % (s,m,d,ns,nm)

main()
