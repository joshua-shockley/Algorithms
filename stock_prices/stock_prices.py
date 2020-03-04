#!/usr/bin/python

import argparse

# prices is  list of stock prices as integers
# can run test by add space between the numbers after python3 stock_prices.py in the terminal

# setup so need to have a smallest that comes before the largest the smallest price is the purchase price and the largest is the sale price.
# should be max price subtracted by the smallest price. the smallest must come before the largest as you cant sell something you did buy yet
# this is  a running possible total... will change as the list gets bigger


def find_max_profit(prices):
    # starts at the first index since max has to come after this min_price
    min_price = prices[0]
    # maybe we loose money on best case.. starting with lowest possibe int
    max_profit = float("-inf")
    for i in range(len(prices)):
        if min_price > prices[i]:  # during loop sets the new minimum
            min_price = prices[i]

            for p in range(i+1, len(prices)):  # max has to come after min price
                # does the profit math then compares with each index after returning the biggest
                current_profit = prices[p] - prices[i]
                if max_profit < current_profit:
                    max_profit = current_profit
    return max_profit


# print(find_max_profit([1050, 270, 1540, 2800, 2]))
# print(find_max_profit([15, 2, 10, 56, 22, 84, 1, 17]))
if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
