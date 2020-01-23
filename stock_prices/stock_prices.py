#!/usr/bin/python

import argparse
# i     p
# [1050,270,1540,3800,2]


def find_max_profit(prices):
    min_price = prices[0]
    max_profit = float("-inf")
    for i in range(len(prices)):

        if min_price > prices[i]:
            min_price = prices[i]

        for p in range(i+1, len(prices)):
            current_profit = prices[p] - prices[i]
            if max_profit < current_profit:
                max_profit = current_profit

    return max_profit


    # pass
# print(find_max_profit([1050, 270, 1540, 3800, 2]))
if __name__ == '__main__':
            # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
