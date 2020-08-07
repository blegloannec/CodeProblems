#!/usr/bin/env python3

class Villager:
    def __init__(self, desc):
        desc = desc.strip('.').split()
        self.name = desc[0].strip(':')
        self.loc = desc[5].strip(',')
        self.Names = set(desc[7::2])
        self.Names.add(self.name)
    
    def __and__(self, W):
        return (self.Names==W.Names if self.loc==W.loc else \
                self.name not in W.Names and W.name not in self.Names)

def main():
    N = int(input())
    V = [Villager(input()) for _ in range(N)]
    murderer = None
    for i in range(N):
        contr = sum(1 for j in range(N) if not V[i]&V[j])
        if contr>1:
            murderer = i
            break
        elif contr==1 and len(V[i].Names)>1:
            murderer = i
    print('It was me!' if murderer is None else f'{V[murderer].name} did it!')

main()
