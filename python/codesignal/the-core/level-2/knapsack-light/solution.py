# https://app.codesignal.com/arcade/code-arcade/at-the-crossroads/r9azLYp2BDZPyzaG2

def knapsackLight(value1: int, weight1: int, value2: int, weight2: int, maxW: int) -> int:
    return max( int(weight1 <= maxW)*value1,  int(weight2 <= maxW)*value2, int(weight2 + weight1 <= maxW)*(value1 + value2))
