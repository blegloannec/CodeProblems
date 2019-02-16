#!/usr/bin/env python3

from datetime import datetime

A = datetime.strptime(input(),'%d.%m.%Y')
B = datetime.strptime(input(),'%d.%m.%Y')
dy = B.year-A.year - int(A.month>B.month or (A.month==B.month and A.day>B.day))
dm = (B.month-A.month)%12 - int(A.day>B.day)
Out = []
if dy>0: Out.append('%d year%s' % (dy,('s' if dy>1 else '')))
if dm>0: Out.append('%d month%s' % (dm,('s' if dm>1 else '')))
Out.append('total %d days' % (B-A).days)
print(', '.join(Out))
