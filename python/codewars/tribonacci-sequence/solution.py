# https://www.codewars.com/kata/tribonacci-sequence/train/python

global record

def tribonacci(signature, n):
    record = dict(zip(range(3), signature))
    
    def tribonacci_recursive(n):
        if n in record:
            return record[n]
        else:
            print(n)
            record[n] = tribonacci_recursive(n - 1) + record[n-2] + record[n-3]
            return record[n]
    
    tribonacci_recursive(n)
    return [record[i] for i in range(n)]
