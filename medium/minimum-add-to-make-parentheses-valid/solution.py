# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/submissions/

class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        # All Parenthesis
        S = list(S)
        # All Truth Values
        T = [True] * len(S)
        # All Parenthesis & Respective Truth Values
        P = zip(S, T)
        
        for i in range(0, len(P)):
            # Skip if element already used
            if not P[i][1]:
                continue
            curr = P[i][0]
            
            if curr == "(":
                for j in range(i, len(P)):
                    if P[j][0] == ")" and P[j][1]:
                        P[i] = ("", False)
                        P[j] = ("", False)
                        break
                        
            if curr == ")":
                for j in range(0, i):
                    if P[j][0] == "(" and P[j][1]:
                        P[i] = ("", False)
                        P[j] = ("", False)
                        break
        
        problems = 0
        for i in range(0, len(P)):
            if P[i][1]:
                problems +=1
                
        return problems