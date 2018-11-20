"""
counting-bits
TODO dp 解法
"""
class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        return [bin(n).count("1") for n in range(num + 1)]


if __name__ == "__main__":
    t = Solution()
    print(t.countBits(20))

