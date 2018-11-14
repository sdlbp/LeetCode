"""
https://leetcode-cn.com/problems/robot-return-to-origin/description/
"""
class Solution:
    def judgeCircle(self, moves):
        """
        v1
        :type moves: str
        :rtype: bool
        """
        return moves.count("R") == moves.count("L") and moves.count("U") == moves.count("D")
