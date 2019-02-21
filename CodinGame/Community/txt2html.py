#!/usr/bin/env python3

N = int(input())
G = [input().strip() for i in range(N)]
Col = [i for i in range(len(G[0])) if G[0][i]=='+']
Row = [i for i in range(N) if G[i][0]=='+']
O = ['<table>']
for i in range(len(Row)-1):
    L = ['<tr>']
    for j in range(len(Col)-1):
        content = [G[x][Col[j]+1:Col[j+1]].strip() for x in range(Row[i]+1,Row[i+1])]
        L.append('<td>%s</td>' % ' '.join(c for c in content if c))
    L.append('</tr>')
    O.append(''.join(L))
O.append('</table>')
print('\n'.join(O))
