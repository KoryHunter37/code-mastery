# any(iterable)

# Return True if one or more of the elements are considered True
# Elements are considered False if they equate to False or None

# > True
# All elements exist, so they are all considered True
print(any([1, 2, 3]))

# > False
# Empty lists are considered False, as no elements are True
print(any([]))

# > True
# First element is True
print(any([2 == 2, 3 == 4, None, False]))

# > False
# All elements are False
print(any([None, False, 5 < 3]))