#!/usr/bin/env python3

def fences(S):
    sa,sb = False,False
    cpt = 0
    a,b = False,False
    for i in range(len(S[0])):
        if (S[0][i],S[1][i])==('*','*'):
            if a or b:
                cpt += 1
            a = b = True
        elif (S[0][i],S[1][i])==('*','.'):
            if a:
                cpt += 1
                b = False
            a = True
        elif (S[0][i],S[1][i])==('.','*'):
            if b:
                cpt += 1
                a = False
            b = True
        sa = sa or a
        sb = sb or b
    return cpt+int(sa and sb)

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        S = [input() for _ in range(2)]
        print(fences(S))

main()
