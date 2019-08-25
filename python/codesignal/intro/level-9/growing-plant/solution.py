# https://app.codesignal.com/arcade/intro/level-9/xHvruDnQCx7mYom3T

def growingPlant(upSpeed, downSpeed, desiredHeight):
    height = 0
    day = 1
    
    while True:
        height += upSpeed
        if height >= desiredHeight: return day
        height -= downSpeed
        day += 1
