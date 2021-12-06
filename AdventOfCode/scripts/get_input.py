#!/usr/bin/env python3

import sys, datetime, requests

TODAY = datetime.date.today()
URL = 'https://adventofcode.com/{}/day/{}/input'
COOKIES = {
    'session': ''  # <= PASTE COOKIE HERE
}


def dl_in(year, day):
    assert 2015 <= year <= TODAY.year
    assert 0 < day <= 25
    url = URL.format(year, day)
    fname = f'input{day:02d}'
    print(f'Downloading {url} as ./{fname}...', end=' ', flush=True)
    req = requests.get(url, cookies=COOKIES)
    with open(fname, 'w') as out:
        out.write(req.text)
    print('done.')


if __name__=='__main__':
    if len(sys.argv)==2:
        year = TODAY.year
        day  = int(sys.argv[1])
    elif len(sys.argv)==3:
        year = int(sys.argv[1])
        day  = int(sys.argv[2])
    else:
        year = TODAY.year
        day  = TODAY.day
    dl_in(year, day)
