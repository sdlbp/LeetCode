"""
https://leetcode.com/problems/array-partition-i/description/
"""
class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum(nums[::2])


if __name__ == "__main__":
    test = Solution()
    data = [1, 4, 3, 2]
    a = test.arrayPairSum(data)
    print(a)
