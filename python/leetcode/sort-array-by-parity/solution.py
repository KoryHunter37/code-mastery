# https://leetcode.com/problems/sort-array-by-parity/description/

class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        evens = []
        odds = []
        
        for number in A:
            if number % 2 == 0:
                evens.append(number)
            else:
                odds.append(number)
               
        evens_and_odds = evens + odds
        return evens_and_odds