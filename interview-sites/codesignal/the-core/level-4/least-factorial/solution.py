# https://app.codesignal.com/arcade/code-arcade/loop-tunnel/7BFPq6TpsNjzgcpXy

def leastFactorial(n: int) -> int:
    def factorials():
        i = 2
        sum = 1
        while True:
            yield sum
            sum *= i
            i += 1
        
    factorial_generator = factorials()
    
    result = next(factorial_generator)
    while result < n:
        result = next(factorial_generator)
        
    return result   
