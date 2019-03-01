# https://leetcode.com/problems/string-to-integer-atoi/submissions/

class Solution:
    def myAtoi(self, str: str) -> int:
        """
        :type str: str
        :rtype: int
        """
        
        arr = list(str)
        result = []
        
        sign_found = False
        for letter in arr:
            if sign_found:
                if letter.isdigit():
                    result.append(letter)
                else:
                    break
            else:
                if letter == "+" or letter == "-" or letter.isdigit():
                    result.append(letter)
                    sign_found = True
                elif letter != " ":
                    break
        try:            
            result = int("".join(result))
        except:
            return 0
        
        
        if result > 2 ** 31 -1:
            return 2 ** 31 - 1
        if result < -2 ** 31:
            return -2 ** 31
        
        return result
        