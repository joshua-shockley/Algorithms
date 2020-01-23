#!/usr/bin/python

import sys
# import itertools

# list = [['rock'], ['paper'], ['scissors']]

# permutations = itertools.permutations(list, 3)


# for i in permutations:
#     print(i)


def rock_paper_scissors(n):
    if n == 0:
        # could onl know this when looking at the test file...apparently thats ok
        return [[]]
    elif n == 1:
        return [['rock'], ['paper'], ['scissors']]
    else:
        # this makes it recursive as 'adding' is what is being repeated until it gets to 1 or 0 the it returns those values then ends
        adding = rock_paper_scissors(n-1)
        nl = []  # sets up a list to enter new info that's being repeated
        # this loops through the i(index of each version of fn being returned?)
        for i in adding:
            # this adds the new value of i into the front of each list
            nl += [i+['rock'], i+['paper'], i+['scissors']]

        return nl  # finally returns the new list after doing the recursion


print(rock_paper_scissors(3))

# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_plays = int(sys.argv[1])
#     print(rock_paper_scissors(num_plays))
#   else:
#     print('Usage: rps.py [num_plays]')
