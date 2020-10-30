#!/usr/bin/env python3

# NB: see also PE 17

W0 = [None,'one','two','three','four','five','six','seven','eight','nine',
      'ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
W1 = [None,None,'twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
W3 = [None,'thousand','million','billion','trillion','quadrillion','quintillion']

def num2eng(num):
    minus = False
    if num[0]=='-':
        minus = True
        num = num[1:]
    if num=='0': return 'zero'
    num = list(map(int, reversed(num)))
    while len(num)%3!=0: num.append(0)
    Out = []
    for k in range(0,len(num),3):
        a,b,c = num[k:k+3]
        if a==b==c==0:    continue
        if k>0:           Out.append(W3[k//3])
        if b>1:           Out.append(W1[b] if a==0 else f'{W1[b]}-{W0[a]}')
        elif not a==b==0: Out.append(W0[a+10*b])
        if c!=0:          Out.append(f'{W0[c]} hundred')
    if minus:             Out.append('negative')
    return ' '.join(reversed(Out))

for _ in range(int(input())):
    print(num2eng(input()))
