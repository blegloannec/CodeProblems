#!/usr/bin/env python3

import sys, os.path
import requests, bs4
import io, zipfile
import argparse


URL = 'https://open.kattis.com/problems/'

def dump_inputs(problem_id, outputs=False):
    try:
        req = requests.get(URL + problem_id)
        req.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err, file=sys.stderr)
        sys.exit(1)
    print(f'Problem "{problem_id}" found.')
    soup = bs4.BeautifulSoup(req.text, 'lxml', multi_valued_attributes=None)
    i = 1
    for table in soup.find_all('table'):
        if table['class']=='sample':
            tds = table.find_all('tr')[1].find_all('td')
            fname = f'in_{problem_id}_{i}'
            print(f'Writing sample input {i} to {fname}...')
            with open(fname, 'w') as F:
                F.write(tds[0].pre.string)
            if outputs:
                fname = f'out_{problem_id}_{i}'
                print(f'Writing sample output {i} to {fname}...')
                with open(fname, 'w') as F:
                    F.write(tds[1].pre.string)
            i += 1
    print('Done.')


URL_ZIP = 'https://open.kattis.com/problems/{}/file/statement/samples.zip'

def dump_inputs_from_zip(problem_id, outputs=False):
    try:
        req = requests.get(URL_ZIP.format(problem_id))
        req.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err, file=sys.stderr)
        sys.exit(1)
    print('Zip downloaded.')
    z = io.BytesIO(req.content)
    with zipfile.ZipFile(z, 'r') as Z:
        for f in Z.namelist():
            fname = None
            if f.endswith('.in'):
                fname = f'in_{problem_id}_{f[:-3]}'
            elif outputs and f.endswith('.ans'):
                fname = f'out_{problem_id}_{f[:-4]}'
            if fname is not None:
                # we could use Z.extract() but this does not allow to choose
                # the file name and there is no proper naming convention for
                # for the content of the archive
                # hence, "manually" writing data to a file
                # (an alternative would be to rename the extracted file afterwards)
                with open(fname, 'wb') as F:
                    print(f'Extracting {f} as {fname}...')
                    F.write(Z.read(f))
    print('Done.')


def main():
    parser = argparse.ArgumentParser(description='Kattis samples downloader')
    parser.add_argument('problem', nargs='+')
    parser.add_argument('--source', '-s', choices=('zip', 'html'), default='zip')
    parser.add_argument('--out', '-o', action='store_true')
    args = parser.parse_args()
    for pb in args.problem:
        pb_id = os.path.splitext(pb)[0]
        if args.source=='html':
            dump_inputs(pb_id, args.out)
        else:  # slightly faster in general
            dump_inputs_from_zip(pb_id, args.out)

if __name__=='__main__':
    main()
