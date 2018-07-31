#!/usr/bin/env python3

INF = float('inf')

def reorder(s):
    if s[0]=='.':
        s = s[1:]
    t = []
    for c in s:
        if 'A'<=c<='Z':
            t.append(c.lower()+'1')
        else:
            t.append(c+'0')
    return ''.join(t)


class Node:
    def __init__(self, name, is_file=False):
        self.name = name
        self.is_file = is_file
        if not self.is_file:
            self.content = {}

    def list_content(self, flag_a=False, flag_d=False):
        return sorted((f for f in self.content if (flag_a or not (len(f)>1 and f[0]=='.')) and not (flag_d and self.content[f].is_file)), key=reorder)
    
    def pretty_print(self, flag_a=False, flag_d=False, flag_L=INF, pref=None):
        if flag_L<0:
            return 0,0
        d,f = 0,1
        if pref==None:
            pref = []
        else:
            spref = ''
            if pref:
                spref  = ''.join('|   ' if p else '    ' for p in pref[:-1]) + ('|-- ' if pref[-1] else '`-- ')
            print(spref + self.name)
        if not self.is_file:
            d,f = 1,0
            L = self.list_content(flag_a,flag_d)
            for i in range(len(L)):
                pref.append(i<len(L)-1)
                d0,f0 = self.content[L[i]].pretty_print(flag_a,flag_d,flag_L-1,pref)
                d += d0
                f += f0
                pref.pop()
        return d,f


class Tree:
    def __init__(self):
        self.root = Node('.')
    
    def insert(self, path):
        path = path.split('/')
        curr = self.root
        for i in range(int(path[0]=='.'),len(path)):
            if path[i] not in curr.content:
                curr.content[path[i]] = Node(path[i], (i==len(path)-1))
            curr = curr.content[path[i]]
    
    def reach(self, path):
        path = path.split('/')
        curr = self.root
        for i in range(int(path[0]=='.'),len(path)):
            if path[i] not in curr.content:
                return None
            curr = curr.content[path[i]]
        return curr


def main():
    S = input()
    F = set(input().split(','))
    N = int(input())
    flag_a = flag_d = False
    flag_L = float('inf')
    for flag in F:
        flag = flag.strip()
        if flag=='-a':
            flag_a = True
        elif flag=='-d':
            flag_d = True
        elif flag[:3]=='-L ':
            try:
                flag_L = int(flag.split()[1])
            except:
                pass
    T = Tree()
    for i in range(N):
        T.insert(input())
    node = T.reach(S)
    if node==None or node.is_file:
        print(S,'[error opening dir]')
        d = f = 0
    else:
        print(S)
        d,f = node.pretty_print(flag_a,flag_d,flag_L)
        d -= 1
    print()
    if not flag_d:
        print('%d director%s, %d file%s' % (d,'y' if d==1 else 'ies',f,'' if f==1 else 's'))
    else:
        print('%d director%s' % (d,'y' if d==1 else 'ies'))

main()
