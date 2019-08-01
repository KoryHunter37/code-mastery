# https://leetcode.com/problems/remove-outermost-parentheses/submissions/

class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        count = 0
        result = []
        for letter in S:
            if letter == '(':
                count += 1
                
            if count != 1 or letter != '(' and letter != ')':
                result.append(letter)
                
            if letter == ')':
                count -= 1
                
        return ''.join(result)