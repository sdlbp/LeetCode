class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        R, C = len(A), len(A[0])
        ans = [[None] * R for _ in range(C)]
        for i, v1 in enumerate(A):
            for j, v2 in enumerate(v1):
                ans[i][j] = A[j][i]
        return ans


if __name__ == "__main__":
    test = Solution()
    print(test.transpose([[1, 2], [3, 4]]))
