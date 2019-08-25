# https://app.codesignal.com/arcade/code-arcade/list-forest-edge/bq2XnSr5kbHqpHGJC

from typing import List

def makeArrayConsecutive2(statues: List[int]) -> int:
    min_height, max_height = min(statues), max(statues)
    return len(range(min_height, max_height + 1)) - len(statues)
