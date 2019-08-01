def dec_to_bin(number):
    if number < 2:
        if number == 1:
            return "1"
        else:
            return "0"
            
    return dec_to_bin(number/2) + dec_to_bin(number%2)
    