"""
https://leetcode.com/problems/third-maximum-number/description/
"""

class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return max(nums)
        (max1, max2, max3) = (nums[0], None, None)
        for num in nums:
            if num not in (max1, max2, max3):
                if num > max1:
                    (max1, max2, max3) = (num, max1, max2)
                elif not max2 or max2 < num:
                    max2, max3 = num, max2
                elif not max3 or max3 < num:
                    max3 = num
        return max3 if max3 != None else max1


if __name__ == "__main__":
    test = Solution()
    print(test.thirdMax([1, 2, 3, 10, 11, 23, 45, 12, 3, 4]))


