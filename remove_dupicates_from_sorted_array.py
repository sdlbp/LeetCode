"""
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/solution/
双指针法
"""

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        lastInx = 0
        for i in range(len(nums)):
            if nums[i] > nums[lastInx]:
                lastInx += 1
                nums[lastInx] = nums[i]
        # print(nums)
        return lastInx + 1


if __name__ == "__main__":
    test = Solution()
    print(test.removeDuplicates([1, 1, 2, 3, 3, 3, 3]))

