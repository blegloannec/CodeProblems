#!/usr/bin/env python3

class DFA:
    def __init__(self):
        alpha = input().split()
        states = input().split()
        nb_trans = int(input())
        self.Trans = {}
        for _ in range(nb_trans):
            q,a,r = input().split()
            assert (q,a) not in self.Trans
            self.Trans[q,a] = r
        self.q0 = input()
        self.Qf = set(input().split())
        
    def accept(self, word):
        q = self.q0
        for c in word:
            if (q,c) not in self.Trans:
                return False
            q = self.Trans[q,c]
        return q in self.Qf

def main():
    A = DFA()
    nb_words = int(input())
    for _ in range(nb_words):
        word = input()
        print('true' if A.accept(word) else 'false')

main()
