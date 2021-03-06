#!/usr/bin/env python3

G = '''+---+---+---+---+---+---+---+---+
|...|:::|...|:::|...|:::|...|:::|
+---+---+---+---+---+---+---+---+
|:::|...|:::|...|:::|...|:::|...|
+---+---+---+---+---+---+---+---+
|...|:::|...|:::|...|:::|...|:::|
+---+---+---+---+---+---+---+---+
|:::|...|:::|...|:::|...|:::|...|
+---+---+---+---+---+---+---+---+
|...|:::|...|:::|...|:::|...|:::|
+---+---+---+---+---+---+---+---+
|:::|...|:::|...|:::|...|:::|...|
+---+---+---+---+---+---+---+---+
|...|:::|...|:::|...|:::|...|:::|
+---+---+---+---+---+---+---+---+
|:::|...|:::|...|:::|...|:::|...|
+---+---+---+---+---+---+---+---+'''
G = [list(L) for L in G.split('\n')]

def main():
    W = input()[len('White: '):].split(',')
    B = input()[len('Black: '):].split(',')
    P  = ['P'+w if len(w)==2 else w         for w in W if 2<=len(w)<=3]
    P += ['p'+w if len(w)==2 else w.lower() for w in B if 2<=len(w)<=3]
    for w in P:
        j =    ord(w[1])-ord('a')
        i = 7-(ord(w[2])-ord('1'))
        G[2*i+1][4*j+2] = w[0]
    for L in G:
        print(''.join(L))

main()
