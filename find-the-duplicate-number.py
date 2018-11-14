"""
find-the-duplicate-number
不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次。
"""
class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.s_1(nums)

    def s_1(self, nums):
        """
        time limit exceeded
        :param nums:
        :return:
        """
        for i, num in enumerate(nums):
            if num in nums[i+1:]:
                return num

    def s_2(self, nums):
        """
        同s_1
        :param nums:
        :return:
        """
        for i, num1 in enumerate(nums):
            for num2 in nums[i+1:]:
                if num1 == num2:
                    return num1

    def s_3(self, nums):
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]

    def s_4(self, nums):
        '''
        换成set更好
        :param nums:
        :return:
        '''
        dict = {}
        for num in nums:
            if num in dict:
                return num
            else:
                dict[num]=0

