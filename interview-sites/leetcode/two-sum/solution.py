# https://leetcode.com/problems/two-sum/description/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in nums and nums.index(comp) != i:
                val1 = i
                val2 = nums.index(comp)
                return [val1, val2]