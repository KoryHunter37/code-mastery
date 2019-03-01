def find_missing_number(list_numbers):
    one_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    missing_number = [x for x in one_to_ten if x not in list_numbers]
    return missing_number[0]
