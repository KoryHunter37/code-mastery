# https://app.codesignal.com/arcade/intro/level-4/xYXfzQmnhBvEKJwXP

def areSimilar(a, b):
    
    error = None
    swapped = False
    for i in range(len(a)):
        # A mismatch has been detected...
        if a[i] != b[i]:
            # If a swap has already been found, the arrays are not similar.
            if swapped:
                return False
            
            # If no error has been found yet, record it.
            if error is None:
                error = i
                
            # If the error has been found, and the previous error can be swapped to this index, swap.
            elif a[error] == b[i] and a[i] == b[error]:
                swapped = True
                
            # If the error has been found, and the previous error cannot be swapped to this index, the arrays are not similar.
            else:
                return False
            
    return True