import sys

# Parsing input & Part 1
Pbs = []
part1 = 0
for L in sys.stdin.readlines():
    L = L.split()
    digs, code = L[:10], L[-4:]
    Pbs.append((digs, code))
    for x in code:
        if len(x) in (2,3,4,7):
            part1 += 1
print(part1)


# Part 2
def solve_pb(digs, code):
    Cnt = [[] for _ in range(8)]
    for s in digs:
        Cnt[len(s)].append(set(s))

    Sol = [None]*10
    Seg = [None]*7

    Sol[1] = Cnt[2][0]
    Sol[4] = Cnt[4][0]
    Sol[7] = Cnt[3][0]
    Sol[8] = Cnt[7][0]

    Seg[0] = (Sol[7]-Sol[1]).pop()    # a (unused)

    for x in Cnt[6]:      # 0 6 9
        if not Sol[1]<x:  # !contains 1 => 6
            Sol[6] = x
        elif Sol[4]<x:    #  contains 4 => 9
            Sol[9] = x
        else:             # 0
            Sol[0] = x

    Seg[5] = (Sol[6]&Sol[1]).pop()    # f
    Seg[2] = (Sol[1]-{Seg[5]}).pop()  # c
    Seg[3] = (Sol[8]-Sol[0]).pop()    # d (unused)
    Seg[4] = (Sol[8]-Sol[9]).pop()    # e (unused)

    for x in Cnt[5]:           # 2 3 5
        if Seg[5] not in x:    # !f => 2
            Sol[2] = x
        elif Seg[2] not in x:  # !c => 5
            Sol[5] = x
        else:                  # 3
            Sol[3] = x

    Seg[1] = (Sol[4]-Sol[3]).pop()        # b (unused)
    Seg[6] = (Sol[8]-set(Seg[:6])).pop()  # g (unused)

    decod = 0
    for d in code:
        decod = 10*decod + Sol.index(set(d))
    return decod

print(sum(solve_pb(*pb) for pb in Pbs))
