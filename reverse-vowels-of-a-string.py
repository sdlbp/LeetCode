"""
reverse-vowels-of-a-string
"""
class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.s_2(s)


    def s_1(self, s):
        y = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        i, j = 0, len(s) - 1
        s_l = list(s)
        i_f, j_f = False, False
        while j > i:
            if s_l[i] in y and not i_f:
                i_f = True
            elif s_l[i] not in y and not i_f:
                i += 1
            if s_l[j] in y and not j_f:
                j_f = True
            elif s_l[j] not in y and not j_f:
                j -= 1
            if i_f and j_f:
                s_l[i], s_l[j] = s_l[j], s_l[i]
                i_f, j_f = False, False
                i += 1
                j -= 1

        return "".join(s_l)

    def s_2(self, s):
        y = set("aeiouAEIOU")
        i, j = 0, len(s) - 1
        s_l = list(s)
        while j > i:
            if s_l[i] in y and s_l[j] in y:
                s_l[i], s_l[j] = s_l[j], s_l[i]
                i += 1
                j -= 1
            if s_l[i] not in y:
                i += 1
            if s_l[j] not in y:
                j -= 1

        return "".join(s_l)


if __name__ == "__main__":
    test = Solution()
    print(test.reverseVowels("leetcode"))