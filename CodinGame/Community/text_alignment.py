#!/usr/bin/env python3

align = input()
N = int(input())
Text = [input() for _ in range(N)]

W = max(len(L) for L in Text)
if align=='RIGHT':
    Text = [' '*(W-len(L))+L for L in Text]
elif align=='CENTER':
    Text = [' '*((W-len(L))//2)+L for L in Text]
elif align=='JUSTIFY':
    for i in range(N):
        L = Text[i].split()
        cnt = len(L)-1
        spc = W-sum(len(w) for w in L)
        s = 0
        NL = [L[0]]
        for j in range(1,len(L)):
            s,s0 = (j*spc)//cnt,s
            NL.append(' '*(s-s0))
            NL.append(L[j])
        Text[i] = ''.join(NL)
print('\n'.join(Text))
