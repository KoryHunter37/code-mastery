def max_gain(input_list):
    best = 0
    for i in range(0, len(input_list)):
        current = input_list[i]
        for j in range(i, len(input_list)):
            compare = input_list[j]
            
            if compare - current > best:
                best = compare - current
                
    return best