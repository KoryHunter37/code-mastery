# all(iterable)

# Return True if none of the elements are considered False
# Elements are considered False if they equate to False, None, Zero, or are an Empty Collection

# > True
# All elements are considered True
print(all([1, 2, 3]))

# > True
# All evaluate to True
print(all([True, 2 == 2, 5*4 == 20, "CAT"]))

# > False
# Second element is False
print(all([True, False]))

# > False
# Second element is None
print(all([True, None]))

# > True
# Empty lists are considered True, as no elements are False
print(all([]))

# > True
# Empty lists INSIDE lists are considered False elements, making the final result False
print(all([[], True, True]))