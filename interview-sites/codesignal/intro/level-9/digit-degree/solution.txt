# https://app.codesignal.com/arcade/intro/level-9/hoLtYWbjdrD2PF6yo

def digitDegree(n):
    degree = 0
    
    while len(str(n)) > 1:
        n = sum(int(i) for i in str(n))
        
        degree += 1
    
    return degree
