#!/usr/bin/env pypy

# O(N B + Q B log N) trie-based solution, B = max bit size (16 here)
# (modified & optimized from HackerRank/maximum_xor.py)
# NB: The editorial suggests a slightly more efficient, though more complicated
#     Persistent Segment Tree (for the sum, on the range [0,2^B]) based solution

import bisect

MaxDepth = 16

class IdxTrie:
    def __init__(self, X):
        self.Children = [[None, None]]
        self.Idx = [[]]
        for idx,x in enumerate(X):
            self.insert(idx, x)

    def new_node(self):
        node = len(self.Children)
        self.Children.append([None, None])
        self.Idx.append([])
        return node

    def insert(self, idx, x):
        node = 0
        self.Idx[node].append(idx)
        depth = MaxDepth
        while depth>=0:
            b = (x>>depth)&1
            if self.Children[node][b] is None:
                self.Children[node][b] = self.new_node()
            node = self.Children[node][b]
            self.Idx[node].append(idx)
            depth -= 1

    def max_xor(self, idx_l, idx_r, x):
        res = 0
        node = 0
        depth = MaxDepth
        while depth>=0:
            b = ((x>>depth)&1)^1
            if self.Children[node][b] is None or \
               not self.contains_idx(self.Children[node][b], idx_l, idx_r):
                b ^= 1
            res |= b<<depth
            node = self.Children[node][b]
            depth -= 1
        return res

    def contains_idx(self, node, idx_l, idx_r):
        i = bisect.bisect_left(self.Idx[node], idx_l)
        return i<len(self.Idx[node]) and self.Idx[node][i]<=idx_r


if __name__=='__main__':
    T = int(raw_input())
    for _ in xrange(T):
        N,Q = map(int,raw_input().split())
        X = list(map(int,raw_input().split()))
        Trie = IdxTrie(X)
        for _ in xrange(Q):
            a,l,r = map(int,raw_input().split())
            y = Trie.max_xor(l-1, r-1, a)
            print a^y
