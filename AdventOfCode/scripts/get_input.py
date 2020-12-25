#!/usr/bin/env python3

import sys, datetime, requests

YEAR = 2020  # <= CHANGE THIS
URL = f'https://adventofcode.com/{YEAR}/day/{{}}/input'
HEADERS = {
    'Cookie': 'session='  # <= PASTE COOKIE HERE
}


def dl_in(day):
    assert 0 < day <= 25
    url = URL.format(day)
    fname = f'input{day:02d}'
    print(f'Downloading {url} as ./{fname}...', end=' ', flush=True)
    req = requests.get(url, headers=HEADERS)
    out = open(fname, 'w')
    out.write(req.text)
    out.close()
    print('done.')


if __name__=='__main__':
    if len(sys.argv)>1:
        day = int(sys.argv[1])
    else:
        day = datetime.date.today().day
    dl_in(day)
