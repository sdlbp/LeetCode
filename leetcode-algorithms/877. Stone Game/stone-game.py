"""
stone-game
"""
class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        return self.v_1()

    def v_1(self):
        """
        1.可以确定一定可以只拿偶数堆或者基数堆
        2.偶数堆或者奇数堆一定不相等
        :return:
        """
        return True
