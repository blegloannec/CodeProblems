#!/usr/bin/env python3

import sys

def main():
    Text = [sent.split() for sent in sys.stdin.readline().split('.')]
    # parsing sentences and indexing words
    N = 0
    Word2Idx = {}
    Words = []
    Q = []
    for Sent in Text:
        for i,word in enumerate(Sent):
            followed = word[-1]==','
            if followed:
                word = word[:-1]
            if word not in Word2Idx:
                Word2Idx[word] = N
                Words.append(word)
                N += 1
            idx = Word2Idx[word]
            Sent[i] = idx
            if followed:
                Q.append((0,idx))
    # building graphs
    # v in G[0][u]  <=>  word v follows  word u somewhere in the text
    # v in G[1][u]  <=>  word v precedes word u somewhere in the text
    # (we don't bother removing duplicated edges)
    G = [[[] for _ in range(N)] for _ in range(2)]
    for Sent in Text:
        for i in range(1, len(Sent)):
            G[0][Sent[i-1]].append(Sent[i])
            G[1][Sent[i]].append(Sent[i-1])
    # DFS to mark everyone
    Comma = [[False]*N for _ in range(2)]
    for g,u in Q:
        Comma[g][u] = True
    while Q:
        g,u = Q.pop()
        gv = g^1
        for v in G[g][u]:
            if not Comma[gv][v]:
                Comma[gv][v] = True
                Q.append((gv,v))
    # output
    out = '. '.join(' '.join(Words[w]+(',' if i+1<len(Sent) and Comma[0][w] else '') for i,w in enumerate(Sent)) for Sent in Text)
    sys.stdout.write(out)
    sys.stdout.write('\n')

main()
