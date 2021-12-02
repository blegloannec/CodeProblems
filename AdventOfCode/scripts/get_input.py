#!/usr/bin/env python3

import sys, datetime, requests

YEAR = 2021  # <= CHANGE THIS
URL = f'https://adventofcode.com/{YEAR}/day/{{}}/input'
COOKIES = {
    'session': ''  # <= PASTE COOKIE HERE
}


def dl_in(day):
    assert 0 < day <= 25
    url = URL.format(day)
    fname = f'input{day:02d}'
    print(f'Downloading {url} as ./{fname}...', end=' ', flush=True)
    req = requests.get(url, cookies=COOKIES)
    with open(fname, 'w') as out:
        out.write(req.text)
    print('done.')


if __name__=='__main__':
    if len(sys.argv)>1:
        day = int(sys.argv[1])
    else:
        day = datetime.date.today().day
    dl_in(day)
