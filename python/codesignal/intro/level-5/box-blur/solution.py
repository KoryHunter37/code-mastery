# https://app.codesignal.com/arcade/intro/level-5/5xPitc3yT3dqS7XkP

from statistics import mean
from math import floor

def boxBlur(image):
    height = len(image)
    width = len(image[0])
    
    result = []
    for h in range(1, height - 1):
        result.append([])
        for w in range(1, width - 1):
            UL = image[h-1][w-1]
            UU = image[h-1][w  ]
            UR = image[h-1][w+1]
            SL = image[h  ][w-1]
            SS = image[h  ][w  ]
            SR = image[h  ][w+1]
            DL = image[h+1][w-1]
            DU = image[h+1][w  ]
            DR = image[h+1][w+1]
            
            average = floor(mean([UL, UU, UR, SL, SS, SR, DL, DU, DR]))
            
            result[-1].append(average)
            
    return result
            