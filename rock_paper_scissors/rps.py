#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    options = [['rock'], ['paper'], ['scissors']]
    plays = []
    if n <= 0:
        return "no players"
    elif n == 1:
        return options
    else:
        for i in options:
            plays = i+['rock'], i+['paper'], i+['scissors']
    return plays


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
