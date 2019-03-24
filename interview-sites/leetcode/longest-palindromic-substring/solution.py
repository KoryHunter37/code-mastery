# https://leetcode.com/problems/longest-palindromic-substring/submissions/

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 1:
            return ""
        
        # Has a Center
        center = 0
        end = len(s) - 1
        
        current = s[center]
        best = s[0]
        
        s = list(s)
        
        while center <= end:
            left = center - 1
            right = center + 1
            
            while left >= 0 and right <= end:
                if s[left] != s[right]:
                    break
                else:
                    current = s[left:right+1]
                    left -= 1
                    right += 1
            
            if len(current) > len(best):
                best = current
                
            center += 1
            
        # No Center
        if len(s) < 2:
            return best
        
        center = 0
        left = 0
        right = 1
        end = len(s) - 1
        
        current = s[0]
        
        s = list(s)
        
        while left <= end:
            left = center
            right = center + 1
            while left >= 0 and right <= end:
                if s[left] != s[right]:
                    break
                else:
                    current = s[left:right+1]
                    left -= 1
                    right += 1
            
            if len(current) > len(best):
                best = current
                
            center += 1
            
        return "".join(best)