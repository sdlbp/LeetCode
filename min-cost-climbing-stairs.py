"""
https://leetcode-cn.com/problems/min-cost-climbing-stairs/description/
"""

class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        """
        true
        两条并线进行
        """
        a, b = cost[0], cost[1]

        for i in cost[2:]:
            a, b = b, min(a, b) + i

        return min(a, b)


if __name__ == "__main__":
    test = Solution()
    source = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    source = [10, 15, 20]
    source = [1, 2, 3, 4, 5]
    a = test.minCostClimbingStairs(source)
    print(a)
