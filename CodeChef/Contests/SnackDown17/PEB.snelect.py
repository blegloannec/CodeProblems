#!/usr/bin/env python3

def snake_eaten(S):
    cpt = 0   # nb of snakes eaten
    s = None  # index of last snake eaten
    for i in range(len(S)):
        if S[i]=='m':
            if i>0 and S[i-1]=='s' and s!=i-1:
                s = i-1
                cpt += 1
            elif i+1<len(S) and S[i+1]=='s':
                s = i+1
                cpt += 1
    return cpt

def main():
    T = int(input())
    for _ in range(T):
        S = input()
        m = S.count('m')
        s = len(S) - m - snake_eaten(S)
        if m<s:
            print('snakes')
        elif m>s:
            print('mongooses')
        else:
            print('tie')

main()
