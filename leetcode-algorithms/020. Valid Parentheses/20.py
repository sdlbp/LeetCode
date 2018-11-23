class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """
        参考耗时排名较高的算法,对于配对少的话可以采取,
        匹配对多的话,可以使用下面的map
        """
        dic = {"}": "{",
               "{": "}",
               "[": "]",
               "]": "[",
               "(": ")",
               ")": "("}
        stack = []
        for temp in s:
            if len(stack) and temp == dic[stack[-1]]:
                stack.pop()
            else:
                stack.append(temp)
        return not stack


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("{[]}"))
