**<span style="text-decoration:underline;">Python Study (Standard Types: Sets):</span>**



---


**<span style="text-decoration:underline;">set:</span>**

sets are mutable unordered collections, which do not allow duplicates. set items must be immutable.

**set parameters are as follows:**

• iterable = an optional iterable used to populate the elements of the set by default.

**set functions are as follows:**

• add(x), where x is an element to add to the set, which adds the element to the set. if the element is already in the set, nothing changes.

• remove(x), where x is an element to remove from the set, which removes the element from the set. if the element is not found, an error occurs.

• copy(), which returns a shallow copy of the original set.

• clear(), which removes all elements from the set.

• difference(other), where other is another set, which returns the difference between the two sets in the form of a set. the difference can be considered as the values of the original set, minus the values which appear in the other set.

• difference_update(other), where other is another set, which modifies the original set to be the difference between itself and the other set.

• discard(x), where x is an element to remove from the set, which removes the element from the set. if the element is not found, an error occurs.

• intersection(others), where others is an arbitrary amount of other sets. this returns the intersection, meaning elements which are found in all listed sets, in the form of a new set.

• intersection_update(others), where others is an arbitrary amount of other sets, which modifies the original set to be the intersection of all listed sets.

• isdisjoint(other), where other is another set, which returns True if there are no shared elements between the original set and the other set, or False if there are any.

• issubset(other), where other is another set, which returns True if all elements in the original set are also listed in the other set, or False if not.

• issuperset(other), where other is another set, which returns True if all elements in the other set are also listed in the original set, or False if not.

• pop(), which returns a random element from the set, and removes that element from the set.

• symmetric_difference(other), where other is another set, which returns a new set containing elements which are only either in the original set or only in the other set.

• symmetric_difference_update(other), where other is another set, which modifies the original set to be the symmetric difference between itself and the other set.

• union(others), where others is an arbitrary amount of other sets, which returns a new set featuring the combined set of elements from all listed sets. this operation may also be performed by using the vertical line operator.

• update(data), where data is a collection such as a set, list, tuple, string, or dictionary, which adds all of the elements in that collection to the set. if the collection is a dictionary, the keys will be used rather than the values.



---


**<span style="text-decoration:underline;">frozenset:</span>**

sets are immutable unordered collections, which do not allow duplicates. frozensets can be items within sets, because they are immutable.

**frozenset parameters are as follows:**

• iterable = an optional iterable used to populate the elements of the set by default.

**frozenset functions are the same as those of set, however, functions which would modify the set are not available due to a frozenset being immutable.**