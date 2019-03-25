# https://app.codesignal.com/arcade/code-arcade/at-the-crossroads/J7PQDxpWqhx7HrvBZ

from typing import List

def metroCard(lastNumberOfDays: int) -> List[int]:
    return {28: [31], 30: [31], 31: [28, 30, 31]}.get(lastNumberOfDays)
