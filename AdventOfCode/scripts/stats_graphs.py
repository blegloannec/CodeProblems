#!/usr/bin/env python3

import sys, requests
import re
import matplotlib.pyplot as plt

YEARS = (2016, 2018, 2019, 2020)  # <= CHANGE THIS
URL = 'https://adventofcode.com/{}/leaderboard/self'
HEADERS = {
    'Cookie': 'session='  # <= PASTE COOKIE HERE
}

def plot_top(board, top=100, label=True):
    # part 1
    X = [int(line[0]) for line in board]
    Y = [int(line[2]) for line in board]
    Y = [y if y <= top else None for y in Y]
    plt.plot(X, Y, ls=' ', marker='*', mfc='#9999cc', mec='#9999cc')
    if label:
        for x,y in zip(X,Y):
            if y is not None:
                plt.annotate(str(y), (x,y), textcoords='offset points',
                             xytext=(4,0), ha='left', va='center')
    # part 2
    Y = [int(line[5]) for line in board]
    Y = [y if y <= top else None for y in Y]
    plt.plot(X, Y, ls=' ', marker='*', mfc='gold', mec='gold')
    if label:
        for x,y in zip(X,Y):
            if y is not None:
                plt.annotate(str(y), (x,y), textcoords='offset points',
                             xytext=(4,0), ha='left', va='center')

def plot_stats():
    plt.rc('font', size=8)
    plt.margins(tight=True)
    H = len(YEARS)
    for idx, year in enumerate(YEARS):
        url = URL.format(year)
        print(f'Extracting year {year}...', end=' ', flush=True)
        req = requests.get(url, headers=HEADERS)
        req.encoding = 'utf-8'
        board = re.search(r'Score</span>([^<]*)</pre>', req.text).group(1).strip().split('\n')
        board = [line.split() for line in reversed(board)]
        # top 100
        ax = plt.subplot(H, 2, 2*idx+1)
        plt.title(f'{year} - top 100', loc='left', pad=1.,
                  fontdict={'fontsize': 9, 'fontweight': 'bold'})
        ax.set_xlim(0, 26)
        ax.set_xticks(range(1, 26))
        ax.set_ylim(0, 101)
        ax.set_yticks([1]+list(range(10, 101, 10)))
        ax.tick_params(labelsize='small')
        plot_top(board)
        # top 1000
        ax = plt.subplot(H, 2, 2*idx+2)
        plt.title(f'{year} - top 1000', loc='left', pad=1.,
                  fontdict={'fontsize': 9, 'fontweight': 'bold'})
        ax.set_xlim(0, 26)
        ax.set_xticks(range(1, 26))
        ax.set_ylim(0, 1001)
        ax.set_yticks([1]+list(range(100, 1001, 100)))
        ax.tick_params(labelsize='small')
        plot_top(board, 1000, False)
        print('done')
    plt.tight_layout(pad=1.)
    plt.show()

if __name__=='__main__':
    plot_stats()
