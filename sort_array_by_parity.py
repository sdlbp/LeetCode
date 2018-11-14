"""
https://leetcode.com/problems/sort-array-by-parity/solution/
"""
class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # 数组相加法
        return ([x for x in A if x % 2 == 0] +
                [x for x in A if x % 2 == 1])


if __name__ == "__main__":
    test = Solution()
    a = test.sortArrayByParity([1, 0, 1])
    print(a)
