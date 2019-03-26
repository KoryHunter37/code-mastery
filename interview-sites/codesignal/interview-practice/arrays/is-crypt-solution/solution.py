# https://app.codesignal.com/interview-practice/task/yM4uWYeQTHzYewW9H

from typing import List

def isCryptSolution(crypt: List[str], solution: List[List[str]]):
    crypt = [word.translate(str.maketrans(dict(solution))) for word in crypt]
    
    if crypt != [word.lstrip('0') if len(word) > 1 else word for word in crypt]:
        return False
    
    crypt = list(map(int, crypt))
    return crypt[0] + crypt[1] == crypt[2]
