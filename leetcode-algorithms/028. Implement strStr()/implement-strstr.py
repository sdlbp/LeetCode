"""
implement-strstr
"""
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return self.s_2(haystack, needle)

    def s_2(self, haystack, needle):
        return haystack.find(needle)

    def s_1(self, haystack, needle):
        if len(needle) == 0:
            return 0
        if needle in haystack:
            haystack = list(haystack)
            needle = list(needle)
            for i, str in enumerate(haystack):
                if needle == haystack[i: len(needle) + i]:
                    return i
        return -1


if __name__ == "__main__":
    test = Solution()
    print(test.strStr("hello", "ll"))
