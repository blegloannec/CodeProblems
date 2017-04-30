#!/usr/bin/env python3

from urllib.request import urlopen
import json

keys_url = 'https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/secret/key.json'
json_dir = 'https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/secret/secret_json/'

S = []
keys_json = urlopen(keys_url).read().decode('utf-8')
for key in json.loads(keys_json):
    secret_json = urlopen(json_dir+key+'.json').read().decode('utf-8')
    S.append(json.loads(secret_json)['news_title'])
S.sort()
for s in S:
    print(s)
