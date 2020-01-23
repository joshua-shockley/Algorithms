#!/usr/bin/python

import sys
# import itertools

# list = [['rock'], ['paper'], ['scissors']]

# permutations = itertools.permutations(list, 3)


# for i in permutations:
#     print(i)


def rock_paper_scissors(n):
    poss = [['rock'], ['paper'], ['scissors']]
    if n == 0:
        return []
    elif n == 1:
        return poss
    elif n >= 2:
        nl = []
        for i in range(len(poss)):
            x = poss[i]
            xs = poss[:i] + poss[i+1]
            for p in rock_paper_scissors(xs):
                nl.append(p+[x])
        return nl


#             return [p] + ['rock'], [p]+['paper'], [p]+['scissors']
print(rock_paper_scissors(2))

# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_plays = int(sys.argv[1])
#     print(rock_paper_scissors(num_plays))
#   else:
#     print('Usage: rps.py [num_plays]')
