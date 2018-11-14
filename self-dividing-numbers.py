"""
https://leetcode-cn.com/problems/self-dividing-numbers/description/
"""
class Solution:
    def selfDividingNumbers(self, left, right):
        """
        v2
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ans = []
        for num in range(left, right + 1):
            temp = num
            while temp > 0:
                i = temp % 10
                if i != 0 and num % i == 0:
                    temp = temp // 10
                else:
                    break
            if temp <= 0:
                ans.append(num)
        return ans


if __name__ == "__main__":
    test = Solution()
    a = test.selfDividingNumbers(1, 22)
    print(a)
