#!/usr/bin/env python3

class Member:
    def __init__(self, name, parent, birth, death, religion, gender):
        self.name,self.parent,self.birth,self.death,self.religion,self.gender = name,parent,birth,death,religion,gender
        self.children = []
    
    def eligible(self):
        return self.death is None and self.religion!='Catholic'
    
    def __lt__(self, X):
        return self.gender>X.gender or (self.gender==X.gender and self.birth<X.birth)

def dfs(X, Order):
    if X.eligible():
        Order.append(X.name)
    for Y in X.children:
        dfs(Y,Order)

if __name__=='__main__':
    n = int(input())
    Family = {}
    for _ in range(n):
        name,parent,birth,death,religion,gender = input().split()
        birth = int(birth)
        death = None if death=='-' else int(death)
        Family[name] = Member(name,parent,birth,death,religion,gender)
        if parent=='-':
            Root = name
    for name in Family:
        if name!=Root:
            X = Family[name]
            X.parent = Family[X.parent]
            X.parent.children.append(X)
    for name in Family:
        Family[name].children.sort()
    O = []
    dfs(Family[Root],O)
    print('\n'.join(O))
