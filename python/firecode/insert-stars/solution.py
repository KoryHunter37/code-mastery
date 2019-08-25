def insert_star_between_pairs(a_string):
    if a_string is None:
        return None
        
    a_list = list(a_string)
    output = []
    
    for i in range(0, len(a_list) - 1):
        if a_list[i] == a_list[i+1]:
            output.append(a_list[i])
            output.append("*")
        else:
            output.append(a_list[i])
            
    if len(a_list) >= 2:
        output.append(a_list[-1])
    
    return "".join(output)
