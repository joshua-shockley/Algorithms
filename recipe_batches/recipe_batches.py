#!/usr/bin/python
"""
need to determine if the key value for ingredients is divisible to a whole number by recipe
then use the lowest common number to determine how many batches i can make
"""
import math


def recipe_batches(recipe, ingredients):
    max_batches = "-inf"
    rec_k = recipe
    ing_k = ingredients
    batches = []
    print(rec_k.keys(), ing_k.keys())
    if rec_k.keys() == ing_k.keys():
        for i in rec_k:
            batches.append(ing_k[i] // rec_k[i])
            print("batches list", batches)
            max_batches = min(batches)
            print(max_batches)
        if max_batches == 0:
            return max_batches
        if max_batches > 0:
            return max_batches
    else:
        return 0


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
