#!/usr/bin/env python3

import sys, os, random
random.seed(987)

def solvable(Pairs):
    Pairs = [S.copy() for S in Pairs]  # copy
    M = len(Pairs)
    Q = [i for i in range(M) if len(Pairs[i])==1]
    Sol = [None]*M
    while Q:
        u = Q.pop()
        if Pairs[u]:
            assert len(Pairs[u])==1
            v = Pairs[u].pop()
            Sol[u], Sol[v] = v, u
            while Pairs[v]:
                w = Pairs[v].pop()
                if w!=u:
                    Pairs[w].remove(v)
                    if len(Pairs[w])==1:
                        Q.append(w)
    return (None not in Sol)

Cases = (2,3,4,5,10,25,50,100,150)

def gen_case(N, fname, write_sol=True):
    M = 2*N
    Even = list(range(2,M+1,2))
    random.shuffle(Even)
    if write_sol:
        F = open(fname+'_sol', 'w')
        F.write(' '.join(map(str,Even)))
        F.write('\n')
        F.close()
    # setting up graph
    Pairs = [set(range(1-i%2,M,2)) for i in range(M)]
    # steps
    Confs = []
    while not solvable(Pairs):
        Conf = [2*i+1 if random.randint(0,1)==1 else Even[i] for i in range(N)]
        random.shuffle(Conf)
        Confs.append(Conf)
        # updating graph
        C0 = [c-1 for c in Conf]
        E, O = [], []
        for c in C0:
            (E if c%2==0 else O).append(c)
        for e in E:
            for o in O:
                Pairs[e].discard(o)
                Pairs[o].discard(e)
    F = open(fname, 'w')
    F.write('%d %d\n' % (N,len(Confs)))
    F.write('\n'.join(' '.join(map(str,C)) for C in Confs))
    F.write('\n')
    F.close()

if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1] in ('clear','clean'):
        os.system('rm -f test* valid*')
    else:
        for i,N in enumerate(Cases):
            gen_case(N, 'test%d'%(i+1))
            gen_case(N, 'valid%d'%(i+1))
