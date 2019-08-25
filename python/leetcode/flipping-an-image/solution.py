# https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        
        def flip(A):
            for i in range(len(A)):
                row = (A[i])[::-1]
                A[i] = row
            return A
        
        def invert(A):
            for i in range(len(A)):
                row = A[i]
                for j in range(len(row)):
                    if row[j] == 0:
                        row[j] = 1
                    elif row[j] == 1:
                        row[j] = 0
                A[i] = row
            return A
        
        return invert(flip(A))