# https://app.codesignal.com/arcade/intro/level-8/Rqvw3daffNE7sT7d5

def arrayMaxConsecutiveSum(arr, k):
    
    total = sum(arr[0:k])
    best = total
    
    for i in range(1, len(arr) - k + 1):
            
        total -= arr[i-1]
        total += arr[i+k-1]
        best = max(total, best)
        
    return best
