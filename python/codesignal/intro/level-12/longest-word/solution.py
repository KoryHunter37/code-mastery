# https://app.codesignal.com/arcade/intro/level-12/s9qvXv4yTaWg8g4ma

import re

def longestWord(text: str) -> int:
    words = re.findall(r'[A-Za-z]+', text)
    return max(words, key=len)
