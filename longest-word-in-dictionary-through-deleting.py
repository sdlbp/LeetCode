"""
longest-word-in-dictionary-through-deleting
"""
class Solution:
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        return self.s_1(d, s)

    def s_3(self, s, d):
        """
        借助index函数
        :param s:
        :param d:
        :return:
        """
        def ss(s, w):
            try:
                i = 0
                for c in w:
                    i = s.index(c, i) + 1
                return True
            except:
                return False
        ans = ""
        for c in d:
            if not ss(s, c):
                continue
            if len(c) > len(ans) or (len(c) == len(ans) and c < ans):
                ans = c
        return ans


    def s_2(self, s, d):
        ans = ""
        for ss in d:
            i, j = 0, 0
            while i < len(s) and j < len(ss):
                if ss[j] == s[i]:
                    j += 1
                    i += 1
                else:
                    i += 1
            if j == len(ss):
                if len(ss) > len(ans) or (len(ss) == len(ans) and ss < ans):
                    ans = ss
        return ans

    def s_1(self, d, s):
        ans = [""]
        for ss in d:
            i, j = 0, 0
            while i < len(s) and j < len(ss):
                if ss[j] == s[i]:
                    j += 1
                    i += 1
                else:
                    i += 1
            if j == len(ss):
                if len(ss) > len(ans[-1]):
                    ans = []
                    ans.append(ss)
                elif len(ss) == len(ans[-1]):
                    ans.append(ss)
        return min(ans)

                