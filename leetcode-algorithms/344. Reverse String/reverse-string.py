"""
https://leetcode-cn.com/problems/reverse-string/description/
"""

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = list(s)
        left, right = 0, len(r)
        while left < right:
            r[left], r[right] = r[right], r[left]
            left += 1
            right -= 1
        return "".join(r)
