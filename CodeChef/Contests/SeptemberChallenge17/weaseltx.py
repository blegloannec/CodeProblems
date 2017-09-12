#!/usr/bin/env python3

# Plusieurs observations :
#  - Il s'agit d'un probleme de somme iteree de "suffixes" sur un arbre.
#    On peut voir la valeur de x a chaque instant comme une combinaison
#    lineaire des valeurs des noeuds du sous-arbre de x, les coefficients
#    variant avec le temps, et comme il s'agit d'un xor, seule leur parite
#    importe.
#  - La valeur d'un sommet x ne contribue qu'aux valeurs de sa chaine
#    d'ancetres jusqu'a la racine et le coefficient de cette contribution
#    ne depend clairement que de la profondeur de x. Comme seule la valeur
#    a la racine nous interesse et que tous les noeuds de meme profondeur
#    ont les memes coeff. de contribution (variant avec le temps) dans la
#    somme a la racine, alors on peut ramener l'arbre a une simple chaine
#    dans laquelle l'unique noeud de profondeur d a pour valeur le xor de
#    toutes les valeurs des noeuds de profondeur d de l'arbre. On a alors
#    un probleme de somme iteree de suffixes dans un tableau classique.
#  - La contribution du sommet de profondeur d a l'instant t dans la
#    somme de la racine est binom(t-1+d,d) (il y a plusieurs manieres de
#    le voir, on ne detaille pas). Seule sa parite nous interesse, par
#    thm de Lucas, binom(t-1+d,d) = 1 mod 2 ssi chaque chiffre de
#    l'ecriture binaire de d est inferieur au chiffre correspondant
#    dans l'ecriture binaire de t-1+d (autrement dit, si le bit i de t-1+d
#    vaut 0, alors celui de d doit aussi valoir 0) et qui se simplifie
#    aisement en la condition (t-1) & d = 0 (pas de retenue dans l'addition
#    (t-1) + d qui creerait un 0 a la position d'un 1 de d).
# Au bilan, a l'instant t, la valeur a la racine est le xor des valeurs des
# noeuds des profondeurs d tq d&(t-1)=0. En particulier, elle ne depend
# que de l'ecriture binaire des d <= dmax la profondeur max donc elle est
# periodique de periode 2^k pour le plus petit k tel que 2^k > dmax
# (de meme que les valeurs a la profondeur d sont periodiques de periode 2^l
#  pour le plus petit l tel que 2^l > dmax - d).
# Chaque valeur a la racine est calculable en O(dmax) et il y a 2^k avec k<=18
# valeurs distinctes a calculer (k<=18 car dmax <= n <= 2*10^5) donc tout
# ca ne suffit pas...

# La technique finale qui me manquait pendant le contest, issue de l'edito,
# https://discuss.codechef.com/questions/108188/weaseltx-editorial
# consiste a faire une prog. dyn. en O(k2^k) = O(n log n) :
# si la periode est 2^kmax, pour Xi les valeurs du tableau initial (issues du
# xor des niveaux de l'arbre) completees par des 0 jusqu'a 2^kmax-1,
# on pose, pour tous 0 <= k <= kmax et 0 <= t < 2^kmax,
# C(k,t) = XOR des Xj tels que j coincide avec t sur ses bits >=i
#          et le ET logique de t et j sur les bits <i vaut 0
# La valeur a la racine a l'instant t est est C(kmax,t-1).
# On a C(0,t) = Xt
# et C(k+1,t) = C(k,t XOR 2^k) si le k-ieme bit de t est 1
#               et C(k,t) XOR C(k,t XOR 2^k) sinon

# NB : Autre interpretation
# Si l'on represente ligne apres lignes les XOR suffixes iteres de X
# i.e. le tableau T(t,d) = XOR( T(t-1,k), d<=k<=dmax )
#      avec T(0,.) = le tableau initial
# alors on a T(t,d) = T(t-1,d) XOR T(t,d+1)
# ou encore T(t-1,d) = T(t,d) XOR T(t,d+1)
# Autrement dit, si l'on inverse le temps, on a, sur chaque bit du resultat,
# un diagramme de l'automate cellulaire one-way du XOR.

def depth_dfs(u0=0):
    S = [u0]
    D = [-1]*N
    D[u0] = 0
    while S:
        u = S.pop()
        for v in G[u]:
            if D[v]<0:
                D[v] = D[u]+1
                S.append(v)
    return D

def one_value(X,t):
    res = 0
    for i in range(len(X)):
        if i&(t-1)==0:  # <=> binom(t+i-1,i) = 1 mod 2
            res ^= X[i]

def dp_all_values(X,kmax):
    C = [X[:] for _ in range(kmax+1)]
    for k in range(1,kmax+1):
        for i in range(len(X)):
            C[k][i] = C[k-1][i^(1<<(k-1))]
            if (i>>(k-1))&1==0:
                C[k][i] ^= C[k-1][i]
    return C
            
def main():
    global N,G
    N,Q = map(int,input().split())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        u,v = map(int,input().split())
        G[u].append(v)
        G[v].append(u)
    X0 = list(map(int,input().split()))
    # on ramene le graphe a une chaine
    D = depth_dfs()
    MD = max(D)
    X = [0]*(MD+1)
    for u in range(N):
        X[D[u]] ^= X0[u]
    # periode
    k = 1
    while (1<<k)<=MD:
        k += 1
    period = 1<<k
    while len(X)<period:
        X.append(0)
    C = dp_all_values(X,k)
    for i in range(Q):
        t = (int(input())-1) % period
        print(C[k][t])

main()
