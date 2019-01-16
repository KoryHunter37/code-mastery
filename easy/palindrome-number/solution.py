# https://leetcode.com/problems/palindrome-number/submissions/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        :type x: int
        :rtype: bool
        """
        
        x = list(str(x))
        for start in range(0, len(x)):
            end = len(x) - 1 - start
            
            if end <= start:
                return True
            
            if x[start] != x[end]:
                return False
