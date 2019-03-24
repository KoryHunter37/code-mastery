# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) < 1:
            return 0
        
        s = list(s)
        
        ptr = 0
        count = 1
        best_count = 1
        
        while ptr <= len(s) - 1:
            chars = [s[ptr]]
            for i in range(ptr + 1, len(s)):
                if s[i] in chars:
                    break
                else:
                    chars.append(s[i])
                    count += 1
            best_count = max(count, best_count)
            count = 1
            ptr = ptr + 1
        
        return best_count