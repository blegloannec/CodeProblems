#!/usr/bin/env python3

from urllib.request import urlopen
import re

base_url = 'https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/infinite/'
start = 'qds.html'

re_link = re.compile('<a href=([a-z]+\.html)>')
re_secret = re.compile('Secret Phrase: </b>([a-zA-Z]+)</font>')

seen = set([start])
S = []
def dfs(page):
    source = urlopen(base_url+page).read().decode('utf-8')
    for secret in re_secret.findall(source):
        S.append(secret)
    for child in re_link.findall(source):
        if child not in seen:
            seen.add(child)
            dfs(child)

dfs(start)
S.sort()
for s in S:
    print(s)
