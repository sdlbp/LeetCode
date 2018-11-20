"""
https://leetcode-cn.com/problems/maximum-subarray/description/
"""
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum, current_sum = -float("inf"), 0
        for n in nums:
            # 以每个位置的最大子序列都是基于前一个位置的最大子序列计算得到
            current_sum = max(n, current_sum + n)
            max_sum = max(max_sum, current_sum)
        return max_sum


if __name__ == "__main__":
    test = Solution()
    a = test.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print(a)


