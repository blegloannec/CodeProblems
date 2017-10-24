#!/usr/bin/env python3

F = ["Danil","Olya","Slava","Ann","Nikita"]
S = input()
print('YES' if sum(S.count(f) for f in F)==1 else 'NO')
