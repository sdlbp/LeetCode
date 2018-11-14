"""
remove-element
"""
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        return self.s_1(nums, val)


    def s_1(self, nums, val):
        """
        error
        :param nums:
        :param val:
        :return:
        """
        if len(nums) == 0:
            return 0

        l, r = 0, len(nums) - 1
        while r > l:
            if nums[l] == val and nums[r] != val:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

            if nums[l] != val:
                l += 1
            if nums[r] == val:
                r -= 1
        return max(l, r) + 1


    def s_2(self, nums, val):
        j = 0
        for i, n in enumerate(nums):
            if n != val:
                nums[i] = nums[j]
                j += 1
        return j

if __name__ == "__main__":
    test = Solution()
    data = [2, 2, 2]
    a = test.removeElement(data, 3)
    print(a)