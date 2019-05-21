# https://www.codewars.com/kata/weight-for-weight/train/python

def order_weight(strng):
    arr = strng.split()
    
    result = {}
    
    for weight in arr:
        sum_weight = sum(int(digit) for digit in str(weight))
        
        if sum_weight in result:
            result[sum_weight].append(weight)
        else:
            result[sum_weight] = [weight]
          
          
    result = {key:sorted(value) for (key, value) in result.items()}
    
    final_result = []
    for key in sorted(result.keys()):
        final_result.extend(result[key])
    
    return ' '.join(final_result)
    