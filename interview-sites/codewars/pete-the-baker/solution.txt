# https://www.codewars.com/kata/pete-the-baker/train/python

def cakes(recipe, available):
    cakes = {key: available.get(key, -1) // recipe[key] for key in recipe.keys()}
    return max(min(cakes.values()), 0)
    