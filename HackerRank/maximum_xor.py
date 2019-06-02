#!/usr/bin/env pypy3

MaxDepth = 30

class TrieNode:
    def __init__(self):
        self.Children = [None, None]

    def insert(self, x, depth=MaxDepth):
        if depth>=0:
            b = (x>>depth)&1
            if self.Children[b] is None:
                self.Children[b] = TrieNode()
            self.Children[b].insert(x, depth-1)

    def max_xor(self, x, depth=MaxDepth):
        res = 0
        if depth>=0:
            b = ((x>>depth)&1)^1
            if self.Children[b] is None:
                b ^= 1
            res = (b<<depth) | self.Children[b].max_xor(x, depth-1)
        return res


if __name__=='__main__':
    N = int(input())
    Trie = TrieNode()
    for a in input().split():
        Trie.insert(int(a))
    Q = int(input())
    for _ in range(Q):
        x = int(input())
        y = Trie.max_xor(x)
        print(x^y)
