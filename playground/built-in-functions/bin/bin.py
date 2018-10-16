# bin(x)

# Convert an integer number to a binary string prefixed with "0b".
# The result is a valid Python expression.
# This method is reversed by using int() if the "0b" has been removed.
# Alternatives include format() and f-string, which do not contain "0b".

# > 0b1010
# The binary representation of 10, with 0b in front.
print(bin(10))

# > 1010
# The binary representation of 10 (format() method)
print(format(10, 'b'))

# > 1010
# The binary representation of 10 (f-string method)
print(f"{10:b}")

# > 10
# Reverses the binary transformation
print(int(bin(10), 2))

# > 10
# Reverses the binary transformation (format() method)
print(int(format(10, 'b'), 2))

# > 10
# Reverses the binary transformation (f-string method)
print(int(f"{10:b}", 2))
