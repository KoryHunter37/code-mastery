# https://www.codewars.com/kata/catching-car-mileage-numbers/train/python

def is_interesting(number, awesome_phrases):

    def interesting(n):
        # A number is only interesting if it is greater than 99!
        if n < 100:
            return False
            
        s = str(n)
        
        # Any digit followed by all zeros
        if s[0] != '0' and s[1:] == '0' * (len(s) - 1):
            return True
        
        # Every digit is the same number
        if len(set(s)) == 1:
            return True
            
        # The digits are sequential, incementing
        digits = [int(d) for d in s]
        if all(digits[i] + 1 == digits[i+1] or digits[i] == 9 and digits[i+1] == 0 for i in range(len(digits)-1)):
            return True
            
        # The digits are sequential, incementing
        if all(digits[i] - 1 == digits[i+1] for i in range(len(digits)-1)):
            return True
            
        # The digits are a palindrome
        if s == s[::-1]:
            return True
            
        # The digits are in the awesome_phrases array
        if n in awesome_phrases:
            return True
            
        return False
        
    if interesting(number):
        return 2
    elif interesting(number+1) or interesting(number+2):
        return 1
        
    return 0
