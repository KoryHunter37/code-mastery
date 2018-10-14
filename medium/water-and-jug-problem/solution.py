# https://leetcode.com/problems/water-and-jug-problem/submissions/

from fractions import gcd

class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        # Zero requirement is met automatically
        if z == 0:
            return True
        # Cannot meet requirement if greater than sum of jugs
        if z > x + y:
            return False
        
        # Must be a multiple of the greatest common denominator
        GCD = gcd(x, y)
        return z % GCD == 0