"""
https://leetcode-cn.com/problems/jump-game-ii/description/
反转数组后每次都跳跃最大的步数 -- error
"""
class Solution:
    def jump(self, A):
        """
        v2
        :type A: List[int]
        :rtype: int
        """
        last_max_reach, current_max_reach = 0, 0
        njump, i = 0, 0
        while current_max_reach < len(A) - 1:
            while i <= last_max_reach:
                current_max_reach = max(i + A[i], current_max_reach)
                i += 1
            if last_max_reach == current_max_reach:
                return -1
            last_max_reach = current_max_reach
            njump += 1
        return njump


if __name__ == "__main__":
    test = Solution()
    a = test.jump([3,2,1,0,4])
    # print(a)