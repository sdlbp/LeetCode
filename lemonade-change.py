"""
https://leetcode-cn.com/problems/lemonade-change/description/
"""

class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five, ten, twenty = 0, 0, 0
        for i in bills:
            if i == 5:
                five += 1
            elif i == 10 and five > 0:
                ten += 1
                five -= 1
            elif i == 20 and five > 0:
                if ten > 0 and five >= 1:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
            else:
                return False
        return True


if __name__ == "__main__":
    test = Solution()
    print(test.lemonadeChange([5,5,10,10,5,20,5,10,5,5]))
