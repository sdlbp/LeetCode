"""
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/description/
"""

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxpro = 0
        for i in range(1, len(prices)):
            print(prices[i])
            print(prices[i - 1])
            if prices[i] > prices[i-1]:
                maxpro += prices[i] - prices[i-1]
        return maxpro


if __name__ == "__main__":
    test = Solution()
    data = [1, 2, 3, 4, 5]
    # data = [7, 1, 5, 3, 6, 4]
    a = test.maxProfit(data)

    print(a)
