#!/usr/bin/env python3

# les serpents forment un langage rationnel
# blancs autorises seulement au debut et a la fin
# entre 2 #  ou 2 . il faut un nb pair de #
#         .       #                       #
# alors qu'entre # et . il en faut un nb impair
#                .    #
# etc
# probablement faisable de facon tres concise avec des regex

# a suivre une implementation tres mediocre...

def is_snake(S):
    p = None
    e = False
    s = False
    i = 0
    while i<len(S[0]):
        if (S[0][i],S[1][i])==('.','.'):
            if p!=None or s:
                e = True
        elif e:
            return False
        elif (S[0][i],S[1][i])==('#','.'):
            if p==None:
                p = 0
            elif p==1:
                return False
        elif (S[0][i],S[1][i])==('.','#'):
            if p==None:
                p = 1
            elif p==0:
                return False
        else:
            s = True
            if p!=None:
                p = 1-p
        i += 1
    return p!=None or s

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        S = [input() for _ in range(2)]
        print('yes' if is_snake(S) else 'no')

main()
