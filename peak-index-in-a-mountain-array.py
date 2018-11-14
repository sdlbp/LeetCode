"""
peak-index-in-a-mountain-array
"""
class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return self.s_2(A)

    def s_1(self, A):
        ans = A[0]
        for i, num in enumerate(A):
            if num >= ans:
                ans = num
            else:
                return i - 1

    def s_2(self, A):
        return A.index(max(A))


    def s_3(self, A):
        """
        双指针
        :param A:
        :return:
        """
        left, right = 0, len(A) - 1
        while left != right:
            if A[left] > A[right]:
                right -= 1
            else:
                left += 1
        return left
