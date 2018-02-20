#!/usr/bin/env python3

# en formant un triangle isocele de cote b,
# on peut couvrir une distance 2*b a la base

def giant(a,b,d):
    c,r = divmod(d,b)
    if r>0:
        if r==a or c>0:
            # soit on utilise a pour couvrir la distance restante
            # soit on couvre la distance b+r < 2b avec un triangle
            c += 1
        else:
            # on couvre la distance r < b avec un triangle
            c += 2
    return c

def main():
    q = int(input())
    for _ in range(q):
        a,b,d = map(int,input().split())
        print(giant(a,b,d))

main()
