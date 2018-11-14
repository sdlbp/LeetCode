"""
merge-sorted-array
"""
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        self.s_1(nums1, m, nums2, n)

    def s_1(self, nums1, m, nums2, n):
        i, j = m-1, n-1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[i+j+1] = nums1[i]
                i -= 1
            else:
                nums1[i+j+1] = nums2[j]
                j -= 1
        if j >= 0:
            nums1[:i+j+2] = nums2[:j+1]
        print(nums1)

if __name__ == "__main__":
    test = Solution()
    a = test.merge([2,5,6,0,0,0], 3,[1,2,3] , 3)
    print(a)

