"""
https://leetcode-cn.com/problems/move-zeroes/description/
"""

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        self.two_point2(nums)

    def two_point2(self, nums):
        """
        v3
        j 标识0
        i 标识非0
        :param nums:
        :return:
        """
        j = -1
        for i, v in enumerate(nums):
            if v != 0:
                j += 1
                nums[j], nums[i] = nums[i], nums[j]

    def two_point(self, nums):
        """
        v2-error
        同时保持非零元素顺序
        :param nums:
        :return:
        """
        left, right = 0, len(nums) - 1
        while right > left:
            if nums[left] == 0 and nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            elif nums[left] != 0:
                left += 1
            elif nums[right] == 0:
                right -= 1
        print(nums)

    def sort_move(self, nums):
        nums.sort(key=lambda x: x == 0)
        print(nums)


if __name__ == "__main__":
    test = Solution()
    data = [0, 1, 4, 3, 0, 2, 0]
    data = [1, 0, 1]
    # data = [1, 2]
    test.moveZeroes(data)

