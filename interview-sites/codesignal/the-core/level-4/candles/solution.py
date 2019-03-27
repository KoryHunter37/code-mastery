# https://app.codesignal.com/arcade/code-arcade/loop-tunnel/LAKReA3CR9EwkZGSz

def candles(candles: int, make: int) -> int:
    leftovers = 0
    count = 0
    
    while candles > 0 or leftovers >= make:
        count += candles
        leftovers += candles
        candles = 0
        
        candles += leftovers // make
        leftovers -= candles * make
        
    return count
