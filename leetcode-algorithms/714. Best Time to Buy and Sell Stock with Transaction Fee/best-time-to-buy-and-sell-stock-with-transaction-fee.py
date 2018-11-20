"""
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/
v1
"""
class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        buy = sell = prices[0]
        max_pro = i = 0
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            buy = prices[i]
            while i < len(prices) - 1:
                i += 1
                if prices[i] - fee > prices[i + 1]:
                    break
            sell = prices[i]
            if buy != sell:
                max_pro = sell - buy - fee

        return max_pro


if __name__ == "__main__":
    test = Solution()
    data = [1,3,2,8,4,9]
    # data = [7, 1, 5, 3, 6, 4]
    a = test.maxProfit(data, 2)

    print(a)
