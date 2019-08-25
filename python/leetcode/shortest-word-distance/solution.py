# https://leetcode.com/problems/shortest-word-distance/submissions/

class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        w1_indices = [i for i in range(len(words)) if words[i] == word1]
        w2_indices = [i for i in range(len(words)) if words[i] == word2]
        
        distances = [abs(i-j) for i in w1_indices for j in w2_indices]
        return min(distances)
        