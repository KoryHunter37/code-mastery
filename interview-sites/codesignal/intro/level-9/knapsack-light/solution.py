# https://app.codesignal.com/arcade/intro/level-9/r9azLYp2BDZPyzaG2

def knapsackLight(value1, weight1, value2, weight2, maxW):
    if weight1 + weight2 <= maxW:
        return value1 + value2
    elif weight1 <= maxW and weight2 <= maxW:
        return max(value1, value2)
    elif weight1 <= maxW:
        return value1
    elif weight2 <= maxW:
        return value2
    return 0
