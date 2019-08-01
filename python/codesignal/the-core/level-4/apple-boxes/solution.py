# https://app.codesignal.com/arcade/code-arcade/loop-tunnel/scG8AFsPuqQGx8Qjf

def appleBoxes(k: int) -> int:
    return sum(m*m if m%2 == 0 else -m*m for m in range(1, k+1) )
