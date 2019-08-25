# bool([x])

# Return a Boolean value of True or False.
# Items are False if they are False, Zero, None, or an Empty Collection.

# > True
print(bool(True))

# > True
print(bool(True or False))

# > False
print(bool(1 and 0))

# > False
print(bool([]))

# > True
# Even though the only element is an empty list, because the collection is not empty, this is considered True.
print(bool([[]]))

# > True
print(bool(["Cat", "Rat", "Bat", 24.81932]))
