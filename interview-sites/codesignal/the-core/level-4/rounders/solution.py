# https://app.codesignal.com/arcade/code-arcade/loop-tunnel/H5PP5MXvYvWXxTytH

def rounders(n: int) -> int:
    if n <= 10:
        return n

    n = list( map(int, list(str(n))) )
    l = len(n)
    for i in range(l-1, 0, -1):     
        if int(n[i]) >= 5:
            n[i-1] += 1
            
        n[i] = 0
        
    return int(''.join(map(str, n)))
