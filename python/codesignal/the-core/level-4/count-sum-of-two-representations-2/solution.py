# https://app.codesignal.com/arcade/code-arcade/loop-tunnel/hBw5BJiZ4LmXcy92u

def countSumOfTwoRepresentations2(n, l, r):
    
    result = set()
    valid_nums = range(l, r+1)

    for n1 in valid_nums:
        n2 = n - n1
        
        if n2 in valid_nums:
            result.add(tuple(sorted([n1, n2])))
        elif n2 <= 0:
            break
            
    return len(result)
