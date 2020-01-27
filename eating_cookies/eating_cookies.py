#!/usr/bin/python

import sys
# def eating_cookies(n):
#   if n < 0:
#     return 0
#   elif n == 0:
#     return 1
#   else:
#     return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)


def eating_cookies(n, cache=None):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif cache and cache[n] > 0:  # using cache to look back at return values
        return cache[n]
    else:
        if not cache:  # looks in cache and if its not there then runs the recursion
            # sets up the cache to follow along with recursion loop.. this one is dictionary
            cache = {i: 0 for i in range(n+1)}
        cache[n] = eating_cookies(
            n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)  # the recursion fn assigns n to input and stores the return value of each in the dictionary set up
        return cache[n]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
