#!/usr/bin/env python

import rosalib

# in general, this is an NP-complete problem
# but here: "there exists a unique way to reconstruct the entire
# chromosome from these reads by gluing together pairs of reads
# that overlap by more than half their length."

def edge(A,B):
    for k in range(len(A),len(A)//2,-1):
        if A[-k:]==B[:k]:
            return k
    return None

def main():
    DNAS = [DNA for _,DNA in rosalib.parse_fasta()]
    Succ = [None]*len(DNAS)
    Start = set(range(len(DNAS)))
    for i in range(len(DNAS)):
        for j in range(len(DNAS)):
            if i==j:
                continue
            e = edge(DNAS[i],DNAS[j])
            if e!=None:
                assert(Succ[i]==None)
                Succ[i] = (j,e)
                assert(j in Start)
                Start.remove(j)
    assert(len(Start)==1)
    s = Start.pop()
    res = [DNAS[s]]
    while Succ[s]!=None:
        t,e = Succ[s]
        res.append(DNAS[t][e:])
        s = t
    print(''.join(res))

main()
