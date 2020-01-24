#!/usr/bin/python
"""
what pattern can we find
10 cents

ten pennies
1111111111
5 pennies 1 nickle
111115
2 nickles
55
1 dime
(10)
0 half dollars
0(50)

"""
import sys
# denominations = [1, 5, 10, 25, 50]
# amount = 40
# def making_change(amount, denominations):
#   # denominations is a list of the coin values available
#   # amount is input in cents
#   # input of 0 and 1 come back with 1 set that condition
#     if amount == 0:
#         return 1
#     if amount == 1:
#         return 1
#     else:
#         print('not 0 or 1 currently')
#         count = 0
#         # set loop that runs though levels of coin that add up to amount and save the combo if it passes check
#         for v in denominations:
#             combo = []
#             combo_set = []
#             if v == amount:
#                 count += 1
#                 combo_set.append
#                 print(combo, v, f'count : {count}')
#             elif v < amount:
#                 combo.append(v)
#                 remainder = amount % v
#                 division = amount / v
#                 print(remainder, v, division)
#                 v = v-1
#     return combo
# print(making_change(amount, denominations))


# was unable to figure this out on my own and in after hours this code was donated for us to review and even with the tl we couldnt quite pick out how this entirely funcioned

def making_change(amount, denominations):
    if amount == 0:
        return 1
    if amount < 0:
        return 0
    if len(denominations) <= 0 and amount > 0:
        return 0
    else:
        return making_change(amount - denominations[-1], denominations) + making_change(amount, denominations[:-1])


if __name__ == "__main__":
        # Test our your implementation from the command line
        # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
