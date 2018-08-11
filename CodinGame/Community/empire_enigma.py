#!/usr/bin/env python3

# approche sans utiliser l'offset...

MOD = 7140
A = 7562100%MOD
B = 907598307%MOD
MASK = (1<<8)-1

def seeded_attack(C,R0,M):
    R = R0
    for i in range(1,len(C)):
        R = (A*R+B)%MOD
        m = (R&MASK)^C[i]        
        if 32<=m<=126:
            M.append(m)
        else:
            return False
    return True

def attack(C):
    for R0 in range(C[0]^ord('@'),7140,256):
        M = []
        if seeded_attack(C,R0,M):
            return ''.join(chr(m) for m in M)

def main():
    _ = int(input())
    L = int(input())
    C = [int(input()) for _ in range(L)]
    print(attack(C))

main()
