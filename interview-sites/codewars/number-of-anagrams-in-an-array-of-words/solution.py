# https://www.codewars.com/kata/number-of-anagrams-in-an-array-of-words/train/python

from collections import Counter, defaultdict

def anagram_counter(words):
    d = defaultdict(int)
    for word in words:
        d[frozenset(Counter(word))] += 1

    return sum( sum(range(v-1, 0, -1)) for v in d.values())
