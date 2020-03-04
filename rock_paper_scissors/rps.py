#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    options = [['rock'], ['paper'], ['scissors']]
    plays = []
    if n <= 0:
        return [[]]
    elif n == 1:
        return options
    else:
        # this sets up the recursion... goes by one less each time giving all the versions
        compile = rock_paper_scissors(n-1)
        for i in compile:
            plays += i+['rock'], i+['paper'], i+['scissors']

        return plays


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
