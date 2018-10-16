# https://leetcode.com/problems/unique-morse-code-words/description/

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        morse_list = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        
        alphabet_morse_zip = zip(alphabet_list, morse_list)
        
        alphabet_morse_list = list(alphabet_morse_zip)
        
        alphabet_morse_dictionary = {}
        
        for letter, morse in alphabet_morse_list:
            alphabet_morse_dictionary[letter] = morse
            
        translations = []    
        
        for word in words:
            new_translation = []
            for letter in word:
                new_translation.append(alphabet_morse_dictionary[letter])
            translations.append("".join(new_translation))
            
        translations = set(translations)
        return len(translations)