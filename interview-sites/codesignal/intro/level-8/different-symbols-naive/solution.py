# https://app.codesignal.com/arcade/intro/level-8/8N7p3MqzGQg5vFJfZ

from collections import Counter

def differentSymbolsNaive(s: str):
    return len(Counter(s).keys())
