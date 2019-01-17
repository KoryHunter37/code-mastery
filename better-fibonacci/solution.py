def better_fibonacci(n):
    prev = None
    curr = None
    for i in range (0, n + 1):
        if i == 0:
            prev = 0
            curr = 0
        if i == 1:
            prev = 0
            curr = 1
        else:
            temp = curr
            curr = curr + prev
            prev = temp
    
    return curr
        