#!/usr/bin/env python3

def majuscule(c):
    return 'A'<=c<='Z'

def c2i(c):
    return ord(c)-ord('A')

def i2c(i):
    return chr(i+ord('A'))


class Rotor:
    def __init__(self, permut, trigger):
        self.trigger = trigger
        self.pos = 0
        self.initpos = 0
        self.permut = permut
        self.calcul_inv()

    def fixe_initpos(self, p):
        self.initpos = p
        self.pos = p

    def reinit(self):
        self.pos = self.initpos

    def calcul_inv(self):
        self.permut_inv = [None]*26
        for i in range(26):
            self.permut_inv[self.permut[i]] = i

    def incr(self):
        self.pos = (self.pos+1)%26

    def chiffre(self, c):
        return (self.permut[(c+self.pos)%26]-self.pos+26)%26

    def chiffre_inv(self, c):
        return (self.permut_inv[(c+self.pos)%26]-self.pos+26)%26


class Reflecteur:
    def __init__(self, permut):
        self.permut = permut

    def chiffre(self, c):
        return self.permut[c]


class Brouilleur:
    def __init__(self):
        self.permut = list(range(26))

    def chiffre(self, c):
        return self.permut[c]

    def ajoute_fiche(self, a, b):
        for c in (a,b):
            assert self.permut[c]!=c
        self.permut[a] = b
        self.permut[b] = a

    def retire_fiche(self, a):
        b = self.permut[a]
        assert a!=b
        self.permut[a] = a
        self.permut[b] = b


class Enigma:
    def __init__(self, s0, t0, s1, t1, s2, t2, r):
        self.rotors = [Rotor(s0,t0),Rotor(s1,t1),Rotor(s2,t2)]
        self.reflecteur = Reflecteur(r)
        self.brouilleur = Brouilleur()

    def chiffre(self, c):
        self.rotors[0].incr()
        d = i2c(self.brouilleur.chiffre(    \
                self.rotors[0].chiffre_inv( \
                self.rotors[1].chiffre_inv( \
                self.rotors[2].chiffre_inv( \
                self.reflecteur.chiffre(    \
                self.rotors[2].chiffre(     \
                self.rotors[1].chiffre(     \
                self.rotors[0].chiffre(     \
                self.brouilleur.chiffre(c2i(c)))))))))))
        if self.rotors[1].pos==self.rotors[1].trigger:
            self.rotors[1].incr()
            self.rotors[2].incr()
        if self.rotors[0].pos==self.rotors[0].trigger:
            self.rotors[1].incr()
        return d

    def chiffre_mess(self, m):
        l = []
        for  c in m:
            if majuscule(c):
                l.append(self.chiffre(c))
            else:
                l.append(c)
        return ''.join(l)

    def clef(self, K):
        for i in range(3):
            self.rotors[i].fixe_initpos(c2i(K[i]))

    def reinit(self):
        for i in range(3):
            self.rotors[i].reinit()

    def ajoute_fiche(self, a, b):
        self.brouilleur.ajoute_fiche(a,b)

    def retire_fiche(self, a):
        self.brouilleur.retire_fiche(a)


def parse_permut(S):
    P = [None]*26
    for X in S.split():
        a,b = map(c2i,X.split('-'))
        P[a] = b
    return P

def main():
    r0 = parse_permut(input())
    t0 = c2i(input())
    r1 = parse_permut(input())
    t1 = c2i(input())
    r2 = parse_permut(input())
    t2 = c2i(input())
    r = parse_permut(input())
    clef = input().split()
    mess = input()
    E = Enigma(r0,t0,r1,t1,r2,t2,r)
    E.clef(clef)
    print(E.chiffre_mess(mess))

main()
