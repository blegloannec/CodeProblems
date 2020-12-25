#!/usr/bin/env python3

import sys, re
import requests, bs4

EXCL_DAYS = {2015: (), 2016: (), 2017: (), 2018: (6,), 2019: (), 2020: (1,)}
URL = 'https://adventofcode.com/{}/leaderboard/day/{}'
CSV_DELIM = '\t'


def dump_ranking(year):
    excluded = EXCL_DAYS[year]
    scores = {}
    for day in range(1, 26):
        print(f'Day {day:2d}...', end=' ', flush=True, file=sys.stderr)
        if day in excluded:
            print(f'skipped (excluded in {year}).', flush=True, file=sys.stderr)
            continue
        url = URL.format(year, day)
        req = requests.get(url)
        req.encoding = 'utf-8'
        soup = bs4.BeautifulSoup(req.text, 'lxml')
        for entry in soup.find_all('div', {'class': 'leaderboard-entry'}):
            rentry = re.match(r'(\d+)\).*\d\d:\d\d:\d\d +(.+)$', entry.text.strip())
            pos = int(rentry.group(1))
            pts = 101 - pos
            name =  rentry.group(2)
            scores[name] = scores.get(name, 0) + pts
        print('done.', flush=True, file=sys.stderr)

    ranking = sorted(scores.items(), key=(lambda ns: ns[1]), reverse=True)
    prev_scr = None
    for pos, (name, scr) in enumerate(ranking):
        rank = prev_rank if scr==prev_scr else pos+1
        print(CSV_DELIM.join((f'{rank:3d}', f'{scr:4d}', name)))
        prev_rank = rank
        prev_scr = scr


if __name__=='__main__':
    try:
        year = int(sys.argv[1])
        assert year in EXCL_DAYS
    except (IndexError, TypeError, AssertionError):
        print(f'usage: {sys.argv[0]} YEAR > ranking.csv', file=sys.stderr)
        sys.exit(1)
    dump_ranking(year)
