# https://app.codesignal.com/arcade/intro/level-2/bq2XnSr5kbHqpHGJC

def makeArrayConsecutive2(statues):
    statues = sorted(statues)
    gap = statues[-1] - statues[0]
    
    return gap - len(statues) + 1
