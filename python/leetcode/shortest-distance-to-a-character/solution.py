# https://leetcode.com/problems/shortest-distance-to-a-character/description/

class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        
        distances = []
        valid_indices = []
        
        S = list(S)
        
        for i in range(0, len(S)):
            if S[i] == C:
                distances.append(0)
                valid_indices.append(i)
            else:
                distances.append(float("inf"))
                
        for d in range(0, len(distances)):
            if distances[d] != 0:
                best_distance = distances[d]
                for index in valid_indices:
                    next_distance = abs(d - index)
                    if next_distance < best_distance:
                        best_distance = next_distance
                distances[d] = best_distance
                
        return distances