#!/usr/bin/env python3

# NB: The mediants are always already irreducible as for any
#     pair of "consecutive" fractions pl/ql and pr/qr, the
#     relation pl*qr - pr*ql = -1 is always verified and preserved
#     (and ensures coprimality by Bezout's thm).

def dicho_path(p,q, pl=0,ql=1, pr=1,qr=0):
    Path = []
    pm, qm = pl+pr, ql+qr
    while (pm,qm)!=(p,q):
        if p*qm<pm*q:
            Path.append('L')
            pr,qr = pm,qm
        else:
            Path.append('R')
            pl,ql = pm,qm
        pm, qm = pl+pr, ql+qr
    return ''.join(Path)

def dicho_frac(Path):
    pl,ql, pr,qr = 0,1, 1,0
    p,q = pl+pr, ql+qr
    for d in Path:
        if d=='L':
            pr,qr = p,q
        else:
            pl,ql = p,q
        p,q = pl+pr, ql+qr
    return p,q

def main():
    N = int(input())
    for _ in range(N):
        I = input().split('/')
        if len(I)==2:
            print(dicho_path(int(I[0]),int(I[1])))
        else:
            print('%d/%d' % dicho_frac(I[0]))

main()
