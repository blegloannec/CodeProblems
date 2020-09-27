#!/usr/bin/env python3

class CodeTrie:
    def __init__(self):
        self.Nodes = [[None, None]]
        self.Chars = [None]
    
    def _new_node(self):
        node = len(self.Nodes)
        self.Nodes.append([None, None])
        self.Chars.append(None)
        return node
    
    def insert(self, code, char):
        node = 0
        for c in code:
            assert self.Chars[node] is None
            if self.Nodes[node][c] is None:
                self.Nodes[node][c] = self._new_node()
            node = self.Nodes[node][c]
        self.Chars[node] = char
    
    def decode(self, data):
        Out = []
        node = i0 = 0
        for i,c in enumerate(data):
            if self.Nodes[node][c] is None:
                return f'DECODE FAIL AT INDEX {i0}'
            node = self.Nodes[node][c]
            if self.Chars[node] is not None:
                Out.append(self.Chars[node])
                node = 0
                i0 = i+1
        if node > 0:
            return f'DECODE FAIL AT INDEX {i0}'
        return ''.join(Out)

def main():
    N = int(input())
    T = CodeTrie()
    for _ in range(N):
        code, char = input().split()
        code = tuple(map(int, code))
        char = chr(int(char))
        T.insert(code, char)
    S = tuple(map(int, input()))
    print(T.decode(S))

main()
