# https://www.codewars.com/kata/string-incrementer/train/python

# You can import a string called 'digits' from the string library.
# REFERENCE: https://docs.python.org/3/library/string.html
# It contains a string which looks like this: '0123456789'
from string import digits

def increment_string(strng):  

    # The rstrip method can strip all of the specified characters off the right side of a string
    # Since we specify '0123456789', it removes the digits and keeps the text on the left-side of the number
    # TRY IT: https://www.programiz.com/python-programming/methods/string/rstrip
    text = strng.rstrip(digits)
    
    # Now we can seperate the number by slicing from the index of the end of the text onwards
    num = strng[len(text):]
    
    # Store the length of the string which represents the numerical part
    num_length = len(num)
    
    # In the case where we have at least a number of zero or more...
    if num_length > 0:
    
        # Convert the string to an integer and add one to it
        num = int(num)
        num += 1
        
        #  Convert it back into a string
        num = str(num)
        
        # The zfill method allows you to format a string with a specified number of zeroes in front of it,
        # and we can use the original length of the ORIGINAL numerical string as the maximum space to fill with zeroes.
        # TRY IT: https://www.programiz.com/python-programming/methods/string/zfill
        num = num.zfill(num_length)
        
    # In the case where there is no number...
    else:
        num = '1'      

    return text + num
