# ascii(object)

# Return a string (printable representation) of an object.
# Convert non-ASCII characters into escaped characters.
# Uses repr() to find the printable representation.

# > \U0001f525
# Converts the fire emoji, as it is non-ASCII.
print(ascii("🔥"))

# > The price for one serving is \xa5500.
# Converts the yen symbol, but leaves the rest of the string intact.
print(ascii("The price for one serving is ¥500."))