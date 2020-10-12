#!/usr/bin/env python3

# trie-based approach

class TrieNode:
    def __init__(self):
        self.Child = {}
        self.count = 0
    
    def insert(self, word, i=0):
        self.count += 1
        if i<len(word):
            c = word[i]
            if c not in self.Child:
                self.Child[c] = TrieNode()
            self.Child[c].insert(word, i+1)
    
    def get_prefix(self, word, i=0):
        if i<len(word) and self.count>1:
            return self.Child[word[i]].get_prefix(word, i+1)
        return word[:i]

def main():
    N = int(input())
    W = [input() for _ in range(N)]
    Trie = TrieNode()
    for w in set(W):
        Trie.insert(w)
    for w in W:
        print(Trie.get_prefix(w))

main()
