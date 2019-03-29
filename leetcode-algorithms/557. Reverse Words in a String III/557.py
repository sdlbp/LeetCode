"""
reverse-words-in-a-string-iii
"""
class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.v_1(s)

    def v_1(self, s):
        ans = []
        for s in s.split(" "):
            ans.append(s[::-1])
        return " ".join(ans)

    def v_2(self, s):
        return " ".join([i[::-1] for i in s.split(" ")])

