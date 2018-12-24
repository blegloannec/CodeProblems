#!/usr/bin/env python3

import sys, re

form = re.compile('(\d+) units each with (\d+) hit points (.*)with an attack that does (\d+) ([a-z]+) damage at initiative (\d+)')

class Group:
    def __init__(self, S, team):
        self.team = team
        self.units, self.hp, extra, self.attack, self.attack_type, self.initiative = form.match(S).groups()
        self.units = int(self.units)
        self.hp = int(self.hp)
        self.attack = int(self.attack)
        self.initiative = int(self.initiative)
        self.immune = set()
        self.weak = set()
        extra = extra.strip()
        if extra:
            for B in extra[1:-1].split('; '):
                L = B.replace(',','').split()
                if L[0]=='immune':
                    self.immune = set(L[2:])
                else:
                    self.weak = set(L[2:])
        # backup for the reset
        self.units0 = self.units
        self.attack0 = self.attack
    
    def power(self):
        return self.units * self.attack
    
    def damage(self, B):
        if self.attack_type in B.immune:
            return 0
        return self.power() * (2 if self.attack_type in B.weak else 1)
    
    def take_damage(self, d):
        loss = min(self.units,d//self.hp)
        self.units -= loss
        return loss
    
    def reset(self, boost=0):
        self.units = self.units0
        self.attack = self.attack0 + boost


A = []  # global army for convenience
for L in sys.stdin.readlines():
    L = L.strip()
    if L=='Immune System:':
        team = 0
    elif L=='':
        continue
    elif L=='Infection:':
        team = 1
    else:
        A.append(Group(L,team))

A0 = A[:]  # backup for army reset/boost
def reset(boost=0):
    global A
    for G in A0:
        G.reset(boost if G.team==0 else 0)
    A = A0[:]


# Part 1
def turn():
    global A
    A.sort(key=(lambda G: (G.power(),G.initiative)), reverse=True)
    Target = [None]*len(A)
    Chosen = [False]*len(A)
    change = False
    for i in range(len(A)):
        # /!\ do not pick j such that A[i].damage(A[j])==0 as Target[i], this does not count as an
        #     actual attack and would wrongfully forbid any other group to pick j as a target
        T = [j for j in range(len(A)) if not Chosen[j] and A[j].team!=A[i].team and A[i].damage(A[j])>0]
        if T:
            j = max(T, key=(lambda j: (A[i].damage(A[j]),A[j].power(),A[j].initiative)))
            Target[i] = j
            Chosen[j] = True
    for i in sorted(range(len(A)), key=(lambda i: A[i].initiative), reverse=True):
        if A[i].units>0 and Target[i] is not None:
            j = Target[i]
            if A[j].take_damage(A[i].damage(A[j])):
                # introduced for part 2 to avoid infinite loops (remaining groups immune to each other
                # or too weak to deal at least hp damages)
                change = True
    A = [G for G in A if G.units>0]
    return change

def turns():
    while len(set(G.team for G in A))>1:
        turn()
    return sum(G.units for G in A)

print(turns())


# Part 2
def turns_boost():
    boost = 0
    win0 = False
    while not win0:
        boost += 1
        reset(boost)
        while turn():
            pass
        win0 = all(G.team==0 for G in A)
    #print(boost)
    return sum(G.units for G in A)

print(turns_boost())
