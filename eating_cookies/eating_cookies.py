#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution

# BELOW IS A WORKING VERSION I SAW BEFORE... will come back to this to see if i find another way to code this.


def eating_cookies(n, cache=None):
    if n < 0:  # can't eat a negative numver of cookies
        return 0
    elif n == 0:  # there can only be one way to eat 0 or 1 cookie
        return 1
    # if in cache made in the arg then grab from there to save time
    elif cache and cache[n] > 0:
        return cache[n]  # returns what it found in the cache
    else:
        if not cache:  # not in the cache? then lest put it in there
            # this sets up the cache to follow recursion below
            cache = {i: 0 for i in range(n+1)}
        cache[n] = eating_cookies(
            n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
        # returning the cache[n] value of the recursive fn to add up the results of n-number of cookies can eat at once to get a value as the number slowly gets smaller to base case of 1
    return cache[n]

    # THIS WAS A FIRST ATTEMPT come back to this to write this my own way...
    # for i in choices:
    #     # print(f'in main loop, i value, i index:\n',
    #     #       i, choices.index(i))
    #     floor = int(n)//i
    #     remainder = int(n) % i
    #     print(
    #         f"i: {i} \nindex: {choices.index(i)} \nfloor: {floor} \nremainder: {remainder}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
