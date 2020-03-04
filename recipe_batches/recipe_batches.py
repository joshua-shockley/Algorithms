#!/usr/bin/python

import math

# this looks at dict called recipe and dict called ingredients
# then it should determine if there is enough ingredients to make what the recipe calls for
# the return is to be a max number of batches that can be created out of what is there


def recipe_batches(recipe, ingredients):
    ingreds_count = {}
    batches = float('inf')
    for keys, values in recipe.items():
        if keys not in ingredients:
            batches = 0
            return batches
        else:
            print(keys, values)
            if recipe[keys] > ingredients[keys]:
                batches = 0  # can't make what we dont have enough for
                return batches
            elif recipe[keys] <= ingredients[keys]:
                floor = ingredients[keys]//recipe[keys]
                ingreds_count[keys] = floor
                print('ingreds_count:', ingreds_count)
                print('floor: ', floor)
            for keys, values in ingreds_count.items():
                if ingreds_count[keys] < batches:
                    batches = ingreds_count[keys]
    return batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
