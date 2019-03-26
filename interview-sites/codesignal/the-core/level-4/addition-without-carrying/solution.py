# https://app.codesignal.com/arcade/code-arcade/loop-tunnel/xzeZqCQjpfDJuN72S

def additionWithoutCarrying(n1: int, n2: int) -> int:
    n1, n2 = str(n1), str(n2)
    maxlen = max(len(n1), len(n2))
    n1, n2 = n1.rjust(maxlen, '0'), n2.rjust(maxlen, '0')
    
    return int(''.join( str(int(n1[i]) + int(n2[i]))[-1] for i in range(maxlen) ))
