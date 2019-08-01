# https://leetcode.com/problems/k-diff-pairs-in-an-array/submissions/

class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        if k < 0:
            return 0
        
        count = collections.Counter(nums)
        
        if k == 0:
            duplicates = 0
            for v in count.values():
                if v > 1:
                    duplicates += 1
            return duplicates
        
        found = []
        for i in count:
            if i + k in count:
                found.append(tuple(sorted([i, i+k])))
            elif i - k in count:
                found.append(tuple(sorted([i, i-k])))
                
        return len(set(found))