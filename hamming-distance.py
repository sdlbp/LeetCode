"""
https://leetcode.com/problems/hamming-distance/submissions/1
v2
"""
class Solution:
    def hammingDistance(self, x, y):
        """
        v2
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count(1)
