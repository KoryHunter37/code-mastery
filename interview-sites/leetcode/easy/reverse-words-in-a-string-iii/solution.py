# https://leetcode.com/problems/reverse-words-in-a-string-iii/description/

class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        s_reverse = s.split()
        for i, word in enumerate(s_reverse):
            s_reverse[i] = (s_reverse)[i][::-1]
            
        reverse = ""
        for word in s_reverse:
            reverse += word
            reverse += " "
            
        return reverse