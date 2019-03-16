# https://app.codesignal.com/arcade/intro/level-2/2mxbGwLzvkTCKAJMG

def almostIncreasingSequence(sequence):  
    
    # Sequence containing only one element is also considered to be strictly increasing.
    if len(sequence) == 1:
        return True
    
    problematic_indices = []
    n_max = float('-inf')
    
    def check_increasing_sequence_without_index(i):
        if sequence[:i] + sequence[i+1:] == sorted(set(sequence[:i] + sequence[i+1:])):
            return True
    
    for i in range(len(sequence) - 1):   
        n1 = sequence[i]
        n2 = sequence[i+1]
        
        if n2 <= max(n1, n_max):
                if check_increasing_sequence_without_index(i): return True
                if check_increasing_sequence_without_index(i+1): return True
        else:
            n_max = max(n1, n_max)
                
    return False
                