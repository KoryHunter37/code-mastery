# https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        r1 = "qwertyuiop"
        r2 = "asdfghjkl"
        r3 = "zxcvbnm"
        
        valid_words = []
        
        for word in words:
            chosen_row = None
            valid = True
            for letter in word:
                letter = letter.lower()
                if letter in r1 and (chosen_row is None or chosen_row == r1):
                    chosen_row = r1
                elif letter in r2 and (chosen_row is None or chosen_row == r2):
                    chosen_row = r2
                elif letter in r3 and (chosen_row is None or chosen_row == r3):
                    chosen_row = r3
                else:
                    valid = False
                    break
                    
            if valid:
                valid_words.append(word)
                
        return valid_words