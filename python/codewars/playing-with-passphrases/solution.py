# https://www.codewars.com/kata/playing-with-passphrases/train/python

from string import ascii_uppercase, digits

def play_pass(s, n):
    # Rotate Letters and Update Numbers
    s = s.upper()    
    ascii_uppercase_r = ascii_uppercase[n:] + ascii_uppercase[:n]    
    s = s.translate(str.maketrans(ascii_uppercase + digits, ascii_uppercase_r + digits[::-1]))
    
    # Capitalize or Decapitalize based on index
    s = list(s)
    s = [s[i].upper() if i % 2 == 0 else s[i].lower() for i in range(len(s))]
    s = ''.join(s)
    
    return s[::-1]