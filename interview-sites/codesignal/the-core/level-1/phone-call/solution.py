# https://app.codesignal.com/arcade/code-arcade/intro-gates/mZAucMXhNMmT7JWta

def phoneCall(min1: int, min2_10: int, min11: int, s: int) -> int:
    cost = {0: min1, 1: min2_10, 2: min2_10, 3: min2_10, 4: min2_10, 5: min2_10, 6: min2_10, 7: min2_10, 8: min2_10, 9: min2_10}
    minutes = 0
    
    while s > 0:
        s -= cost.get(minutes, min11)
        if s >= 0:
            minutes += 1
        
    return minutes
        