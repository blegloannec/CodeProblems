#!/usr/bin/env python3

import re

num = lambda c: ord(c)-ord('a')

class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.final = False

    def insert(self, w, i=0):
        if i<len(w):
            a = num(w[i])
            if self.children[a] is None:
                self.children[a] = TrieNode()
            self.children[a].insert(w, i+1)
        else:
            self.final = True

def main():
    text = re.sub(r'[^a-z]', '', input().lower())
    N = int(input())
    root = TrieNode()
    for _ in range(N):
        root.insert(re.sub(r'[^a-z]', '', input().lower()))
    sol = []
    for i in range(len(text)):
        a = num(text[i])
        if root.children[a] is not None:
            first = root.children[a]
            for j in range(i+1, len(text)):
                node = first
                for k in range(j, len(text), j-i):
                    b = num(text[k])
                    if node.children[b] is not None:
                        node = node.children[b]
                        if node.final:
                            sol.append((i,j,k))
                    else:
                        break
    i,j,k = max(sol, key=(lambda ijk: (ijk[2]-ijk[0])//(ijk[1]-ijk[0])))
    res = ''.join(c.upper() if l%(j-i)==0 else c for l,c in enumerate(text[i:k+1]))
    print(res)

main()
