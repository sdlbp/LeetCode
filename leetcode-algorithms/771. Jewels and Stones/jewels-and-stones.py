"""
https://leetcode-cn.com/problems/jewels-and-stones/description/
v1
"""

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        all_ = 0
        for s in S:
            if s in J:
                all_ += 1
        return all_