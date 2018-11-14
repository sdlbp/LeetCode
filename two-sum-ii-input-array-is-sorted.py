"""
https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/description/
"""
class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        return self.map_solution(numbers, target)

    def two_pointer(self, nums, target):
        """
        v1
        :param nums:
        :param target:
        :return:
        """
        l, r = 0, len(nums) - 1
        while r > l:
            if nums[l] + nums[r] == target:
                return [l + 1, r + 1]
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                l += 1

    def map_solution(self, nums, target):
        dic = {}
        for i, num in enumerate(nums):
            if target - num in dic:
                return [dic[target - num] + 1, i + 1]
            else:
                dic[num] = i


if __name__ == "__main__":
    test = Solution()
    print(test.twoSum([2,7,11,15], 9))
