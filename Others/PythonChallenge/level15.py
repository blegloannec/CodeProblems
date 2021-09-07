#!/usr/bin/env python
# -*- coding: utf-8 -*-

import calendar

print 'Looking for leap years, with January 26 on Monday, between 1006 and 1996...'

c = calendar.Calendar(0)
for y in range(1006,1997,10):
    if calendar.isleap(y):
        for w in c.monthdays2calendar(y,1):
            if (26,0) in w:
                print y

print 'Second youngest born on 27 January 1756...'
print '--> Mozart'
