"""
https://leetcode-cn.com/problems/backspace-string-compare/description/
"""
class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        self.solution_v1(S, T)

    def solution_v1(self, S, T):
        s, t = "", ""
        for str in S:
            if str == "#":
                s = s[:len(s)-1]
            else:
                s += str

        for str in T:
            if str == "#":
                t = t[:len(t)-1]
            else:
                t += str
        return s == t


if __name__ == "__main__":
    test = Solution()
    a = test.backspaceCompare("a##c", "a#c#")
    print(a)
