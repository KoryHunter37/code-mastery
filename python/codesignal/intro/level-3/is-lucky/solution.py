# https://app.codesignal.com/arcade/intro/level-3/3AdBC97QNuhF6RwsQ

def isLucky(n):
    n = [int(x) for x in str(n)]
    
    half = len(n) // 2        
    h1, h2 = n[:half], n[half:]
    
    return sum(h1) == sum(h2)