from collections import Counter

def duplicate_items(list_numbers):
    count = Counter(list_numbers)
    
    redundant_numbers = []
    for key in count.keys():
        if count[key] > 1:
            redundant_numbers.append(key)
    
    return sorted(redundant_numbers)


