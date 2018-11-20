"""
https://leetcode.com/problems/can-place-flowers/description/
"""
class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        length = len(flowerbed)
        i, count = 1, 0
        flowerbed = [0] + flowerbed + [0]
        while i <= length:
            if flowerbed[i] + flowerbed[i - 1] + flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                count += 1
            i += 1
        return count >= n, flowerbed


if __name__ == "__main__":
    test = Solution()
    a = [0, 0, 1, 0, 1]
    a = [0, 1, 0, 0, 1, 0]
    a = [1, 0, 0, 0, 1, 0, 0]
    result, flowerbed = test.canPlaceFlowers(a, 2)
    print(result, flowerbed)


