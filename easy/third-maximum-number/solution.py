# https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(set(nums))
        original_nums = copy.copy(nums)
        
        for i in range(0, 2):
            nums.pop()
            if len(nums) == 0:
                return original_nums[-1]
            
        return nums[-1]