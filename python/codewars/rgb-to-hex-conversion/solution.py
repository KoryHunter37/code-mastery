# https://www.codewars.com/kata/rgb-to-hex-conversion/train/python

def rgb(r, g, b):
    hexadecimal = []
    
    for color in [r, g, b]:
        
        # Ensure value is in the bounds 0 to 255
        value = min( max(0, color), 255 )
        # Convert to hexadecimal
        value = hex(value)
        # Properly format to be a two character representation
        value = value[2:].rjust(2, '0')
        
        # Add the two character representation to the final result
        hexadecimal.append(value)

    # Capitalize all letters and return final result
    return ''.join(e.upper() for e in hexadecimal)
