# https://app.codesignal.com/arcade/intro/level-12/YqZwMJguZBY7Hz84T

import re

def sumUpNumbers(s: str) -> int:
    return sum(int(i) for i in re.findall(r'\d+', s))
