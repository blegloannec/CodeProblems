#!/usr/bin/env python

import sys

# Si ni le dernier, ni le premier siege ne sont disponibles, alors
# on prend le premier siege libre tel que le precedent soit libre.
# En effet, le siege precedent ne sera alors plus "bon", et sera le plus
# a gauche possible pour cela et donc choisi le plus tard possible
# (les sieges libres precedents n'etant deja pas bons, ils seraient
# choisis plus tard de toute facon) et donc la place choisie reste
# bonne le plus longtemps possible.
# Bien sur on ne peut pas choisir le premier siege parmi les 2 premiers
# sieges libres consecutifs car :
#  - EEE -> OEE -> OOE et le siege choisi ne sera donc immediatement
#    plus bon car les autres passagers suivent la meme strategie...
#  - EEO -> OEO ->* OOO apres le meme delai que si on avait choisi la
#    2eme place, mais cela contredit la regle qui impose en cas d'egalite
#    de choisir la place la plus a droite...

def main():
    S = sys.stdin.readline().strip()
    if S[-1]=='E':
        print len(S)-1
    elif S[0]=='E':
        print 0
    else:
        for i in xrange(1,len(S)-2):
            if S[i:i+2]=='EE':
                print i+1
                return
        for i in xrange(len(E)-2,-1,-1):
            print i
            break

main()
