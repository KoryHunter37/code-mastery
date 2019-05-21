# https://www.codewars.com/kata/rot13-1/train/python

import string
from codecs import encode as _dont_use_this_

def rot13(message):
    abc = string.ascii_lowercase
    ABC = string.ascii_uppercase
    abc13 = abc[13:] + abc[:13]
    ABC13 = ABC[13:] + ABC[:13]
    return message.translate(string.maketrans(abc + ABC, abc13 + ABC13))
