"""
https://leetcode-cn.com/problems/assign-cookies/description/
"""

class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int] 孩子
        :type s: List[int] 饼干
        :rtype: int
        """
        g.sort()
        g_i = 0
        s.sort()
        s_i = 0
        child = 0
        while s_i < len(s) and g_i < len(g):
            if s[s_i] >= g[g_i]:
                child += 1
                g_i += 1
            s_i += 1
        return child


if __name__ == "__main__":
    test = Solution()
    data1 = [1, 2]
    data2 = [1, 2, 3]
    a = test.findContentChildren(data1, data2)
    print(a)

