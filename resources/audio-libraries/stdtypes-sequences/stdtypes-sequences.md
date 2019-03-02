**<span style="text-decoration:underline;">Python Study (Standard Types: Sequences):</span>**

there are three basic sequence types: lists, tuples, and range objects.



---


**<span style="text-decoration:underline;">list:</span>**

lists are mutable ordered sequences, which allow duplicates.

**list parameters are as follows:**

• iterable = an optional iterable used to populate the elements of the list by default. \
• you can also declare a list by listing elements inside of square brackets, or list comprehensions.

**list functions are as follows:**

• append(x), where x is an element which is added to the right side of the list.

• extend(iterable), where iterable is an iterable which has all of its elements appended onto the right side of the list.

• insert(i, x), where i is the index of insertion, where x is the element to insert.

• remove(x), where x is a value to remove from the deque. this will remove the first equivalent element found.

• pop([i]), where i is an optional index to remove, which removes and returns an element from the list. if i is not specified, the last element in the list will be removed and returned.

• clear(), which removes all elements from the list.

• index(x [, start[, stop]]), where x is a value to search for, where start is an optional starting index for the search, where stop is an optional start-dependent stopping index for the search, which returns the position of x.

• count(x), where x is a value to search for, which returns the number of elements equivalent to x.

• sort(key=None, reverse=False), where key is a function which processes the elements in the list before comparing them, where reverse dictates if the sort ordering is normal or backwards, which sorts the list.

• reverse(), which reverses the elements of the list in place.

• copy(), which returns a shallow copy of the list.



---


**<span style="text-decoration:underline;">tuple:</span>**

tuples are immutable ordered sequences, which allow duplicates.

**tuple parameters are as follows:**

• iterable = an optional iterable used to populate the elements of the tuple by default.

**tuple functions are as follows:**

• count(x), where x is a value to search for, which returns the number of elements equivalent to x.

• index(x), where x is a value to search for, which returns the position of x.



---


**<span style="text-decoration:underline;">range:</span>**

ranges are immutable ordered sequences, which represents all numbers between a stopping and starting point.

**tuple parameters are as follows:**

constructor one:

• stop = the last value of the range, exclusive.

• this constructor will default the starting point to one, and the step to one.

constructor two:

• start = the first value of the range, inclusive.

• stop = the last value of the range, exclusive.

• step = the amount to move.



---


**<span style="text-decoration:underline;">str:</span>**

str represent string values.

**str parameters are as follows:**

constructor one:

• object = the value to be converted to a string.

• this constructor will default 

constructor two:

• object = the value to be converted to a string. for example, UTF-8

• encoding = the method for encoding the string.

• errors = the error handler for when decoding fails. can be: strict, which raises an error, ignore, which ignores the error, replace, which replaces it with a question mark, etc.

**str functions are as follows:**

• capitalize(), which returns a copy of the string with its first character capitalized, and the rest lowercased.

• casefold(), which returns a "truly" lowercase copy of the string. this is different than lower(), because it is more aggressive and accounts for foreign languages.

• center(width [, fillchar]), where width is the length of the newly centered string, where fillchar is an optional symbol to fill the space in with, which centers the contents of the string in a new string of length width, and pads it with fillchar. if the string is smaller than width, the original string is returned instead. if there is uneven padding space, the extra space will go on the right. by default, fillchar is a blank space.

• count(sub [, start [, end]]), where sub is a substring to search for, where start is an optional inclusive starting index for the search, where end is an optional start-dependent exclusive stopping index for the search, which returns the number of non-overlapping occurrences of sub in that search range.

• encode(encode="utf-8", errors="strict"), where encoding is a type of encoding for the string, where errors is the error handler when decoding fails, which returns an encoded version of the string as a bytes object.

• endswith(suffix [, start [, end]]), where suffix is a substring to look for at the end of the string, where start is an optional inclusive starting point for where to look for the suffix, where stop is an optional start-dependent exclusive ending point for where to look for the suffix, which returns True or False based on if that suffix is found at the end of the range. suffix can also be a tuple of substrings to look for. 

if any of the suffixes in that tuple match up with the ending, then the result will be True.

• expandtabs(tabsize=8), where tabsize is how many spaces a tab symbol should be replaced with, which returns a copy of the string where all symbols have been replaced with a number of spaces equal to tabsize.

• find(sub [, start [, end]]), where sub is a substring to look for, where start is an optional inclusive starting point for the search, where end is an optional start-dependent exclusive stopping point for the search, which returns the lowest index in the string where the substring is found. If the substring cannot be found, it will return negative one.

• format(*args, **kwargs), where args is a list of unnamed values to fill into the string in place of curly braces, where kwargs is a list of named values to fill into the string in place of curly braces. 

curly braces which match up with a named value in kwargs will always get that value, no matter how many times it is used in the string. 

curly braces which do not match up with a named value in kwargs will be filled by values in args, from left to right. 

there can be more values in args than there are unnamed curly braces to fill, but there cannot be more unnamed curly braces to fill than there are values in args.

• format_map(mapping), where mapping is a dict, which replaces named curly braces in a string with the value of keys in the mapping that have names matching the curly braces.

• index(sub [, start [, end]]), which has the same functionality as find, but raises an error instead of returning negative one.

• isalnum(), which returns True if all characters in the string are alphanumeric and there is at least one character, otherwise returns False.

• isalpha(), which returns True if all characters in the string are alphabetical and there is at least one character, otherwise returns False.

• isascii(), which returns True if all characters in the string are ASCII and there is at least one character, otherwise returns False.

• isdecimal(), which returns True if all characters in the string are decimals and there is at least one character, otherwise returns False.

decimal characters include all characters which can form numbers in base ten.

• isdigit(), which returns True if all characters in the string are digits and there is at least one character, otherwise returns False.

digit characters include decimal characters and digits which need special handling, such as superscripts.

• isidentifier(), which returns True if the string is a valid identifier, otherwise returns False. identifiers are strings which only contain alphanumeric letters, the numbers 0 through 9, or underscores. the string cannot start with a number or contain any spaces.

• islower(), which returns True if all cased characters are lowercase and there is at least one cased character, otherwise returns False.

• isnumeric(), which returns True if all characters in the string are numeric characters, and there is at least one character, otherwise returns False.

• isprintable(), which returns True if all characters in the string are printable, otherwise returns False. some characters, such as escape characters or parts of unicode, are not considered printable.

• isspace(), which returns True if all characters in the string are whitespace, and there is at least one character, otherwise returns False. whitespace includes spaces, tabs, new lines, etc.

• istitle(), which returns True if the string is a title, and there is at least one character, otherwise returns False.

a title is considered to be formatted such that all cased words begin with a capital letter, and all other cased letters in the word are lowercase. 

If a word begins with a non-cased letter and also has letters, such as a number followed by one or more letters, the first letter in that word must be capitalized, and all subsequent letters must be lower case.

• isupper(), which returns True if all characters in the string are uppercase, and there is at least one cased character, otherwise returns False.

• join(iterable), where iterable is an iterable to join together, which returns a new string where all the elements of the iterable are joined together, and separated from one another by the contents of this string. to merge all elements of an iterable with no spacing, simply use this method on an empty string.

• ljust(width [, fillchar]), where width is the length of the newly created string, where fillchar is an optional value to fill any empty spaces with, which returns a new string where the contents of this string are pushed all the way to the left, and any remaining space is filled with fillchar.  by default, fillchar is a blank space. this method stands for left-justified.

• lower(), which returns a copy of the string with all cased characters converted to lowercase.

• lstrip([chars]), where chars is an optional string specifying which characters should be removed from the string, which returns a copy of the string after removing all the characters in chars starting from the left side of the string, up until a character not found in chars is reached.

• split(sep=None, maxsplit= -1), where sep is a substring used to split the string, where maxsplit 

• static maketrans(x [, y [, z]]), where you can either specify just x, just x and y, or x y and z. if only x is specified, it must be a dictionary which will map ordinals to ordinals, or characters to ordinals. if x and y are specified, they should each be strings of equal length, and a mapping of each of their characters ordinal values will be generated. if x y and z are specified, it will work the same, but the characters in string z will be paired with None.

• partition(sep), where sep is a seperator substring to search for and divide the string by, which returns a 3-tuple of the substring before the sep, the sep itself, and then the substring after the sep. this will always divide by the first occurrence of sep. if the separator is not found, return a 3-tuple containing the original string, and then two empty strings.

• replace(old, new [, count]), where old is a substring to replace, where new is a substring to fill with, where count is an optional limit to how many times the replacement can occur, which returns a copy of the string with all instances of the old substring replaced with the new substring, with respect to the count limit.

• rfind(sub [, start [, end]]), where sub is a substring to look for, where start is an optional inclusive starting point for the search, where end is an optional start-dependent exclusive stopping point for the search, which returns the highest index in the string where the substring is found. If the substring cannot be found, it will return negative one.

• rindex(sub [, start [, end]]), which has the same functionality as rfind, but raises an error instead of returning negative one.

• rjust(width [, fillchar]), where width is the length of the newly created string, where fillchar is an optional value to fill any empty spaces with, which returns a new string where the contents of this string are pushed all the way to the right, and any remaining space is filled with fillchar.  by default, fillchar is a blank space. this method stands for right-justified.

• rpartition(sep), where sep is a seperator substring to search for and divide the string by, which returns a 3-tuple of the substring before the sep, the sep itself, and then the substring after the sep. this will always divide by the last occurrence of sep. if the separator is not found, return a 3-tuple containing the original string, and then two empty strings.

• rsplit(sep=None, maxsplit= -1), where sep is a substring used to split the string, where maxsplit is the maximum number of splits which can occur, which returns a list of strings generated by splitting the original string on the separator. the separator itself is not included in the list. if the maxsplit limit is reached, only the right-most separators will be used for splitting. a -1 value for maxsplit means there is no limit on split count.

• rstrip([chars]), where chars is an optional string specifying which characters should be removed from the string, which returns a copy of the string after removing all the characters in chars starting from the right side of the string, up until a character not found in chars is reached.

• split(sep=None, maxsplit= -1), where sep is a substring used to split the string, where maxsplit is the maximum number of splits which can occur, which returns a list of strings generated by splitting the original string on the separator. the separator itself is not included in the list. if the maxsplit limit is reached, only the left-most separators will be used for splitting. a -1 value for maxsplit means there is no limit on split count.

• splitlines([keepends]), where keepends is a boolean value dictating if line break characters should be displayed or not, which returns a list of strings after splitting the string on its line break characters. if keepends is True, meaning the line break characters will be displayed, they will affixed to the end of the line which they break.

• startswith(prefix [, start [, end]]), where prefix is a substring to look for at the start of the string, where start is an optional inclusive starting point for where to look for the prefix, where stop is an optional start-dependent exclusive ending point for where to look for the prefix, which returns True or False based on if that prefix is found at the end of the range. prefix can also be a tuple of substrings to look for. 

if any of the prefixes in that tuple match up with the ending, then the result will be True.

• rstrip([chars]), where chars is an optional string specifying which characters should be removed from the string, which returns a copy of the string after removing all the characters in chars starting from both the left side of the string and the right side of the string, up until a character not found in chars is reached. each direction stops independently of the other, so it will strip from the left until a character not found in chars is reached, and will strip from the right until a character not found in chars is reached.

• swapcase(), which returns a copy of the string with uppercase characters converted to lowercase, and lowercase letters converted to uppercase. weird characters might make using this method twice back to back return a different string from the original.

• title(), which returns a titlecased version of the string, where words start with an uppercase character, and other characters are lowercase.

• translate(table), where table is a mapping, which returns a copy of the string after translating each character in the string with respect to the mapping. use str.maketrans() to create a translation map.

• upper(), which returns a copy of the string with all cased characters converted to uppercase.

• zfill(width), where width represents the width of the new string, which returns a copy of the string but filled with leading zeros up to the length of the specified width. if the original string starts with a + or - sign, that sign is positioned before the zeroes. if width is smaller than the original string, then the original string will be returned instead.

**str constants are as follows:**

• ascii_letters = the combination of all lowercase letters in alphabetical order, and then all uppercase letters in alphabetical order. \
• ascii_lowercase = all lowercase letters in alphabetical order. \
• ascii_uppercase = all uppercase letters in alphabetical order.

• digits = the numbers 0 through 9 in ascending order. \
• hexdigits = the numbers 0 through 9 in ascending order, then lowercase letters a through f in alphabetical order, then uppercase letters a through f in alphabetical order. \
• octdigits = the numbers 0 through 7 in ascending order. \
• punctuation = a variety of ASCII punctuation symbols, brackets, symbols, etc.

• printable = all ASCII characters which are considered printable. \
• whitespace = all ASCII characters which are considered whitespace, including space, tab, new line, etc.