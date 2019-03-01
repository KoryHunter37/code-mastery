# https://leetcode.com/problems/jump-game/submissions/

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # If input is null, return False
        if not nums:
            return False
        # If there is only one element, we're already at the goal, so return True
        if len(nums) == 1:
            return True    
        # If there are no zeroes in the list, we can always reach the goal, so return True
        if 0 not in nums:
            return True
        # If the starting position has a zero, there's no way to reach goal, so return False
        if nums[0] == 0:
            return False
        
        # Find all zeroes
        zeroes = []
        for i in range(0, len(nums)):
            if nums[i] == 0:
                zeroes.append(i)
        
        # Check to see if every zero found can be "jumped" over by any preceeding number
        for z in zeroes:
            print(z)
            for i in reversed(range(0, z)):
                # Check to see if the value at this index can "jump" over the zero or to the goal
                if i + nums[i] > z or i + nums[i] >= len(nums) - 1:
                    break
                # If the starting position has been reached, and no jump has been found, it's impassable
                if i == 0:
                    print(z)
                    return False
        
        return True