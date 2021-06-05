#!/usr/bin/env python3

# markov chain learning bot

from collections import defaultdict

Name2000 = 'Automaton2000'

class Chain2000:
    __start__ = '__start__'
    __end__ = '__end__'
    __depth__ = 30
    
    def __init__(self):
        self.graph = {self.__start__: defaultdict(int)}

    def learn(self, sentence):
        sentence = [w for w in sentence if w!=Name2000]
        if sentence:
            s = self.__start__
            for w in sentence:
                self.graph[s][w] += 1
                if w not in self.graph:
                    self.graph[w] = defaultdict(int)
                s = w
            self.graph[s][self.__end__] += 1
    
    def speak(self):
        s = self.__start__
        S = []
        while s!=self.__end__ and len(S)<self.__depth__:
            s = min(self.graph[s].keys(), key=(lambda w: (-self.graph[s][w],w)))
            S.append(s)
        if S[-1]==self.__end__:
            S.pop()
        return ' '.join(S)


if __name__=='__main__':
    A2000 = Chain2000()
    n = int(input())
    for _ in range(n):
        line = input().split()
        # /!\ there are sometimes spaces between the login and ":" at the beginning of a chat line
        name, sentence = line[1], line[2+int(len(line)>2 and line[2]==':'):]
        A2000.learn(sentence)
        if any(Name2000 in w for w in sentence):
            print(A2000.speak())
