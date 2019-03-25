# https://app.codesignal.com/arcade/code-arcade/at-the-crossroads/7jaup9HprdJno2diw

def tennisSet(score1: int, score2: int) -> bool:
    return 7 == max(score1, score2) and 5 <= min(score1, score2) < 7 or 6 == max(score1, score2) and min(score1, score2) < 5
