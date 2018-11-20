"""
https://leetcode.com/problems/intersection-of-two-arrays/description/
"""
class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return set(nums1) & set(nums2)


if __name__ == "__main__":
    test = Solution()
    a = test.intersection([1, 2, 4, 3, 2], [4, 5, 6])
    print(a)