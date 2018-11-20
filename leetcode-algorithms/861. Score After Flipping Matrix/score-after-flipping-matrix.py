"""
https://leetcode-cn.com/problems/jump-game/description/
"""
class Solution:
    def matrixScore(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: bool
        """
        column = 0
        while column < len(nums[0]):
            temp = []
            row = 0
            while row < len(nums):
                if column == 0 and nums[row][column] == 0:
                    nums[row] = [v ^ 1 for v in nums[row]]
                    break
                else:
                    temp.append(nums[row][column])
                    row += 1

            if column != 0:
                if sum(temp) > sum([v ^ 1 for v in temp]):
                    pass
                else:
                    i = 0
                    while i < len(temp):
                        nums[i][column] = temp[i] ^ 1
                        i += 1
            column += 1

        # 计算二进制
        
        return nums


if __name__ == "__main__":
    test = Solution()
    data = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
    a = test.matrixScore(data)
    print(a)

