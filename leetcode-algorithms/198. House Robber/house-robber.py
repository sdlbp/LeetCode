"""
https://leetcode-cn.com/problems/house-robber/description/
"""
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f1, f2 = 0, 0
        for i in nums:
            f1, f2 = f2, max(f1 + i, f2)
        return f2


if __name__ == "__main__":
    test = Solution()
    a = test.rob([1, 4, 3, 2])
    print(a)
