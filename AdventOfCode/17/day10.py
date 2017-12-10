#!/usr/bin/env python3

S = 256      # list size
I = input()  # input

def invert(T,i,l):
    if l>1:
        j = i+l-1
        while i<j:
            T[i%S],T[j%S] = T[j%S],T[i%S]
            i += 1
            j -= 1

def knot_round(T,L,p=0,s=0):
    for l in L:
        invert(T,p,l)
        p = (p+l+s)%S
        s += 1
    return p,s

# Part 1
T = list(range(S))
L = list(map(int,I.split(',')))
knot_round(T,L)
print(T[0]*T[1])


# Part 2
def knot_hash(I):
    T = list(range(S))
    L = list(map(ord,I)) + [17,31,73,47,23]
    p = s = 0
    for _ in range(64):
        p,s = knot_round(T,L,p,s)
    H = [0]*16
    for i in range(16):
        for j in range(16):
            H[i] ^= T[16*i+j]
    return ''.join('%02x'%h for h in H)

print(knot_hash(I))
