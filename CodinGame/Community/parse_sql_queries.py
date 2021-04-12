#!/usr/bin/env python3

import re

sql = re.match(r'SELECT (.*?) FROM (\S*)(?: WHERE (\S*) = (\S*))?(?: ORDER BY (\S*) (ASC|DESC))?', input())
rows = int(input())
Fields = input().split()
Table = [input().split() for _ in range(rows)]

sel = sql.group(1)
if sel=='*': sel = list(range(len(Fields)))
else:        sel = [Fields.index(f) for f in sel.split(', ')]

widx = sql.group(3)
if widx is not None:
    widx = Fields.index(widx)
    wval = sql.group(4)

oidx = sql.group(5)
if oidx is not None:
    oidx = Fields.index(oidx)
    onum = all(re.fullmatch(r'[0-9.]+', line[oidx]) for line in Table)
    orev = sql.group(6)=='DESC'

Out = []
for entry in Table:
    if widx is None or entry[widx]==wval:
        Out.append([entry[fi] for fi in sel])
        if oidx is not None:
            Out[-1].append(float(entry[oidx]) if onum else entry[oidx])

if oidx is not None:
    Out.sort(key=(lambda line: line[-1]), reverse=orev)
    Out = [line[:-1] for line in Out]

print(*(Fields[fi] for fi in sel))
for line in Out: print(*line)
