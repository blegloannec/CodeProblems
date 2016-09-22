#!/usr/bin/env python

from decimal import Decimal

N = 15
# un pliage d'une chaine de longueur 15 a entre 14 et 22 points
# de contact
# empiriquement (en tirant des chaines au hasard), il apparait inutile
# de chercher parmi les arrangements ayant strictement moins de 20
# points de contact
thresh = 20

# runs in 40s with pypy

# on genere les arrangements
def backtrack_shapes(n,i,(x0,y0),Pos,Contact,result,elim=True):
    if i==n:
        if len(Contact)>=thresh:
            result.append(Contact[:])
    else:
        for (x,y) in [(x0-1,y0),(x0+1,y0),(x0,y0-1),(x0,y0+1)]:
            if elim and y<y0: # pour eliminer la symetrie verticale
                continue
            if (x,y) not in Pos:
                Pos[x,y] = i
                cont_cpt = 0
                for (x1,y1) in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                    if (x1,y1) in Pos:
                        Contact.append((Pos[x1,y1],Pos[x,y]))
                        cont_cpt += 1
                backtrack_shapes(n,i+1,(x,y),Pos,Contact,result,elim and (y==y0))
                del Pos[x,y]
                while cont_cpt>0:
                    Contact.pop()
                    cont_cpt -= 1

def shapes(n):
    res = []
    Pos = {(0,0):0,(1,0):1}
    Contact = [(0,1)]
    backtrack_shapes(n,2,(1,0),Pos,Contact,res)
    return res

# on compte les contacts H-H pour la chaine n
def count(n,contacts):
    res = 0
    for (i,j) in contacts:
        res += (n>>i)&(n>>j)&1
    return res

def main():
    contacts_list = shapes(N)
    res = 0
    #print len(contacts_list)
    for n in xrange(1<<N):
        m = 0
        for c in contacts_list:
            m = max(m,count(n,c))
        res += m
    print Decimal(res)/Decimal(1<<N)

main()
