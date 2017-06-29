#!/usr/bin/env python3

# essentiellement Rabin-Karp en 2D, O(RC)
# NB : on ne s'embete pas a verifier les faux-positifs ici
# NB : on pourrait pre-calculer les B^k mod P pour tout k<=r*c
#      afin d'aller un peu plus vite, l'implementation suivante
#      est en O(RC log(RC)) car on ne l'a pas fait

M = 10**9+7  # modulo du hash
B = 10       # base du hash

def find():
    # hashs de toutes les fenetres de largeur c
    H = [[] for _ in range(R)]
    for i in range(R):
        h = 0
        for j in range(C):
            h = (B*h + G[i][j] - (G[i][j-c] if j>=c else 0)*pow(B,c,M)) % M
            if j>=c-1:
                H[i].append(h)
    # hash du motif recherche
    PH = 0
    for i in range(r):
        for j in range(c):
            PH = (B*PH + P[i][j])%M
    # hashs de tous les motifs r*c
    for j in range(C-c+1):
        h = 0
        for i in range(R):
            h = (pow(B,c,M)*h + H[i][j] - (H[i-r][j] if i>=r else 0)*pow(B,c*r,M)) % M
            if i>=r-1 and h==PH:
                return True
    return False

def num(c):
    return ord(c)-ord('0')

def main():
    global R,C,G,r,c,P
    T = int(input())
    for _ in range(T):
        R,C = map(int,input().split())
        G = [list(map(num,input())) for _ in range(R)]
        r,c = map(int,input().split())
        P = [list(map(num,input())) for _ in range(r)]
        print('YES' if find() else 'NO')

main()
