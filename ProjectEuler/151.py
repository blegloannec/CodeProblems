#!/usr/bin/env python

# there is a potential of exactly 2^4 = 16 A5 sheets
# in a A1 sheet

# on utilise une chaine de markov donc les etats
# sont les contenus possibles pour l'enveloppe
# NB: ce n'est pas necessairement l'approche la plus naturelle
# ou pertinente dans la mesure ou le potentiel de feuilles A5
# dans l'enveloppe decroit exactement d'1 a chaque tirage
# et qu'on ne s'interesse donc qu'a un court regime transitoire,
# une prog dyn etait sans doute plus naturelle...

# successeur d'une conf si l'on prend une feuille pick dedans
def next_conf(conf,pick):
    new = list(conf)
    new[pick] -= 1
    for a in xrange(pick+1,5):
        new[a] += 1
    return tuple(new)

init_conf = (1,0,0,0,0)
confs_solo = [(1,0,0,0,0),(0,1,0,0,0),(0,0,1,0,0),(0,0,0,1,0),(0,0,0,0,1)]
conf_cpt = 0
conf2num = {}

# generer et numeroter les etats possibles (87)
def gen_confs(conf):
    global conf_cpt
    if conf in conf2num:
        return
    conf2num[conf] = conf_cpt
    conf_cpt += 1
    for a in xrange(5):
        if conf[a]>0:
            gen_confs(next_conf(conf,a))

# construire la matrice de la chaine de markov
def gen_markov():
    N = len(conf2num)
    M = [[0 for _ in xrange(N)] for _ in xrange(N)]
    for conf in conf2num:
        s = sum(conf)
        if s==0: # conf vide
            M[conf2num[conf]][conf2num[conf]] = 1.
            continue
        for a in xrange(5):
            if conf[a]>0:
                new = next_conf(conf,a)
                # proba d'arriver dans new depuis conf
                M[conf2num[new]][conf2num[conf]] = float(conf[a])/s
    return M

# produit matrice vecteur
def prod(M,V):
    W = [0. for _ in xrange(len(V))]
    for a in xrange(len(W)):
        for k in xrange(len(W)):
            W[a] += M[a][k]*V[k]
    return W

def main():
    gen_confs(init_conf)
    M = gen_markov()
    V = [0. for _ in xrange(len(M))]
    V[conf2num[init_conf]] = 1.
    s = 0.
    for _ in xrange(14):
        V = prod(M,V)
        s += sum(V[conf2num[conf]] for conf in confs_solo)
    print s

main()
