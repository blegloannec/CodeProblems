#!/usr/bin/env pypy

# O(n^2) suffix trees are good enough here, ~1s with pypy

# suffix tree code from pb SUFF
# insere le suffixe S[i:] dans le sous-arbre de ST enracine en u
def add(S,ST,i,u=0):
    iv = 0
    while iv<len(ST[u]) and S[ST[u][iv][1]]!=S[i]:
        iv += 1
    if iv==len(ST[u]):
        # il n'y a pas d'arete a suivre en u
        # on connecte donc une nouvelle feuille pour S[:i] ici
        v = len(ST)
        ST[u].append((v,i,len(S)-i))
        ST[v] = []
    else:
        v,k0,l = ST[u][iv]
        k = k0
        l += k
        j = i
        while j<len(S) and k<l and S[j]==S[k]:
            j += 1
            k += 1
        if k==l:
            # on est alle au bout de l'arete
            add(S,ST,j,v)
        else:
            # on cree un sommet intermediaire et on bifurque
            nv = len(ST)
            ST[nv] = [(v,k,l-k)]
            ST[u][iv] = (nv,k0,k-k0)
            w = len(ST)
            ST[nv].append((w,j,len(S)-j))
            ST[w] = []

def main():
    S = raw_input()+'$'
    # building suffix tree in O(n^2)
    ST = {0:[(1,0,len(S))],1:[]}
    for i in xrange(1,len(S)):
        add(S,ST,i)
    # computing m(), m(a,k,n) = min(a^k,n-k+1)
    # a^k is increasing with k and can become very large
    # n-k+1 is decreasing with k and rapidly falls below a^k
    # we do it naively in O(n), yet solving a^k = n-k+1 in k would lead
    # to an explicit formula as m = sum(a^k, 0<k<k0) + sum(n-k+1, k>=k0)
    n,m = len(S)-1,0
    p4,p4test = 1,True
    for i in xrange(1,n+1):
        if p4test:
            p4 *= 4
            if p4<n-i+1:
                m += p4
            else:
                m += n-i+1
                # we stop computing powers of 4 from now on
                p4test = False
        else:
            m += n-i+1
    # computing sub() = nb of prefixes in the tree (not taking the final $
    #                   into account)
    cpt = 0
    for u in ST:
        for (_,i,l) in ST[u]:
            cpt += l if i+l<len(S) else l-1
    # lc()
    print float(cpt)/m

main()
