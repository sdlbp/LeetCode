"""
https://leetcode-cn.com/problems/climbing-stairs/description/
"""
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 3
        a, b = 3, 5
        for i in range(3, n):
            a, b = b, a + b
        return a


if __name__ == "__main__":
    test = Solution()
    print(test.climbStairs(6))
