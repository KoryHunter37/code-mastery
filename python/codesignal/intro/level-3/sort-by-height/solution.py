# https://app.codesignal.com/arcade/intro/level-3/D6qmdBL2NYz49XHwM

def sortByHeight(a):
    humans = sorted([height for height in a if height != -1])
    
    for i in range(len(a)):
        if a[i] != -1:
            a[i] = humans.pop(0)
            
    return a
    