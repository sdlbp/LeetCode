"""
k-diff-pairs-in-an-array
"""
class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.s_1(k, nums)

    def s_1(self, k, nums):
        """
        双指针
        :param k:
        :param nums:
        :return:
        """
        if len(nums) < 2:
            return 0
        ans = set()
        nums.sort()
        i, j = 0, 1
        while j < len(nums):
            if nums[j] - nums[i] == k:
                ans.add((nums[i], nums[j]))
                i, j = i + 1, i + 2
            elif nums[j] - nums[i] > k:
                i, j = i + 1, i + 2
            else:
                j += 1
        return len(ans)


if __name__ == "__main__":
    test = Solution()
    a = test.findPairs([1, 3, 1, 5, 4], 0)
    print(a)