#!/usr/bin/env python3

def main():
    E = input()
    P = []
    S = []
    for i,c in enumerate(E):
        if c=='(':
            S.append(i)
        elif c==')':
            l = S.pop()
            P.append((l,i))
    Out = set()
    for p in range(1, 1<<len(P)):
        Mask = [True]*len(E)
        for b in range(len(P)):
            if (p>>b)&1:
                Mask[P[b][0]] = Mask[P[b][1]] = False
        Out.add(''.join(c for c,m in zip(E,Mask) if m))
    print('\n'.join(sorted(Out)))

main()
