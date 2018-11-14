"""
https://leetcode-cn.com/problems/jump-game/description/

"""

class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last_pos = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if nums[i]+i >= last_pos:
                last_pos = i
        return last_pos == 0

if __name__ == "__main__":
    test = Solution()
    a = test.canJump([3,2,1,0,5,4])
    print(a)
