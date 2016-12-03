#!/usr/bin/env python

import sys

# le prog input calcule dans b le nb d'etapes pour arriver a 1
# de la suite de syracuse depuis 4971 pour a=0 (solution 170)
# et 113383 pour a=1 (solution 247)

prog = []
#reg = {'a':0,'b':0}
reg = {'a':1,'b':0}

# version rec terminale qui fait quand meme peter la pile !
# python ne gere pas la recursion terminale
def simulate(i):
    if i<0 or i>=len(prog):
        return
    o = prog[i]
    if o[0]=='hlf':
        reg[o[1]] /= 2
        simulate(i+1)
    elif o[0]=='tpl':
        reg[o[1]] *= 3
        simulate(i+1)
    elif o[0]=='inc':
        reg[o[1]] += 1
        simulate(i+1)
    elif o[0]=='jmp':
        simulate(i+int(o[1]))
    elif o[0]=='jie':
        if reg[o[1][:-1]]%2==0:
            simulate(i+int(o[2]))
        else:
            simulate(i+1)
    elif o[0]=='jio':
        if reg[o[1][:-1]]==1:
            simulate(i+int(o[2]))
        else:
            simulate(i+1)

# version iterative
def simulate2():
    i = 0
    while 0<=i and i<len(prog):
        o = prog[i]
        if o[0]=='hlf':
            reg[o[1]] /= 2
            i += 1
        elif o[0]=='tpl':
            reg[o[1]] *= 3
            i += 1
        elif o[0]=='inc':
            reg[o[1]] += 1
            i += 1
        elif o[0]=='jmp':
            i += int(o[1])
        elif o[0]=='jie':
            if reg[o[1][:-1]]%2==0:
                i += int(o[2])
            else:
                i += 1
        elif o[0]=='jio':
            if reg[o[1][:-1]]==1:
                i += int(o[2])
            else:
                i += 1

def main():
    global prog
    f = open(sys.argv[1],'r')
    prog = f.readlines()
    f.close()
    prog = map((lambda x: x.strip().split()),prog)
    simulate2()
    print reg

main()
