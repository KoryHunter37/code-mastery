def flip_horizontal_axis(matrix):
    height = len(matrix)
    width = len(matrix[0])
    
    for h in range(height):
        
        swap_index = height - 1 - h
        if swap_index <= h:
            return matrix
        
        temp = matrix[h]
        matrix[h] = matrix[swap_index]
        matrix[swap_index] = temp