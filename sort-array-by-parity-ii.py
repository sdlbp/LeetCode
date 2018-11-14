"""
https://leetcode.com/problems/sort-array-by-parity-ii/description/
"""
class Solution:
    def sortArrayByParityII(self, A):
        """
        v1
        :type A: List[int]
        :rtype: List[int]
        """
        i, even, odd = 0, 0, 1
        while i < len(A):
            if i % 2 == 0 and A[i] % 2 != 0:
                A[i], A[odd] = A[odd], A[i]
                odd += 2
            elif i % 2 == 1 and A[i] % 2 != 1:
                A[i], A[even] = A[even], A[i]
                even += 2
            else:
                i += 1
        return A
