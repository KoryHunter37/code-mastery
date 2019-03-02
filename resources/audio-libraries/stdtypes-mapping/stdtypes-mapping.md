**<span style="text-decoration:underline;">Python Study (Standard Types: Mapping):</span>**

types which map hashable values to arbitrary objects.



---


**<span style="text-decoration:underline;">dict:</span>**

key and value pairs, where a given key is associated with a particular value. they are ordered by insertion.

**dict parameters are as follows:**

• kwarg, where kwarg is an arbitrary amount of keyword and value pairs. for example: one="a", two="b", three="c". note that these must be valid function keywords, so they cannot start with a number or be a string, etc. \
• you may also declare a dict with an iterable, if that iterable is a list of key and value pairs, and you can even list keyword and value pairs after it just like in the original method.

• you may also declare a dict by simply using curly braces around a mapping, with the syntax of the mapping as: keyword colon value, separating each entry with commas.

**dict functions are as follows:**

• clear(), which removes all items from the dict. \
• copy(), which returns a shallow copy of the dict. \
• fromkeys(sequence [, value]), where sequence is a list of keys, where value is an optional value to map those keys to, which returns a new dictionary with all of the items in sequence as keys, which are all mapped to the value in value. if no value is specified, they will be mapped to None.

• get(key [, value]), where key is a key to search for, where value is an optional value to return if the key is not found, which returns the value associated with they key if it is found. if the default value is not specified, then None will be returned if the key is not found.

• items(), which returns a dictview, which is essentially a list of tuples, where the first element is the key and the second element is the value, for all mappings in the dict.

• keys(), which returns a dictview, which is essentially a list of all keys in the dict.

• values(), which returns a dictview, which is essentially a list of all values in the dict.

• popitem(), which returns and removes the last item inserted into the dict, as a tuple.

• setdefault(key [, default_value]), where key is a key to search for, where default_value is an optional value to potentially use if that key is not found, which attempts to insert the key into the dictionary with the value default_value, unless the key is already in the dictionary. 

it also returns several things based on context: if the key is in the dictionary, it returns the value. if the key is not in the dictionary, it returns the value of default_value. default_value is None if not specified.

• pop(key [, default]), where key is a key to search for, where default is an optional value to return if that key is not found, which removes and returns the value of the key if found, otherwise returning the value of default. if default is not specified, and the key is not found, an error will be raised.

• update([other]), where other is an optional iterable or dictionary, which updates the keys and values of the dictionary to include those found in other. if a key specified in other already has a value in the dictionary, the key in the original dictionary will have its value updated to equal that of other.

**additional dictionary information is as follows:**

• you can access dictionary values by index much like lists, with the syntax my_dictionary, followed by the key to search for in square brackets, to return the value mapped to that key. if the key is not found, this will raise an error.

• you can also set keys to new values in the same way. \
• you can also delete keys from dictionaries by using the del keyword, then accessing the dictionary value in the same way. if the key is not found, this will raise an error.