# https://leetcode.com/problems/self-dividing-numbers/description/

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        
        numbers = []
        for n in range(left, right+1):
            numbers.append(n)
            
        chosen_numbers = []
        for number in numbers:
            str_number = str(number)
            
            if "0" in str_number:
                continue
            
            valid = True
            for i in range(0, len(str_number)):
                if number % int(str_number[i]) != 0:
                    valid = False
            if valid:       
                chosen_numbers.append(number)
        
        return chosen_numbers