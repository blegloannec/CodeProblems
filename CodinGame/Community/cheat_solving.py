#!/usr/bin/env python3

#            11111
#  012345678901234
# 0    ABC
# 1    D E
# 2    FGH
# 3
# 4ADF FGH HEC CBA
# 5I J J K K L L I
# 6MNO OPQ QRS STM
# 7
# 8    OPQ
# 9    N R
#10    MTS

EdgePos = [((0,5),(4,13)), ((1,4),(4,1)), ((1,6),(4,9)), ((2,5),(4,5)),
         ((5,0),(5,14)), ((5,2),(5,4)), ((5,6),(5,8)), ((5,10),(5,12)),
         ((6,1),(9,4)), ((6,5),(8,5)), ((6,9),(9,6)), ((6,13),(10,5))]
CornPos = [((0,4),(4,14),(4,0)), ((0,6),(4,10),(4,12)), ((2,4),(4,2),(4,4)),
           ((2,6),(4,6),(4,8)), ((6,0),(6,14),(10,4)), ((6,4),(6,2),(8,4)),
           ((6,6),(8,6),(6,8)), ((6,10),(10,6),(6,12))]
EdgeRef = {'RU', 'BR', 'LU', 'DL', 'DR', 'FL', 'DF', 'FR', 'BU', 'BD', 'FU', 'BL'}
CornRef = {'BLU', 'FUL', 'BRD', 'FRU', 'BDL', 'DRF', 'BUR', 'DFL'}

I = [input() for _ in range(11)]
Edge = set()
for (i1,j1),(i2,j2) in EdgePos:
    E = ''.join(sorted((I[i1][j1],I[i2][j2])))
    Edge.add(E)
Corn = set()
for (i1,j1),(i2,j2),(i3,j3) in CornPos:
    C = I[i1][j1]+I[i2][j2]+I[i3][j3]
    i = C.index(min(C))
    C = C[i:]+C[:i]
    Corn.add(C)
print(('UNSOLVABLE','SOLVABLE')[Edge==EdgeRef and Corn==CornRef])
